#!/usr/bin/env python3
"""Quick, high-yield proofing scan for scientific manuscripts.

Goal: catch *high-confidence* defects that are easy to miss in a manual pass:
- duplicated punctuation (", ,", ",,", "..", '" , ,')
- semicolon-capitalization anomalies ('; A' etc.)
- equation-adjacent malformed frames ("into ... into ...", "plugging ... into together")
- common product/language capitalization (javascript/iOS/iPhone)
- arctan(x/y) quadrant ambiguity patterns
- thesis/LaTeX finalization hazards (TODO/FIXME/TBD/XXX, empty refs/cites,
  unresolved "??" references, repeated words)

Usage:
  python scripts/proofing_scan.py <path-to-pdf-or-text> [--max-hits 80]

Output:
  One line per hit:
    [RULE_ID] p<page>: <snippet>
    [RULE_ID] l<line>: <snippet>

Notes:
- Page numbers are 1-indexed.
- Text and LaTeX line numbers are 1-indexed.
- Snippets are best-effort and may include line breaks collapsed to spaces.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import List, Tuple


SourceChunk = Tuple[str, str]


def _read_pdf_pages(pdf_path: Path) -> List[SourceChunk]:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: pypdf. Install skill dependencies with: "
            "python -m pip install -r requirements.txt"
        ) from exc

    reader = PdfReader(str(pdf_path))
    pages = []
    for i, p in enumerate(reader.pages, start=1):
        try:
            txt = p.extract_text() or ""
        except Exception:
            txt = ""
        txt = re.sub(r"\s+", " ", txt).strip()
        pages.append((f"p{i}", txt))
    return pages


def _read_text_lines(path: Path) -> List[SourceChunk]:
    chunks: List[SourceChunk] = []
    for line_no, line in enumerate(path.read_text(errors="ignore").splitlines(), start=1):
        txt = re.sub(r"\s+", " ", line).strip()
        if txt:
            chunks.append((f"l{line_no}", txt))
    return chunks


def _snip(text: str, start: int, end: int, window: int = 60) -> str:
    lo = max(0, start - window)
    hi = min(len(text), end + window)
    snippet = text[lo:hi]
    return snippet.strip()


def _mask_inline_code(text: str) -> str:
    return re.sub(r"`[^`]*`", lambda m: "M" * (m.end() - m.start()), text)


def _find_regex(
    rule_id: str,
    pattern: re.Pattern,
    chunks: List[SourceChunk],
    max_hits: int,
) -> List[Tuple[str, str, str]]:
    hits: List[Tuple[str, str, str]] = []
    for location, text in chunks:
        if not text:
            continue
        scan_text = _mask_inline_code(text)
        for m in pattern.finditer(scan_text):
            hits.append((rule_id, location, _snip(text, m.start(), m.end())))
            if len(hits) >= max_hits:
                return hits
    return hits


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", type=str, help="PDF or text file")
    ap.add_argument(
        "--max-hits",
        type=int,
        default=80,
        help="Cap total hits across all rules",
    )
    args = ap.parse_args()

    if args.max_hits < 1:
        raise SystemExit("--max-hits must be at least 1")

    path = Path(args.path)
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    if path.suffix.lower() == ".pdf":
        chunks = _read_pdf_pages(path)
    else:
        chunks = _read_text_lines(path)

    rules: List[Tuple[str, re.Pattern]] = [
        ("PUNC_DOUBLE_COMMA", re.compile(r",\s*,")),
        ("PUNC_DOUBLE_PERIOD", re.compile(r"(?<!\.)\.\s*\.(?!\.)")),
        ("PUNC_QUOTE_DOUBLE_COMMA", re.compile(r"\"\s*,\s*,")),
        ("SEMICOLON_CAP", re.compile(r";\s+[A-Z]")),
        ("FRAME_INTO_INTO", re.compile(r"\binto\b.{0,80}?\binto\b", re.IGNORECASE)),
        (
            "FRAME_PLUGGING_INTO_TOGETHER",
            re.compile(r"plugging\s+into\s+together", re.IGNORECASE),
        ),
        ("CAP_JAVASCRIPT", re.compile(r"\bjavascript\b")),
        ("CAP_IOS", re.compile(r"\bios\b")),
        ("CAP_IPHONE", re.compile(r"\biphone\b")),
        (
            "ARCTAN_DIV",
            re.compile(
                r"\barctan\s*\(\s*[^()]{0,40}?/[^()]{0,40}?\)",
                re.IGNORECASE,
            ),
        ),
        ("DRAFT_MARKER", re.compile(r"\\todo\b|\b(?:TODO|FIXME|TBD|XXX)\b")),
        ("EMPTY_CITE", re.compile(r"\\(?:cite|citet|citep|autocite)\s*\{\s*\}")),
        ("EMPTY_REF", re.compile(r"\\(?:ref|eqref|autoref|cref|Cref)\s*\{\s*\}")),
        ("UNRESOLVED_REF_MARKER", re.compile(r"(?<!\?)\?\?(?!\?)")),
        (
            "REPEATED_WORD",
            re.compile(r"\b([A-Za-z]{3,})\s+\1\b", re.IGNORECASE),
        ),
    ]

    remaining = args.max_hits
    out: List[Tuple[str, str, str]] = []
    for rule_id, pat in rules:
        if remaining <= 0:
            break
        hits = _find_regex(rule_id, pat, chunks, remaining)
        out.extend(hits)
        remaining = args.max_hits - len(out)

    if not out:
        print("[OK] No high-confidence pattern-scan hits found.")
        return

    for rule_id, location, snippet in out:
        print(f"[{rule_id}] {location}: {snippet}")


if __name__ == "__main__":
    main()

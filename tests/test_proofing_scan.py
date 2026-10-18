from __future__ import annotations

import sys
import unittest
from pathlib import Path

# Add scripts directory to path
repo_root = Path(__file__).resolve().parent.parent
scripts_dir = repo_root / "paper-review" / "scripts"
if str(scripts_dir) not in sys.path:
    sys.path.insert(0, str(scripts_dir))

import proofing_scan
from proofing_scan import SourceChunk, _find_regex, _mask_inline_code, _read_text_lines


class TestProofingScan(unittest.TestCase):
    def test_source_chunk_type_alias(self) -> None:
        chunk: SourceChunk = ("l1", "Sample text")
        self.assertEqual(chunk[0], "l1")
        self.assertEqual(chunk[1], "Sample text")

    def test_mask_inline_code(self) -> None:
        text = "Check `code with , , inside` and outside"
        masked = _mask_inline_code(text)
        self.assertNotIn(", ,", masked)
        self.assertIn("MMMMMMMMMMMMMMMMMMM", masked)

    def test_read_text_lines(self) -> None:
        import tempfile

        with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as f:
            f.write("First line\n\nSecond line\n")
            temp_path = Path(f.name)

        try:
            chunks = _read_text_lines(temp_path)
            self.assertEqual(len(chunks), 2)
            self.assertEqual(chunks[0], ("l1", "First line"))
            self.assertEqual(chunks[1], ("l3", "Second line"))
        finally:
            temp_path.unlink(missing_ok=True)

    def test_find_regex_draft_marker(self) -> None:
        import re

        chunks: list[SourceChunk] = [("l1", "Here is a TODO marker for draft.")]
        pattern = re.compile(r"\\todo\b|\b(?:TODO|FIXME|TBD|XXX)\b")
        hits = _find_regex("DRAFT_MARKER", pattern, chunks, max_hits=10)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0][0], "DRAFT_MARKER")
        self.assertEqual(hits[0][1], "l1")
        self.assertIn("TODO", hits[0][2])


if __name__ == "__main__":
    unittest.main()

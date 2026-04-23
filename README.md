# Paper Review Skill

Codex skill for reviewing scientific and technical manuscripts, especially LaTeX drafts.

The skill focuses on technical correctness first:

- equations, derivations, notation, units, and algorithmic correctness
- consistency between claims, evidence, figures, tables, captions, and conclusions
- unsupported claims, implementation ambiguity, and factual problems
- meaningful editorial issues and high-confidence proofing defects

## Contents

- `SKILL.md` - skill instructions and workflow
- `scripts/proofing_scan.py` - mechanical scan for common proofing issues
- `references/review-rubric.md` - compact review checklist
- `requirements.txt` - Python dependency for the proofing scan

## Installation

Copy this directory into your Codex skills folder:

```powershell
Copy-Item -Path . -Destination "$env:USERPROFILE\.codex\skills\paper-review" -Recurse
```

Restart Codex after installing or updating the skill.

## Script Setup

Install the Python dependency before running the proofing scan:

```powershell
python -m pip install -r requirements.txt
```

# Paper Review Skill

This repository contains an agent skill for reviewing scientific and technical manuscripts, papers, theses, dissertation chapters, and final submission drafts.

The skill lives in [`paper-review/`](paper-review/) and is defined by [`paper-review/SKILL.md`](paper-review/SKILL.md). It includes:

- review workflow instructions focused on technical correctness first
- thesis-specific review guidance
- bundled review rubrics in `paper-review/references/`
- a proofing helper script in `paper-review/scripts/proofing_scan.py`

## Install Locally

Preferred: ask your local agent to install the skill for you:

```text
Install the paper-review skill from https://github.com/JustAmply/paper-review-skill by copying the paper-review directory into my local agent skills folder as paper-review.
```

### Manual Fallback

The commands below install the skill for Codex by copying the actual skill directory into the Codex skills folder.

#### Windows

```powershell
Copy-Item -Recurse -Force ".\paper-review" "$env:USERPROFILE\.codex\skills\"
```

#### macOS and Linux

```bash
mkdir -p "$HOME/.codex/skills"
cp -R ./paper-review "$HOME/.codex/skills/"
```

If a previous copy already exists, these commands refresh files with the same names in place.

## Requirements

The proofing scan can process text-like files without extra setup. PDF scanning requires the Python dependency listed in:

```powershell
python -m pip install -r paper-review\requirements.txt
```

## Usage

Once installed, ask your agent to review a manuscript, paper, thesis, thesis chapter, or final submission draft. The skill writes a timestamped LaTeX review file by default under `paper-reviews/`.

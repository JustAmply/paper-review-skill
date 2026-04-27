# Paper Review Skill

This repository contains a Codex skill for reviewing scientific and technical manuscripts, papers, theses, dissertation chapters, and final submission drafts.

The skill lives in [`paper-review/`](paper-review/) and is defined by [`paper-review/SKILL.md`](paper-review/SKILL.md). It includes:

- review workflow instructions focused on technical correctness first
- thesis-specific review guidance
- bundled review rubrics in `paper-review/references/`
- a proofing helper script in `paper-review/scripts/proofing_scan.py`

## Install Locally

Link the actual skill directory into your Codex skills folder:

### Windows

```powershell
New-Item -ItemType Junction `
  -Path "$env:USERPROFILE\.codex\skills\paper-review" `
  -Target "$PWD\paper-review"
```

### macOS and Linux

```bash
mkdir -p "$HOME/.codex/skills"
ln -s "$PWD/paper-review" "$HOME/.codex/skills/paper-review"
```

If a previous link already exists, remove that link first and recreate it with the target above for your operating system.

## Requirements

The proofing scan can process text-like files without extra setup. PDF scanning requires the Python dependency listed in:

```powershell
python -m pip install -r paper-review\requirements.txt
```

## Usage

Once installed, ask Codex to review a manuscript, paper, thesis, thesis chapter, or final submission draft. The skill writes a timestamped LaTeX review file by default under `paper-reviews/`.

# Gemini Gems for Research

Version-controlled Google Gemini Gem prompts for a research group's AI assistants. This is a prototype repository — content here is not for real research use.

## Repository structure

Each Gem lives in its own folder under `gems/`, named in lowercase-hyphenated form (e.g. `data-documenter`). A Gem folder must contain:

- `README.md` (required) — description of the Gem, a link to `instructions.md`, and a "Knowledge" section listing suggested context files.
- `instructions.md` (required) — the Gem's system prompt / instructions.
- `knowledge/` (optional) — supporting reference docs bundled with the Gem.

No other files or folders belong directly under a Gem folder.

## CI checks

- `.github/workflows/markdown-lint.yml` lints all Markdown with markdownlint-cli2, configured via `.markdownlint.yaml` at the repo root.
- `.github/workflows/structure-check.yml` runs `scripts/check_structure.py`, which verifies every folder under `gems/` has the required files and no unexpected entries.
- `.github/workflows/link-check.yml` runs `lychee` over all Markdown files to catch broken links, on push/PR to `main` and monthly on a schedule.

All must pass before merging changes.

## Verification

Before considering a change to `gems/` complete, run:

1. `python scripts/check_structure.py`
2. `npx markdownlint-cli2 "**/*.md"`

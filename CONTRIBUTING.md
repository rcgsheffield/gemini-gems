# Contributing

Thanks for contributing a Gemini Gem to this repository.

## Adding or updating a Gem

1. Create a folder under `gems/` named in lowercase-hyphenated form (e.g. `gems/data-documenter`).
2. Include the required files:
   - `README.md` — description of the Gem, a link to `instructions.md`, and a "Knowledge" section listing suggested context files.
   - `instructions.md` — the Gem's system prompt / instructions.
3. Optionally add a `knowledge/` folder with supporting reference docs.
4. Do not add any other files or folders directly under the Gem folder — CI will reject them.

## Before opening a pull request

Run the same checks CI runs:

```bash
python scripts/check_structure.py
```

Also lint your Markdown against `.markdownlint.yaml` (e.g. with `markdownlint-cli2 "**/*.md"` if you have it installed).

## Pull requests

- Keep changes scoped to one Gem where possible.
- Describe what the Gem does and any testing/review performed on the prompt.
- Both the markdown-lint and directory structure checks must pass before merging.

## Reminder

This is a prototype repository — content here is not for real research use.

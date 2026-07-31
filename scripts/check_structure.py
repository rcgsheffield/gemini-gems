#!/usr/bin/env python3
"""Verify that every gem folder under gems/ follows the required structure.

Each gems/<name>/ folder must contain:
  - README.md       (required file)
  - instructions.md (required file)
  - knowledge/       (optional folder)

No other files or folders are allowed directly under a gem folder.
"""

import sys
from pathlib import Path

REQUIRED_FILES = {"README.md", "instructions.md"}
ALLOWED_ENTRIES = REQUIRED_FILES | {"knowledge"}

GEMS_DIR = Path(__file__).resolve().parent.parent / "gems"


def check_gem(gem_dir: Path) -> list[str]:
    errors = []
    entries = {entry.name for entry in gem_dir.iterdir()}

    missing = REQUIRED_FILES - entries
    for name in sorted(missing):
        errors.append(f"{gem_dir.name}: missing required file '{name}'")

    unexpected = entries - ALLOWED_ENTRIES
    for name in sorted(unexpected):
        errors.append(f"{gem_dir.name}: unexpected entry '{name}'")

    knowledge_dir = gem_dir / "knowledge"
    if knowledge_dir.exists() and not knowledge_dir.is_dir():
        errors.append(f"{gem_dir.name}: 'knowledge' must be a directory")

    return errors


def main() -> int:
    if not GEMS_DIR.is_dir():
        print(f"error: {GEMS_DIR} does not exist", file=sys.stderr)
        return 1

    gem_dirs = sorted(p for p in GEMS_DIR.iterdir() if p.is_dir())
    if not gem_dirs:
        print(f"error: no gem folders found under {GEMS_DIR}", file=sys.stderr)
        return 1

    all_errors = []
    for gem_dir in gem_dirs:
        all_errors.extend(check_gem(gem_dir))

    if all_errors:
        print("Directory structure check FAILED:\n")
        for error in all_errors:
            print(f"  - {error}")
        return 1

    print(f"Directory structure check passed for {len(gem_dirs)} gem(s):")
    for gem_dir in gem_dirs:
        print(f"  - {gem_dir.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

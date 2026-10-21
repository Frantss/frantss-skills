#!/usr/bin/env python3
"""Create a portable skill from the repository template."""

import argparse
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def create_skill(root: Path, name: str, description: str) -> Path:
    if len(name) > 64 or not NAME.fullmatch(name):
        raise ValueError("name must be 1-64 lowercase letters/digits with single hyphens")
    description = description.strip()
    if not 1 <= len(description) <= 1024:
        raise ValueError("description must contain 1-1024 characters")
    content = (root / "templates/SKILL.md.tmpl").read_text(encoding="utf-8").format(
        name=name,
        description=json.dumps(description, ensure_ascii=False),
        title=name.replace("-", " ").capitalize(),
    )
    destination = root / "skills" / name
    destination.mkdir(parents=True, exist_ok=False)
    (destination / "SKILL.md").write_text(content, encoding="utf-8")
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name")
    parser.add_argument("--description", required=True)
    args = parser.parse_args()
    try:
        destination = create_skill(ROOT, args.name, args.description)
    except (ValueError, OSError) as error:
        parser.exit(1, f"error: {error}\n")
    print(f"Created {destination.relative_to(ROOT)}/SKILL.md")
    print("Replace the scaffold comments with instructions, then run make validate.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Bundle the shared tracked-run contract inside independently installable skills."""

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BDD_SKILLS = (
    "bdd-frame-problem",
    "bdd-design-solution",
    "bdd-discover-behavior",
    "bdd-formulate-behavior",
    "bdd-slice-work",
    "bdd-implement-ticket",
)
CONTRACT = Path("templates/bdd-run-record.md")
REFERENCE = Path("references/run-record.md")
SKILLS = Path("plugins/frantss-bdd/skills")


def participating_skills(root: Path) -> list[Path]:
    return [root / SKILLS / name for name in BDD_SKILLS
            if (root / SKILLS / name / "SKILL.md").is_file()]


def reference_errors(root: Path) -> list[str]:
    skills = participating_skills(root)
    if not skills:
        return []
    source = root / CONTRACT
    if not source.is_file():
        return [f"{CONTRACT}: missing shared BDD run contract"]
    expected = source.read_bytes()
    errors = []
    for skill in skills:
        destination = skill / REFERENCE
        if not destination.is_file() or destination.read_bytes() != expected:
            errors.append(f"{destination.relative_to(root)}: stale or missing BDD contract; run make sync-bdd")
    return errors


def sync_references(root: Path) -> None:
    expected = (root / CONTRACT).read_bytes()
    for skill in participating_skills(root):
        destination = skill / REFERENCE
        if destination.is_symlink() or destination.parent.is_symlink():
            raise ValueError(f"{destination}: bundle real files and directories")
        destination.parent.mkdir(exist_ok=True)
        if not destination.exists() or destination.read_bytes() != expected:
            destination.write_bytes(expected)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report drift without writing")
    args = parser.parse_args()
    if not args.check:
        sync_references(ROOT)
    errors = reference_errors(ROOT)
    if errors:
        parser.exit(1, "\n".join(errors) + "\n")
    print("BDD reference bundles are current.")


if __name__ == "__main__":
    main()

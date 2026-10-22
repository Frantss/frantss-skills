#!/usr/bin/env python3
"""Check packaging, then delegate format validation to GitHub and Claude CLIs."""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MAX_SKILL_LINES = 75
SKILL_LINE_LIMITS = {
    "frantss-communicate": 50,
    "frantss-update": 50,
    "frantss-persistance": 100,
    "frantss-persistance-obsidian": 100,
}
LINK = re.compile(r'!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:\s+[\'\"][^)\n]*[\'\"])?\s*\)')
FENCE = re.compile(r"^```[^\n]*\n.*?^```\s*$", re.MULTILINE | re.DOTALL)


def packaging_errors(root: Path) -> list[str]:
    errors = []
    try:
        plugin = json.loads((root / ".claude-plugin/plugin.json").read_text())
        codex = json.loads((root / ".codex-plugin/plugin.json").read_text())
        market = json.loads((root / ".claude-plugin/marketplace.json").read_text())
        entries = market.get("plugins", [])
        if len(entries) != 1 or entries[0].get("name") != plugin.get("name"):
            errors.append("marketplace must contain the root plugin with the same name")
        for entry in entries:
            if entry.get("source") != "./":
                errors.append("marketplace plugin source must be ./")
        for manifest in [plugin, *entries]:
            if "version" in manifest:
                errors.append("omit plugin versions to track Git revisions")
            if "skills" in manifest:
                errors.append("use automatic skills/ discovery instead of explicit skill lists")
        if codex.get("name") != plugin.get("name"):
            errors.append("Codex and Claude plugin names must match")
        if codex.get("skills") != "./skills/":
            errors.append("Codex skills must reference the shared ./skills/ directory")
        if "version" in codex:
            errors.append("omit Codex plugin versions to track Git revisions")
    except (OSError, ValueError, TypeError, AttributeError) as error:
        errors.append(f"invalid plugin manifests: {error}")

    skills = root / "skills"
    if not skills.is_dir() or skills.is_symlink():
        return errors + ["skills/ must be a real directory"]
    for skill in sorted(skills.iterdir()):
        if skill.name == ".gitkeep":
            continue
        label = skill.relative_to(root)
        if skill.is_symlink() or not skill.is_dir():
            errors.append(f"{label}: expected a real skill directory")
            continue
        if not (skill / "SKILL.md").is_file():
            errors.append(f"{label}: missing SKILL.md")
        line_count = 0
        for path in sorted(skill.rglob("*")):
            label = path.relative_to(root)
            if path.is_symlink():
                errors.append(f"{label}: bundle real files and directories; installers may skip symlinks")
                continue
            try:
                path.resolve(strict=True)
            except (OSError, RuntimeError) as error:
                errors.append(f"{label}: unresolved path: {error}")
                continue
            if not path.is_file():
                continue
            data = path.read_bytes()
            if b"\0" in data:
                continue
            try:
                text = data.decode("utf-8")
            except UnicodeDecodeError:
                continue
            line_count += len(text.splitlines())
            if path.suffix != ".md":
                continue
            if "<!-- scaffold:" in text:
                errors.append(f"{label}: replace unfinished scaffold comments")
            for match in LINK.finditer(FENCE.sub("", text)):
                target = urlsplit(match.group(1).strip("<>"))
                if target.scheme or target.netloc or not target.path:
                    continue
                destination = (path.parent / unquote(target.path)).resolve()
                if not destination.is_relative_to(skill.resolve()):
                    errors.append(f"{label}: link escapes its skill folder: {target.path}")
                elif not destination.exists():
                    errors.append(f"{label}: broken local link: {target.path}")
        line_limit = SKILL_LINE_LIMITS.get(skill.name, MAX_SKILL_LINES)
        if line_count > line_limit:
            errors.append(f"{skill.relative_to(root)}: {line_count} text lines exceeds the {line_limit}-line limit")

    for directory, children, files in os.walk(root):
        children[:] = [name for name in children if name not in {".git", ".venv", "node_modules"}]
        if "SKILL.md" in files and Path(directory).parent != skills:
            errors.append(f"{Path(directory).relative_to(root)}/SKILL.md: skills must live directly under skills/")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packaging-only", action="store_true", help="skip external CLI validators")
    args = parser.parse_args()
    errors = packaging_errors(ROOT)
    if errors:
        parser.exit(1, "\n".join(f"error: {error}" for error in errors) + "\n")
    print("Repository packaging passed.", flush=True)
    if args.packaging_only:
        return
    commands = []
    if any((ROOT / "skills").glob("*/SKILL.md")):
        commands.append(["gh", "skill", "publish", "--dry-run"])
    else:
        print("No skills yet; skipping skill format validation.", flush=True)
    commands.append(["claude", "plugin", "validate", "."])
    for command in commands:
        if not shutil.which(command[0]):
            parser.exit(1, f"error: install {command[0]} to run {' '.join(command)}\n")
        result = subprocess.run(command, cwd=ROOT, check=False)
        if result.returncode:
            parser.exit(result.returncode, f"error: {' '.join(command)} failed\n")


if __name__ == "__main__":
    main()

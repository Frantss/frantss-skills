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

from sync_bdd_references import reference_errors


ROOT = Path(__file__).resolve().parents[1]
MAX_SKILL_LINES = 75
SKILL_LINE_LIMITS = {
    "atomic-commits": 50,
    "core-communicate": 50,
    "core-update": 50,
    "persistence-records": 100,
    "persistence-obsidian": 350,
}
LINK = re.compile(r'!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:\s+[\'\"][^)\n]*[\'\"])?\s*\)')
FENCE = re.compile(r"^```[^\n]*\n.*?^```\s*$", re.MULTILINE | re.DOTALL)


def plugin_directories(root: Path) -> list[Path]:
    return sorted((root / "plugins").iterdir())


def manifest_errors(root: Path) -> list[str]:
    errors = []
    try:
        market = json.loads((root / ".claude-plugin/marketplace.json").read_text())
        entries = market.get("plugins", [])
        if market.get("name") != "frantss":
            errors.append("marketplace name must remain frantss")
        plugins = plugin_directories(root)
        expected = {path.name: f"./plugins/{path.name}" for path in plugins}
        if len(entries) != len(expected) or {entry.get("name"): entry.get("source") for entry in entries} != expected:
            errors.append("marketplace must list each plugin with the same name and source")
        for agent in ("claude", "codex"):
            if (root / f".{agent}-plugin/plugin.json").exists():
                errors.append("plugin manifests must live under plugins/")
        for entry in entries:
            if "version" in entry:
                errors.append("omit plugin versions to track Git revisions")
            if "skills" in entry:
                errors.append("declare skills in plugin manifests instead of marketplace entries")
        for directory in plugins:
            name = directory.name
            for agent in ("claude", "codex"):
                path = directory / f".{agent}-plugin/plugin.json"
                manifest = json.loads(path.read_text())
                if manifest.get("name") != name:
                    errors.append(f"{path.relative_to(root)}: plugin names must match {name}")
                if "version" in manifest:
                    errors.append(f"{path.relative_to(root)}: omit {agent.title()} plugin versions to track Git revisions")
                expected_skills = "./skills/" if agent == "codex" else None
                if manifest.get("skills") != expected_skills:
                    errors.append(f"{path.relative_to(root)}: skills must reference {expected_skills!r}")
    except (OSError, ValueError, TypeError, AttributeError) as error:
        errors.append(f"invalid plugin manifests: {error}")
    return errors


def skill_errors(root: Path) -> list[str]:
    errors = []

    plugins = root / "plugins"
    if not plugins.is_dir() or plugins.is_symlink():
        return ["plugins/ must be a real directory"]
    skill_roots = []
    for plugin in plugin_directories(root):
        skills = plugin / "skills"
        if plugin.is_symlink() or not plugin.is_dir() or skills.is_symlink() or not skills.is_dir():
            errors.append(f"{plugin.relative_to(root)}: expected a real plugin with a skills/ directory")
        else:
            skill_roots.append(skills)
    names = set()
    for skill in sorted(path for skills in skill_roots for path in skills.iterdir()):
        if skill.name == ".gitkeep":
            continue
        label = skill.relative_to(root)
        if skill.is_symlink() or not skill.is_dir():
            errors.append(f"{label}: expected a real skill directory")
            continue
        if skill.name in names:
            errors.append(f"{label}: duplicate skill name across plugins")
        names.add(skill.name)
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
        if "SKILL.md" in files and Path(directory).parent not in skill_roots:
            errors.append(f"{Path(directory).relative_to(root)}/SKILL.md: skills must live under plugins/<plugin>/skills/")
    return errors + reference_errors(root)


def packaging_errors(root: Path) -> list[str]:
    return manifest_errors(root) + skill_errors(root)


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
    if any(ROOT.glob("plugins/*/skills/*/SKILL.md")):
        commands.append(["gh", "skill", "publish", "--dry-run"])
    else:
        print("No skills yet; skipping skill format validation.", flush=True)
    commands.append(["claude", "plugin", "validate", "."])
    commands.extend(["claude", "plugin", "validate", str(path.relative_to(ROOT))]
                    for path in plugin_directories(ROOT))
    for command in commands:
        if not shutil.which(command[0]):
            parser.exit(1, f"error: install {command[0]} to run {' '.join(command)}\n")
        result = subprocess.run(command, cwd=ROOT, check=False)
        if result.returncode:
            parser.exit(result.returncode, f"error: {' '.join(command)} failed\n")


if __name__ == "__main__":
    main()

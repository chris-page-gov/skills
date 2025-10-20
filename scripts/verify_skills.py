#!/usr/bin/env python3
"""Verify SKILL.md files for required YAML frontmatter fields.

Checks each top-level directory (excluding dot dirs and infrastructure) for a SKILL.md.
Ensures frontmatter contains 'name' and 'description'. Reports duplicates and missing fields.
Exit codes:
 0 - All OK
 1 - Issues found
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List, Set

REPO_ROOT = Path(__file__).resolve().parent.parent
REQUIRED_FIELDS = {"name", "description"}
IGNORE_DIRS = {".git", ".devcontainer", "scripts", "node-sandbox"}

FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

def extract_frontmatter(content: str) -> Dict[str, str]:
    match = FRONTMATTER_PATTERN.search(content)
    if not match:
        return {}
    block = match.group(1)
    data: Dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            data[key.strip()] = val.strip()
    return data

def find_skill_files(root: Path) -> List[Path]:
    skills: List[Path] = []
    for child in root.iterdir():
        if not child.is_dir():
            continue
        if child.name in IGNORE_DIRS or child.name.startswith('.'):
            continue
        skill_md = child / "SKILL.md"
        if skill_md.exists():
            skills.append(skill_md)
    return skills

def main() -> int:
    skill_files = find_skill_files(REPO_ROOT)
    duplicates: Dict[str, List[Path]] = {}
    names_seen: Dict[str, Path] = {}
    issues: List[str] = []

    for file_path in skill_files:
        content = file_path.read_text(encoding="utf-8")
        fm = extract_frontmatter(content)
        missing: Set[str] = REQUIRED_FIELDS - set(fm.keys())
        if missing:
            issues.append(f"Missing {missing} in {file_path.relative_to(REPO_ROOT)}")
        name = fm.get("name")
        if name:
            if name in names_seen:
                duplicates.setdefault(name, []).append(file_path)
            else:
                names_seen[name] = file_path

    for dup_name, paths in duplicates.items():
        listed = ", ".join(str(p.relative_to(REPO_ROOT)) for p in paths)
        issues.append(f"Duplicate name '{dup_name}' in: {listed}")

    if issues:
        print("Skill verification FAILED:\n")
        for issue in issues:
            print(f" - {issue}")
        print(f"\nChecked {len(skill_files)} skill files.")
        return 1
    else:
        print(f"All {len(skill_files)} skill files passed verification.")
        return 0

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Lightweight validation without external dependencies.

Validates structure, metadata constraints, and relative markdown links.
Does not test an OpenCodex runtime.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
ALLOWED_DIRS = ("references/", "assets/")


def main():
    text = SKILL.read_text(encoding="utf-8")
    fm = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    assert fm, "SKILL.md must begin with YAML frontmatter"
    name = re.search(r"(?m)^name:\s*([^\r\n]+)$", fm.group(1))
    desc = re.search(r"(?m)^description:\s*([^\r\n]+)$", fm.group(1))
    assert name, "Missing 'name'"
    slug = name.group(1).strip()
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug), "Invalid skill slug"
    assert slug == ROOT.name, "Skill name must match directory"
    assert len(slug) <= 64, "Skill name too long"
    assert desc and 1 <= len(desc.group(1).strip()) <= 1024, "Invalid description"

    paths = re.findall(r"\]\(([^)]+)\)", text)
    n = 0
    for target in paths:
        if target.startswith(ALLOWED_DIRS):
            assert ".." not in Path(target).parts, f"Unsafe relative link: {target}"
            assert (ROOT / target).is_file(), f"Broken local link: {target}"
            n += 1
    assert n >= 5, "Not enough supporting links"
    assert (ROOT / "README.zh-CN.md").is_file(), "Missing install instructions"
    print(f"PASS: skill={slug}, description={len(desc.group(1))} chars, {n} local links verified")


if __name__ == "__main__":
    main()

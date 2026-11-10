#!/usr/bin/env python3
"""Validate the ten-skill package metadata and its local Markdown links."""
import re
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "stephen-curry-ui", "stephen-curry-research", "stephen-curry-brand",
    "stephen-curry-experience", "stephen-curry-design-system",
    "stephen-curry-creative", "stephen-curry-assets-motion",
    "stephen-curry-frontend", "stephen-curry-visual-qa",
    "stephen-curry-evaluation",
}

repo_plugin_package = PACKAGE_ROOT / "plugins" / "stephen-curry-ui" / "skills" / "stephen-curry-ui"
package_candidates = (repo_plugin_package, PACKAGE_ROOT)
SUITE_ROOT = None
skill_dirs = []
for candidate in package_candidates:
    if not (candidate / "SKILL.md").is_file():
        continue
    candidate_suite = candidate.parent
    candidate_skills = sorted(
        path for path in candidate_suite.glob("stephen-curry-*")
        if (path / "SKILL.md").is_file()
    )
    if {path.name for path in candidate_skills} == EXPECTED:
        SUITE_ROOT = candidate_suite
        skill_dirs = candidate_skills
        break
assert SUITE_ROOT is not None, (
    "Complete ten-skill suite not found. Run this from the installed skill directory "
    "or the repository root containing plugins/stephen-curry-ui/skills/"
)
names = {path.name for path in skill_dirs}
assert names == EXPECTED, f"Expected the complete ten-skill suite, found: {sorted(names)}"

checked = 0
for skill_dir in skill_dirs:
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\r?\n(?P<front>.*?)\r?\n---\r?\n", text, re.S)
    assert frontmatter, f"Missing skill frontmatter: {skill_dir}"
    name = re.search(r"(?m)^name:\s*(\S+)\s*$", frontmatter.group("front"))
    description = re.search(r"(?m)^description:\s*(.+)\s*$", frontmatter.group("front"))
    assert name and name.group(1) == skill_dir.name, f"Wrong skill name: {skill_dir}"
    assert description and len(description.group(1)) <= 1024, f"Invalid description: {skill_dir}"

    for doc in skill_dir.rglob("*.md"):
        for link in re.findall(r"\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
            if link.startswith(("https://", "http://", "#", "sandbox:")):
                continue
            target = (doc.parent / link.split("#")[0]).resolve()
            assert SUITE_ROOT == target or SUITE_ROOT in target.parents, f"Unsafe link in {doc}: {link}"
            assert target.is_file(), f"Broken link in {doc.relative_to(skill_dir)}: {link}"
            checked += 1

print(f"PASS: {len(skill_dirs)} skill metadata records and {checked} local Markdown links")

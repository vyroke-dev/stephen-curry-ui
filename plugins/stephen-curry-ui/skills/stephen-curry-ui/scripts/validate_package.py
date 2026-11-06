#!/usr/bin/env python3
"""Self-contained Agent Skills package and links sanity checker."""
import re
from pathlib import Path

root=Path(__file__).resolve().parents[1]
text=(root/'SKILL.md').read_text(encoding='utf-8')
fm=re.match(r'\A---\r?\n(.*?)\r?\n---\r?\n',text,re.S)
assert fm,'Missing skill frontmatter'
name=re.search(r'(?m)^name:\s*(\S+)\s*$',fm.group(1))
description=re.search(r'(?m)^description:\s*(.+)\s*$',fm.group(1))
assert name and name.group(1)==root.name
assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name.group(1))
assert len(name.group(1))<=64
assert description and len(description.group(1)) <=1024

checked=0
for doc in root.rglob('*.md'):
    for link in re.findall(r'\]\(([^)]+)\)',doc.read_text(encoding='utf-8')):
        if link.startswith(('https://','http://','#','sandbox:')):continue
        path=(doc.parent/link.split('#')[0]).resolve()
        assert root in path.parents or root==path, f'Unsafe link {link}'
        assert path.is_file(),f'Broken link in {doc.relative_to(root)}: {link}'
        checked+=1
assert checked>=15
print(f'PASS: {root.name} metadata and {checked} local file links; all package files exist')

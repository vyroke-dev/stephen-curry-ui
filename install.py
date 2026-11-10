#!/usr/bin/env python3
"""Safely install/upgrade the standalone suite without touching Canvas or Codex account config.

Managed Skill folders are backed up before upgrade. Existing unknown destinations
are never overwritten. This installer is intentionally conservative.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
SKILLS = sorted(p for p in (ROOT / '.agents' / 'skills').iterdir() if p.is_dir())
AGENTS = sorted((ROOT / '.codex' / 'agents').glob('*.toml'))


def operations(global_install: bool, base: Path):
    items = []
    for source in SKILLS:
        items.append((source, base / '.agents' / 'skills' / source.name, f'.agents/skills/{source.name}', 'skill'))
    if global_install:
        # Support data is folded into the main Skill at staging time, rather
        # than moved independently over the new Skill dir after installation.
        return items
    for source in AGENTS:
        items.append((source, base / '.codex' / 'agents' / source.name, f'.codex/agents/{source.name}', 'agent'))
    for name in ['contracts', 'tools']:
        items.append((ROOT / name, base / name, name, name))
    return items


def recognized_existing(dest: Path, kind: str, source: Path) -> bool:
    if not dest.exists():
        return True
    if dest.is_symlink():
        return False
    if kind == 'skill':
        marker = dest / 'SKILL.md'
        if not dest.is_dir() or not marker.is_file():
            return False
        try:
            head = marker.read_text(encoding='utf-8')[:600]
        except OSError:
            return False
        return f'name: {source.name}' in head
    if kind == 'agent':
        return dest.is_file() and 'developer_instructions' in dest.read_text(encoding='utf-8')
    if kind == 'contracts':
        return dest.is_dir() and (dest / 'schemas' / 'concept-set.schema.json').is_file()
    if kind == 'tools':
        return dest.is_dir() and (dest / 'scui.py').is_file()
    return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument('--global', dest='global_install', action='store_true')
    g.add_argument('--project', type=Path)
    parser.add_argument('--upgrade', action='store_true', help='Back up and replace recognized older Stephen Curry Skill files')
    args = parser.parse_args()
    if args.global_install:
        base = Path.home()
    else:
        base = args.project.expanduser().resolve()
        if not base.is_dir():
            parser.error('Project directory does not exist')
    ops = operations(args.global_install, base)
    conflicts = []
    for src,dst,label,kind in ops:
        if dst.exists() or dst.is_symlink():
            if not args.upgrade or not recognized_existing(dst,kind,src):
                conflicts.append(str(dst))
    if conflicts:
        print('REFUSED: existing destination is not a recognized upgrade target (no files changed):\n'+ '\n'.join(conflicts),file=sys.stderr)
        return 2

    skill_home = base / '.agents' / 'skills'
    skill_home.mkdir(parents=True, exist_ok=True)
    backup_root = skill_home / '.stephen-curry-ui-backups' / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    # Prevent timestamp collision without relying on a random cleanup policy.
    counter=0
    backup_dir=backup_root
    while backup_dir.exists():
        counter+=1
        backup_dir=Path(str(backup_root)+f'-{counter}')
    stage_root=Path(tempfile.mkdtemp(prefix='.scui-install-stage-', dir=skill_home))
    installed=[]
    backed_up=[]
    try:
        for src,dst,label,kind in ops:
            stage=stage_root/label
            stage.parent.mkdir(parents=True, exist_ok=True)
            if src.is_dir(): shutil.copytree(src,stage)
            else: shutil.copy2(src,stage)
            if args.global_install and kind=='skill' and src.name=='stephen-curry-ui':
                support=stage/'support'
                support.mkdir()
                shutil.copytree(ROOT/'contracts',support/'contracts')
                shutil.copytree(ROOT/'tools',support/'tools')
                shutil.copy2(ROOT/'requirements-contracts.txt', support/'requirements-contracts.txt')
        for src,dst,label,kind in ops:
            if dst.exists():
                backup=backup_dir/label
                backup.parent.mkdir(parents=True,exist_ok=True)
                shutil.move(str(dst),str(backup))
                backed_up.append((backup,dst))
            staged=stage_root/label
            dst.parent.mkdir(parents=True,exist_ok=True)
            shutil.move(str(staged),str(dst))
            installed.append(dst)
    except Exception as exc:
        print(f'INSTALL FAILED: {exc}; attempting rollback',file=sys.stderr)
        for p in reversed(installed):
            if p.is_dir(): shutil.rmtree(p)
            elif p.exists(): p.unlink()
        for backup,dst in reversed(backed_up):
            if backup.exists():
                dst.parent.mkdir(parents=True,exist_ok=True)
                shutil.move(str(backup),str(dst))
        return 1
    finally:
        shutil.rmtree(stage_root,ignore_errors=True)
    print('Stephen Curry UI 4.2 Image-Only standalone suite installed.')
    if backed_up: print('Previous recognized files safely backed up:',backup_dir)
    if args.global_install:
        print('For full project-local jury TOML use --project /path/to/website; not installed globally.')
    print('Refresh Codex, verify Skill discovery and image generation capability before new design work.')
    return 0

if __name__=='__main__': sys.exit(main())

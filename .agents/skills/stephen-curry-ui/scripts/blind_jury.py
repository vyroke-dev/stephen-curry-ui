#!/usr/bin/env python3
"""Create LOCAL evidence-only jury package from an experience_audit.py report.

Does not transmit files or invoke any agent. Input report is treated as untrusted:
only supported images inside the report folder are copied.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import shutil
from pathlib import Path

EXTENSIONS={'.png','.jpg','.jpeg','.webp'}
MAX_SIZE=25_000_000


def safe_image(source, audit_root):
    path=Path(source)
    if not path.is_absolute():path=audit_root/path
    path=path.resolve()
    root=audit_root.resolve()
    if root not in path.parents or path.suffix.lower() not in EXTENSIONS or not path.is_file():
        raise ValueError('Unsafe/unavailable screenshot evidence path')
    if path.stat().st_size>MAX_SIZE:raise ValueError('Evidence image too large')
    return path


def prepare_pack(report_path, output):
    report_path=Path(report_path).resolve()
    source=json.loads(report_path.read_text(encoding='utf-8'))
    if 'captures' not in source or not isinstance(source['captures'],list):
        raise ValueError('Not an experience audit report')
    root=report_path.parent
    output=Path(output).resolve()
    if output==root or root in output.parents:
        raise ValueError('Write blind packet outside source audit directory')
    output.mkdir(parents=True,exist_ok=True)
    output_images=output/'frames';output_images.mkdir(exist_ok=True)
    evidence=[];seq=0
    for record in source['captures']:
        route=record.get('route','<unknown>')
        # Only route identity within the review packet; omit original hostname and directory.
        for photo in record.get('screenshots',[]):
            original=safe_image(photo,root)
            seq+=1
            name=f'frame-{seq:04d}-{hashlib.sha256(original.read_bytes()).hexdigest()[:8]}{original.suffix.lower()}'
            target=output_images/name
            shutil.copyfile(original,target)
            evidence.append({'frame':name,'route':route,'viewport':record.get('viewport'),
                             'auditStatus':record.get('status'),'kind':'screenshot'})
    result={'purpose':'Blind visual-first evaluation. Viewer must not see implementation details or creator intent.',
            'evidence':evidence,
            'limitations':['Still frames alone cannot establish live motion, audio, accessibility or GPU performance',
                           'Image pixels may contain visible client/brand information; handle privately',
                           'This packet does not itself constitute an independent AI jury or certification'],
            'initialCriticQuestions':['Is any middle or ending scene materially weaker than the hero?',
                                      'Is the cross-route identity coherent and distinctive?',
                                      'Does each frame communicate content, hierarchy and quality?',
                                      'Which observations need live motion or real interaction before judgment?']}
    (output/'evidence.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--audit',required=True,help='Path to experience_audit.py report.json')
    p.add_argument('--out',required=True,help='Private destination outside audit folder')
    a=p.parse_args()
    result=prepare_pack(a.audit,a.out)
    print(f"Prepared {len(result['evidence'])} evidence frames in {a.out} (local only; no reviewer executed)")


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Conservative CSS token contract checker for multi-page design systems.

This is NOT a CSS parser: it finds declared custom-property definitions and
compares them to an explicit manifest. A mismatch is a factual token-drift
signal, not a judgment on visual quality. No external dependencies.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

DECLARATION=re.compile(r'(--[a-zA-Z_][\w-]*)\s*:\s*([^;}{]+);?')


def check_contract(contract, css_texts):
    if not isinstance(contract,dict) or not isinstance(contract.get('cssVariables'),dict):
        raise ValueError('Contract requires cssVariables object')
    declared={}
    for filename,text in css_texts.items():
        clean=re.sub(r'/\*.*?\*/','',text,flags=re.S)
        for name,value in DECLARATION.findall(clean):
            # Ignore custom property var() references, but not definitions.
            declared.setdefault(name,[]).append({'file':filename,'value':value.strip().lower()})
    results=[]
    for name,value in sorted(contract['cssVariables'].items()):
        if not re.fullmatch(r'--[a-zA-Z_][\w-]*',name) or not isinstance(value,str) or not value.strip():
            raise ValueError('Invalid CSS variable contract entry')
        actual=declared.get(name,[])
        values={x['value'] for x in actual}
        if not actual:status='MISSING'
        elif value.strip().lower() not in values:status='MISMATCH'
        elif len(values)>1:status='OVERRIDDEN'
        else:status='MATCH'
        results.append({'name':name,'expected':value.strip(),'observed':actual,'status':status})
    return {'results':results,'passed':all(x['status']=='MATCH' for x in results),
            'note':'A token match does not establish color contrast, visual fidelity, full browser CSS resolution or cross-route consistency.'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--contract',required=True,help='JSON with cssVariables mapping')
    p.add_argument('--css',nargs='+',required=True,help='One or more project CSS files (read-only)')
    p.add_argument('--out',help='Write JSON report')
    p.add_argument('--strict',action='store_true',help='Nonzero on non-matching tokens')
    a=p.parse_args()
    contract=json.loads(Path(a.contract).read_text(encoding='utf-8'))
    report=check_contract(contract,{path:Path(path).read_text(encoding='utf-8') for path in a.css})
    print('\n'.join(f"{r['status']:10} {r['name']} expected={r['expected']} observed={[x['value'] for x in r['observed']]}" for r in report['results']))
    if a.out:
        dest=Path(a.out);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(json.dumps(report,indent=2)+'\n')
    return 0 if report['passed'] or not a.strict else 2


if __name__=='__main__':raise SystemExit(main())

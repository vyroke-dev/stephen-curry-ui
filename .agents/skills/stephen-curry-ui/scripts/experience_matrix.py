#!/usr/bin/env python3
"""Map a site experience plan onto available audit evidence without inventing coverage."""
from __future__ import annotations
import argparse
import json
from pathlib import Path


def summarize(plan,audit):
    if not isinstance(plan.get('routes'),list) or not isinstance(plan.get('views'),list):
        raise ValueError('Plan requires routes[] and views[]')
    captured={(x.get('route'),x.get('viewport')):x for x in audit.get('captures',[])}
    result=[]
    for item in plan['routes']:
        path=item.get('path')
        if not path or not isinstance(item.get('scenes'),list):raise ValueError('Every route needs path and scenes[]')
        for view in plan['views']:
            ev=captured.get((path,view))
            if ev is None:status='NOT_CAPTURED'
            elif ev.get('status')!='PASS':status=ev.get('status','BLOCKED')
            else:status='SCREENSHOTS_CAPTURED'
            result.append({'route':path,'view':view,'captureStatus':status,'images':len(ev.get('screenshots',[])) if ev else 0,
                           'actionsCaptured':sum(x.get('status')=='CAPTURED' for x in ev.get('interaction_actions',[])) if ev else 0,
                           'requiredScenes':item['scenes'],'sceneReview':'NEEDS_HUMAN_REVIEW',
                           'interactionStates':item.get('states',[]),'stateCoverage':'UNVERIFIED_UNLESS_ACTION_MANIFEST_MATCHED'})
    return {'rows':result,'note':'A screenshot count is not scene-by-scene coverage. Manual scene/state/video evidence is required.'}


def render(result):
    lines=['# Whole Experience Coverage Matrix','',result['note'],'','| Route | View | Capture | Screenshots | Actions | Scene review |', '|---|---|---|---:|---:|---|']
    for row in result['rows']:
        lines.append(f"| {row['route']} | {row['view']} | {row['captureStatus']} | {row['images']} | {row['actionsCaptured']} | {row['sceneReview']} |")
    lines+=['','## Manual scene/state checklists','']
    for r in result['rows']:
        lines += [f"### {r['route']} · {r['view']}", f"- Scenes: {', '.join(r['requiredScenes']) or '(none)'}",f"- States: {', '.join(r['interactionStates']) or '(none)'}",'- Review transitions, interrupted/return paths, touch/keyboard/reduced-motion and dynamic performance evidence.','']
    return '\n'.join(lines)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--plan',required=True)
    p.add_argument('--audit',required=True)
    p.add_argument('--out',required=True)
    a=p.parse_args()
    plan=json.loads(Path(a.plan).read_text(encoding='utf-8'))
    audit=json.loads(Path(a.audit).read_text(encoding='utf-8'))
    report=summarize(plan,audit)
    out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(render(report),encoding='utf-8')
    out.with_suffix('.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Coverage matrix: {len(report["rows"])} route/viewport rows. Scene/state verification remains manual.')

if __name__=='__main__':main()

#!/usr/bin/env python3
"""Capture real browser motion frames plus local rAF timing diagnostics.

Requires playwright + Chromium. rAF timing is an observational diagnostic on
this machine, not proof of perceived smoothness or real-user INP/CLS/LCP.
"""
from __future__ import annotations
import argparse
import json
import shutil
import statistics
from pathlib import Path


def report_frame_times(delta_ms):
    clean=[float(x) for x in delta_ms if isinstance(x,(int,float)) and 0<float(x)<2000]
    if not clean:return {'samples':0,'p50FrameDeltaMs':None,'p95FrameDeltaMs':None,'over33msFraction':None}
    clean.sort()
    return {'samples':len(clean),'p50FrameDeltaMs':round(statistics.median(clean),2),
            'p95FrameDeltaMs':round(clean[min(len(clean)-1,int(0.95*len(clean)))],2),
            'over33msFraction':round(sum(x>33.3 for x in clean)/len(clean),3)}


def run(args):
    try:from playwright.sync_api import sync_playwright
    except ImportError as e:raise RuntimeError('Missing Playwright. Install playwright and Chromium first') from e
    out=Path(args.out).resolve();out.mkdir(parents=True,exist_ok=True)
    meta={'target':args.url or args.html_file,'mode':'reduce' if args.reduce_motion else 'no-preference','frames':[],
          'limitations':['No reference against real mobile hardware','rAF samples are not official Core Web Vitals or a guarantee of perceptual quality']}
    with sync_playwright() as p:
        exe=shutil.which('chromium') or shutil.which('google-chrome')
        b=p.chromium.launch(headless=True,**({'executable_path':exe} if exe else {}))
        try:
            context=b.new_context(viewport={'width':args.width,'height':args.height},reduced_motion='reduce' if args.reduce_motion else 'no-preference')
            page=context.new_page()
            if args.html_file:
                page.set_content(Path(args.html_file).read_text(encoding='utf-8'),wait_until='load')
                meta['note']='Local inline HTML: relative assets and external network requests may not resolve.'
            else:
                page.goto(args.url,wait_until='domcontentloaded',timeout=30000)
            page.wait_for_timeout(args.settle_ms)
            # Monitor time between callback invocations under this test machine's schedule.
            page.evaluate("""() => {window.__scuiRAF=[];window.__scuiRAFStop=false;let last;function frame(t){if(window.__scuiRAFStop)return;if(last!==undefined)window.__scuiRAF.push(t-last);last=t;requestAnimationFrame(frame)}requestAnimationFrame(frame)}""")
            if args.trigger=='click':
                if not args.selector:raise ValueError('--trigger click requires --selector')
                page.locator(args.selector).first.click(timeout=8000)
            elif args.trigger=='hover':
                if not args.selector:raise ValueError('--trigger hover requires --selector')
                page.locator(args.selector).first.hover(timeout=8000)
            elif args.trigger=='scroll':
                page.mouse.wheel(0,args.scroll_delta)
            # Capture across time: open / middle / completion where applicable.
            intervals=max(2,args.frames)
            for i in range(intervals):
                if i>0:page.wait_for_timeout(max(1,args.duration_ms//(intervals-1)))
                frame=out/f'frame-{i:03d}.png';page.screenshot(path=str(frame),animations='allow')
                meta['frames'].append(str(frame))
            delta=page.evaluate('() => {window.__scuiRAFStop=true;return window.__scuiRAF||[]}')
            meta['rafDiagnostic']=report_frame_times(delta)
            meta['title']=page.title()
            context.close()
        finally:b.close()
    (out/'motion-report.json').write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    return meta


def main():
    p=argparse.ArgumentParser(description=__doc__)
    target=p.add_mutually_exclusive_group(required=True)
    target.add_argument('--url',help='Real accessible site URL')
    target.add_argument('--html-file',help='Standalone local HTML (uses page.set_content; suitable for offline concept tests)')
    p.add_argument('--out',required=True)
    p.add_argument('--trigger',choices=['none','click','hover','scroll'],default='none')
    p.add_argument('--selector')
    p.add_argument('--duration-ms',type=int,default=1800)
    p.add_argument('--frames',type=int,default=5)
    p.add_argument('--scroll-delta',type=int,default=750)
    p.add_argument('--width',type=int,default=1440)
    p.add_argument('--height',type=int,default=900)
    p.add_argument('--settle-ms',type=int,default=150)
    p.add_argument('--reduce-motion',action='store_true')
    a=p.parse_args()
    if not 2<=a.frames<=20 or not 100<=a.duration_ms<=30000 or not 320<=a.width<=4096 or not 320<=a.height<=4096:
        p.error('Invalid capture frame count, duration or viewport')
    m=run(a)
    print(f"Captured {len(m['frames'])} motion frames; rAF diagnostics={m['rafDiagnostic']}")


if __name__=='__main__':main()

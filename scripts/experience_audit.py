#!/usr/bin/env python3
"""Whole-site browser reconnaissance for Stephen Curry UI 2.0.

Uses Playwright and local Chrome/Chromium (or Playwright's installed Chromium).
This is a *coverage aid*, NOT a substitute for manual motion, UX, WCAG or perf review.

Example:
  python scripts/experience_audit.py --url http://localhost:3000 \
    --paths /,/about,/work --views desktop,mobile --out /tmp/scui-qa \
    --interactions examples/interaction-manifest.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse

VIEWPORTS = {
    "desktop": dict(viewport={"width": 1440, "height": 900}, is_mobile=False, has_touch=False),
    "tablet": dict(viewport={"width": 820, "height": 1180}, is_mobile=True, has_touch=True),
    "mobile": dict(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True),
}


def safe_token(x: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]+", "-", x.strip("/") or "home")[:80]


def load_manifest(path: str | None) -> dict[str, list[dict]]:
    if not path:
        return {}
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("routes"), list):
        raise ValueError("Interaction manifest must contain a routes array")
    out = {}
    allowed = {"click", "hover", "press", "hold", "drag", "scroll", "wait"}
    for item in data["routes"]:
        p, acts = item.get("path"), item.get("actions")
        if not isinstance(p, str) or not isinstance(acts, list):
            raise ValueError("Each route needs path and actions list")
        for a in acts:
            if a.get("type") not in allowed:
                raise ValueError("Invalid action type (only declarative gestures allowed)")
        out[p] = acts
    return out


def resolve_url(base: str, route: str) -> str:
    if base.startswith("file:"):
        if route == "/":
            return base
        raise ValueError("file:// URL supports only route '/' ; use a local HTTP server for routing")
    return urljoin(base.rstrip("/") + "/", route.lstrip("/"))


def structural_probe(page):
    return page.evaluate("""() => {
      const all = Array.from(document.querySelectorAll('*'));
      const ids = all.map(el => el.id).filter(Boolean);
      const duplicateIds = [...new Set(ids.filter((id,i) => ids.indexOf(id) !== i))];
      const unlabeledButtons = [...document.querySelectorAll('button')]
        .filter(el => !((el.innerText || '').trim() || el.getAttribute('aria-label') || el.getAttribute('aria-labelledby') || el.title)).length;
      const unlabelledImages = [...document.querySelectorAll('img:not([alt])')].length;
      const nav = performance.getEntriesByType('navigation')[0];
      return {
        title: document.title, h1Count: document.querySelectorAll('h1').length,
        sectionCount: document.querySelectorAll('section').length,
        linkCount: document.querySelectorAll('a[href]').length,
        duplicateIds, unlabeledButtons, imagesMissingAlt: unlabelledImages,
        documentHeight: document.documentElement.scrollHeight,
        viewportHeight: window.innerHeight,
        navDomContentLoadedMs: nav ? Math.round(nav.domContentLoadedEventEnd - nav.startTime) : null,
        note: 'Heuristic signals only; not WCAG, CWV, interaction or performance certification'
      };
    }""")


def exec_action(page, action, output_prefix: Path, index: int):
    kind = action["type"]
    selector = action.get("selector")
    if kind in {"click", "hover", "hold"} and not selector:
        raise ValueError(f"{kind} requires selector")
    if kind == "click":
        page.locator(selector).first.click(timeout=8000)
    elif kind == "hover":
        page.locator(selector).first.hover(timeout=8000)
    elif kind == "press":
        page.keyboard.press(action.get("key", "Escape"))
    elif kind == "hold":
        loc = page.locator(selector).first
        loc.scroll_into_view_if_needed(timeout=8000)
        box = loc.bounding_box()
        if box is None:
            raise ValueError("Hold target has no bounding box")
        page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
        page.mouse.down()
        try:
            page.wait_for_timeout(min(max(int(action.get("ms", 850)), 50), 10000))
        finally:
            page.mouse.up()
    elif kind == "drag":
        p1 = action.get("from")
        p2 = action.get("to")
        if not (isinstance(p1, list) and isinstance(p2, list) and len(p1) == len(p2) == 2):
            raise ValueError("drag requires from/to [x,y] screen coordinates")
        page.mouse.move(float(p1[0]), float(p1[1]))
        page.mouse.down()
        try:
            page.mouse.move(float(p2[0]), float(p2[1]), steps=12)
        finally:
            page.mouse.up()
    elif kind == "scroll":
        page.mouse.wheel(0, int(action.get("delta", 600)))
    elif kind == "wait":
        page.wait_for_timeout(min(max(int(action.get("ms", 500)), 0), 10000))
    page.wait_for_timeout(220)
    snap = output_prefix.parent / f"{output_prefix.name}-action-{index:02d}-{kind}.png"
    page.screenshot(path=str(snap), animations="allow")
    return {"type":kind,"status":"CAPTURED","file":str(snap)}


def audit(args):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise RuntimeError("Install browser driver: python -m pip install playwright") from exc

    output = Path(args.out).resolve()
    output.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(args.interactions)
    routes = [x.strip() for x in args.paths.split(",") if x.strip()]
    views = [x.strip() for x in args.views.split(",") if x.strip()]
    if not routes or not views or any(x not in VIEWPORTS for x in views):
        raise ValueError("Specify valid --paths and --views (desktop,tablet,mobile)")
    results = {"url":args.url, "timestamp":dt.datetime.now(dt.timezone.utc).isoformat(),
               "limitations":["Not a frame-rate/INP/LCP field test", "Not a WCAG compliance scan", "Static captures do not prove live motion quality"],
               "captures":[],"browser":"", "errors":[]}

    with sync_playwright() as p:
        chrome = shutil.which("chromium") or shutil.which("google-chrome")
        launch_kwargs={"headless":True}
        if chrome:
            launch_kwargs["executable_path"] = chrome
        browser = p.chromium.launch(**launch_kwargs)
        results["browser"] = browser.version
        try:
            for view_name in views:
                vp = VIEWPORTS[view_name]
                for route in routes:
                    rec = {"route":route, "viewport":view_name, "status":"PASS", "screenshots":[], "interaction_actions":[], "consoleErrors":[], "pageErrors":[], "failedRequests":[], "structure":{}}
                    ctx = browser.new_context(viewport=vp["viewport"], is_mobile=vp["is_mobile"], has_touch=vp["has_touch"], device_scale_factor=1,
                                              reduced_motion="reduce" if args.reduced_motion else "no-preference")
                    page = ctx.new_page()
                    page.on("console", lambda msg, r=rec: r["consoleErrors"].append(msg.text[:500]) if msg.type == "error" else None)
                    page.on("pageerror", lambda err, r=rec: r["pageErrors"].append(str(err)[:500]))
                    page.on("requestfailed", lambda req, r=rec: r["failedRequests"].append(req.url[:500]))
                    name = safe_token(route) + "-" + view_name
                    prefix=output / name
                    try:
                        page.goto(resolve_url(args.url, route), wait_until="domcontentloaded", timeout=args.timeout_ms)
                        page.wait_for_timeout(args.settle_ms)
                        rec["structure"] = structural_probe(page)
                        first=output/f"{name}-full.png"
                        page.screenshot(path=str(first),full_page=True,timeout=args.timeout_ms, animations="allow")
                        rec["screenshots"].append(str(first))
                        # Deliberately sample the whole scroll journey; wheel also advances virtual scrollers.
                        max_scroll=max(int(rec["structure"].get("documentHeight",0)) - vp["viewport"]["height"], 0)
                        if max_scroll > vp["viewport"]["height"] * 1.1:
                            for fraction in (0.25,0.50,0.75,1.0):
                                page.evaluate("fraction => window.scrollTo(0, Math.floor((document.documentElement.scrollHeight-innerHeight)*fraction))",fraction)
                                page.wait_for_timeout(args.settle_ms)
                                f=output/f"{name}-scroll-{int(fraction*100):03d}.png"
                                page.screenshot(path=str(f),timeout=args.timeout_ms,animations="allow")
                                rec["screenshots"].append(str(f))
                        else:
                            rec["virtualScrollWarning"] = "Native document not significantly scrollable. A virtual-scroll/WebGL experience may need manual gate/gesture testing."
                            for step in range(1,5):
                                page.mouse.wheel(0, int(vp["viewport"]["height"]*.82))
                                page.wait_for_timeout(args.settle_ms)
                                f=output/f"{name}-wheel-{step:02d}.png"
                                page.screenshot(path=str(f),timeout=args.timeout_ms,animations="allow")
                                rec["screenshots"].append(str(f))
                        # Reset to a predictable entry state before declarative action script.
                        if route in manifest:
                            page.goto(resolve_url(args.url,route),wait_until="domcontentloaded",timeout=args.timeout_ms)
                            page.wait_for_timeout(args.settle_ms)
                            for i, act in enumerate(manifest[route],start=1):
                                try:
                                    rec["interaction_actions"].append(exec_action(page,act,prefix,i))
                                except Exception as exc:
                                    rec["interaction_actions"].append({"type":act.get("type"),"status":"FAIL","error":str(exc)[:400]})
                                    rec["status"]="FAIL"
                        if rec["pageErrors"]:
                            rec["status"]="FAIL"
                    except Exception as exc:
                        rec["status"]="BLOCKED"
                        rec["error"] = str(exc)[:600]
                        results["errors"].append({"route":route,"viewport":view_name,"error":rec["error"]})
                    finally:
                        results["captures"].append(rec)
                        ctx.close()
        finally:
            browser.close()
    (output/"report.json").write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding="utf-8")
    md=["# Stephen Curry UI — Experience Audit", "",f"Target: `{results['url']}`  ",f"Timestamp: {results['timestamp']}","", "| Route | View | Status | Captures | JS errors | Actions |", "|---|---|---|---:|---:|---:|"]
    for r in results["captures"]:
        md.append(f"| {r['route']} | {r['viewport']} | {r['status']} | {len(r['screenshots'])} | {len(r['pageErrors'])} | {len(r['interaction_actions'])} |")
    md += ["", "## Limits", "", "Static screenshots do not prove continuous animation timing, accessibility, runtime FPS or field CWV.", "Run manual six-role review and record interactive video/trace, audio controls, reduced-motion and key journeys.", "", "## Detailed evidence", "", "See `report.json`, screenshots and action captures in this folder."]
    (output/"report.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(f"Saved {output/'report.md'} and {output/'report.json'}")
    for r in results["captures"]:
        print(f"  {r['route']:16s} {r['viewport']:8s} {r['status']:8s} {len(r['screenshots'])} captures")
    return 0 if all(x["status"] == "PASS" for x in results["captures"]) else 2


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url",required=True,help="Running preview URL (local staging preferred), or a file:// single page")
    parser.add_argument("--paths",default="/",help="Comma-separated routes, e.g. /,/work,/contact")
    parser.add_argument("--views",default="desktop,mobile",help="desktop,tablet,mobile")
    parser.add_argument("--out",default="./.scui-audit",help="Output folder for actual screen captures and reports")
    parser.add_argument("--interactions",help="JSON declarative action manifest; avoid live irreversible transactions")
    parser.add_argument("--reduced-motion",action="store_true",help="Run captures under prefers-reduced-motion=reduce")
    parser.add_argument("--settle-ms",type=int,default=500,help="Wait after scrolling for scene to settle")
    parser.add_argument("--timeout-ms",type=int,default=20000)
    args=parser.parse_args()
    try:
        return audit(args)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

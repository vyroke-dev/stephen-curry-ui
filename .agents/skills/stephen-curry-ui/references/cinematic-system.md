# Whole-site composition, cinematic language and creative coding

## Experience direction != cinematic styling

Plan the **entire visitor journey**: initial contact, first answer, curiosity, middle chapter depth, information/proof, turning point, concluding CTA/next path, footer/return path. Different goals demand different emotional rhythms. Dashboards require an information-flow story, not forced fullscreen theatrical chapters.

For each route and each major scene, capture:

| Field | Meaning |
|---|---|
| Scene purpose | User thought/action that advances here |
| Emotional beat | Calm → anticipation → reveal → proof → closure, or another deliberate arc |
| Frame composition | Static paused viewport must work without motion |
| Entry/middle/exit | What changes *across time* and at section boundary |
| Continuous thread | Image, shape, typography or spatial object carried between scenes |
| Input | Scroll, hover, click, hold, drag, tap, focus, keyboard, optional audio |
| State machine | start / active / complete / interrupted / reverse, not one uninterruptible timeline |
| Recovery/fallback | touch/no hover, reduced-motion, low-end GPU, no audio, offline asset |
| Technical proof | Minimal working POC and browser evidence |

Write a [Scene & Continuity Map](../templates/scene-map.md). A navigation change or route transition is also a scene connection; evaluate the **whole site**, not just page sections.

## Motion grammar

Choose 2–4 recurring “verbs” (e.g. unfold, reveal, morph, refract) tailored to the brand; not all appear everywhere. Normalize timing, movement, scale, easing/spring, interaction affordance, background transition and audio intent. Contrast meaningful stillness with peaks. Respect `prefers-reduced-motion` without hiding essential content.

## Complex visual effects: selection ladder

1. Semantic CSS/SVG first when the visual can be genuinely matched and remains interactive.
2. Animation library / Web Animations for coordinated movement and interrupted timelines.
3. Canvas/WebGL/R3F/shader/post effects for spatial, multi-element, pixel-transform or GPU workloads that ordinary DOM cannot reasonably accomplish.
4. Pre-rendered video for deterministic filmic storytelling; real user-responsive effects require runtime graphics or DOM, **never** a fake video overlay.
5. Select advanced 3D asset generation (optional Higgsfield) only when content, fidelity and performance justify it.

For effects, document: frame update owner, render loop lifecycle, scene memory, WebGL context count, uniform updates, rAF scheduling, device pixel ratio ceiling, shader warm-up, fallback, context loss/recovery, audio opt-in/mute and licensing. Don't lock to one framework version. Minimize redundant RAF loops and forced layouts.

## Quality gates no screenshot can settle

- Motion frame sequence, temporal consistency, reversibility and gesture interruptions.
- Dynamic FPS/frame-budget evidence on target hardware; synthetic trace data is **not** field CWV or universal performance guarantee.
- Press-and-hold release mid-way, drag reversal, route navigation during active effect, sticky transitions, modal focus and history/back restoration.
- Audio off by default until authorized/gesture where required; provide mute and non-audio alternatives.
- High and low device tiers; do not conceal essential controls when WebGL or video fail.

The [motion evidence tool](../scripts/motion_evidence.py) captures time-separated frames and rAF samples; it is a diagnostic aid, not automated artistic judgment.

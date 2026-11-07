---
name: stephen-curry-ui
description: Use for designing, building, redesigning, and refining exceptionally crafted interactive websites or frontend interfaces. This skill requires evidence-backed reference research, whole-site experience direction, interaction and motion prototypes, cohesive effects, production engineering, and full-journey multi-role browser QA, not just hero-section aesthetics. Model-agnostic across compatible coding agents and text models, with optional image-generation and Higgsfield media tools when available.
---

# Stephen Curry UI 3.1

**One adaptive, high-ambition creative-web skill.** The four user-provided benchmarks (Son Daven, Silencio, Why Zero, Unseen Studio) are a **baseline for experiential ambition, not a set of visual motifs to copy**. Never confuse a gorgeous first viewport with a great website. Art-direct the **whole journey**: concept, structure, transitions, interactions, media, navigation, closing moment, and mobile experience.

**Non-negotiable thesis:** *A website is a directed experience, not a stack of attractive sections.* Every material visual or technical choice must reinforce the audience, content, brand or interaction. Sophistication is the quality of orchestration, not the count of effects.

## Runtime assumptions and honest capability detection

- **Model-agnostic by design:** operate with the **current model** in the available coding-agent runtime (including OpenCodex). Do not assume a default, preferred, or superior text-model family; do not force switching models or require a separate Claude Code agent. Use only capabilities actually exposed by the runtime.
- On activation, detect capabilities rather than model names: inspect the repository, current runtime, browsers, image generation access, media/3D tooling, optional Higgsfield access, and actual subagent support. Do not assume a ChatGPT-connected app is directly accessible inside local OpenCodex.
- An explicitly available image model (such as GPT Image) is useful for original visual assets/concepts; it is **not** a substitute for real DOM, shaders, or interactive implementation. If image generation is unavailable, say so and make browser-native visual prototypes instead.
- Higgsfield is **optional** and only valuable for a specific asset need. It may supply video, cinematic stills, and GLB models **when the current environment actually exposes those tools**; it does not supply live scroll/mouse interaction. Never silently spend credits or generate paid media. See [Media decision rules](references/media-and-higgsfield.md).
- Six professional reviewers are **six checklists/perspectives**, not a promise of six independently running models. Parallelize with actual subagents only if supported; otherwise perform sequential audits and disclose the mode.
- Default discussion/report language: **Chinese**, unless the user requests otherwise. Code and existing project copy follow project conventions.

## Operating doctrine: preserve all 12 foundations

1. **Intelligent Hybrid Autonomy:** execute normal creative/technical decisions; request approval only for costly, irreversible, brand-critical, or meaningfully ambiguous choices unless authority was delegated.
2. **Reference-First Design:** before new design implementation, inspect excellent external **real websites** plus repository/UI context. Log observed evidence and source links. On existing small changes, reuse a recently verified relevant reference brief; if browsing is blocked, mark it and do not fabricate research.
3. **Adaptive Creative Exploration:** explore alternatives proportional to novelty, risk, and uncertainty. Variants must differ in experience architecture, not merely color.
4. **Extreme Visual-First:** high-impact work needs desktop + mobile **art direction and motion/interaction concepts**, not only static mockups; build small browser-native interaction proofs before committing to an expensive effect.
5. **Adaptive Motion Intelligence:** choose movement according to story, audience, affordance, technical cost, and user control.
6. **Multi-Agent Quality Assurance:** six lenses, tangible evidence, independent passes when supported, prioritized fixes, regression verification.
7. **Deep AI Collaboration:** the current OpenCodex text model can plan and code; accessible image/video tools create media. Share written briefs across stages; do not invent conversations between models.
8. **Unlimited Creative Engineering:** any justified framework, library, shader, 3D or audiovisual technique may be used if maintainable and measurable. Preserve an existing repo's correct architecture unless a change is justified.
9. **Adaptive Signature Design:** find a brand-relevant identity *across the experience*; it can be typographic, narrative, spatial, sonic, or interactive. Never force gimmicks into functional UI.
10. **Design Memory & Continuous Learning:** save verified general craft knowledge in real files, protect client/private assets, and never assert autonomous cross-project learning without a writable store and consent.
11. **Maximum Visual Fidelity + Intelligent Adaptation:** faithfully implement approved concepts but adapt impossible mockups for real content, responsive devices, accessibility and interaction.
12. **Adaptive Asset Direction:** use the right source: real licensed photo, available image-generation models, coded graphics, 3D, or optional Higgsfield video. Log provenance; avoid misrepresenting actual products.

## Whole-experience core: four engines

**A. Experience Direction Engine:** design an **experience arc** from entry to exit. Specify the narrative beats, emotional energy, scroll/chapter relationships, transitions between sections, navigation, project/detail routes, interaction states, contact/CTA, footer and exit. A bland middle is a failure even if the hero is extraordinary. Read [Experience Direction](references/experience-direction.md).

**B. Interaction & Effects Choreography:** map gesture → feedback → transition → state → recovery/fallback. Use the proper medium for each effect (CSS, GSAP, Canvas, WebGL/Three.js, spatial audio, video); ensure coordinated timelines and coherent visual grammar across scenes, not unrelated demos. Read [Motion Systems](references/motion-and-effects.md).

**C. Feasibility-First Prototyping:** prove the **hardest signature interaction** in a browser early, test touch/keyboard/reduced-motion, validate implementation and frame timing before polishing every section. Treat desktop/mobile visual concepts and **interactive motion prototypes as complementary**. Read [Prototyping and Engineering](references/prototyping-and-engineering.md).

**D. Whole-Journey Quality Gates:** prove every section, connection, page transition, interactive state and device mode was inspected. Combine an evidence matrix, scripted screenshots/traces, role-separated critique, and bounded fix/retest cycles. Read [Multi-role QA](references/whole-experience-qa.md).

## ADDED in 3.0: specialized proven creative-work disciplines

This skill incorporates **original implementations** of useful ideas from expert design systems, while preserving context-specific choice. See [External Skill Research](references/external-skill-findings.md) for sources and licensing boundaries. Other Skill packages are **not dependencies**.

- **Evidence & reverse-engineering:** audit actual websites across their entire scroll, including continuous cross-fold compositions, route boundaries, interaction states, and mobile experience. [Creative Exploration](references/creative-exploration.md).
- **Real visual direction competition:** flagship work compares 2–3 distinct whole-experience concepts. Build an accessible, self-contained local **Creative Direction Explorer** with `scripts/style_explorer.py`; don't mistake it for final interaction feasibility or a coded site.
- **Director's screenplay:** assign a purpose to **every scene** and map emotional arc, entry/middle/exit, pinned visual threads and cross-route transitions using the [Scene Map](templates/scene-map.md). See [Cinematic System](references/cinematic-system.md).
- **Living design contract:** maintain `DESIGN.md` for visual, responsive, motion, FX and route rules; use `scripts/design_guard.py` as a **limited factual CSS-token check**, not aesthetic approval. See [Design Governance](references/design-governance.md).
- **Specialized effects repertoire:** use CSS, GSAP, native animation, R3F/Three.js, GLSL, particles, WebGL, audio or video only when the desired interaction actually merits them; no forced spring/glass/3D aesthetics. Prove a complex effect in a browser first. [Cinematic System](references/cinematic-system.md).
- **Timed evidence instead of hero screenshot theater:** use `scripts/motion_evidence.py` to capture frames and limited rAF diagnostics, `scripts/visual_metrics.py` for descriptive color/pixel differences, and `scripts/experience_matrix.py` for coverage tracking. None alone certifies craft or performance.
- **Blind independent jury:** when agent isolation is supported, give a reviewer only rendered evidence, not the original creative brief, to check the whole result. `scripts/blind_jury.py` prepares a private **local** packet. If no independent agent exists, run sequential role reviews without claiming true independence. See [Independent Jury](references/independent-jury.md).
- **Up-to-date interface baseline:** use the actual [Vercel Web Interface Guidelines](references/interface-guidelines.md) when reachable, and explicitly mark blocked or stale rule retrieval; these are usability standards, not a design style.
- **Selective multi-route rollout:** validate a representative home + interior/detail route and shared system, then scale to remaining pages with route-specific QA. Never let page one monopolize the polish budget.

### Suggested local commands (optional tools, not automatic prerequisites)

```bash
python scripts/style_explorer.py --input templates/directions.example.json --out /tmp/directions.html
python scripts/experience_audit.py --url http://localhost:3000 --paths /,/work --views desktop,mobile --out /tmp/scui-audit
python scripts/experience_matrix.py --plan templates/experience-plan.example.json --audit /tmp/scui-audit/report.json --out /tmp/scui-coverage.md
python scripts/motion_evidence.py --url http://localhost:3000 --trigger scroll --out /tmp/scui-motion
python scripts/visual_metrics.py /tmp/scui-audit/home-desktop-full.png --out /tmp/scui-colors.json
python scripts/blind_jury.py --audit /tmp/scui-audit/report.json --out /tmp/scui-jury
```

All `/tmp` paths above are examples; actual preview URLs, routes, and files must exist. Never report success unless commands really executed. Python tools may require Playwright/Chromium and/or Pillow; recognize missing or blocked environments.

## Mandatory staged execution

### Gate 0 — Inspect reality and project assets

Before design/code changes, inspect repo structure, dependencies, current screenshots/design language, running pages, existing routes, tools, asset rights, constraints, and the user's actual goal. Identify the scope: brand experience, commerce, portfolio, SaaS, dashboard, etc. Characterize experience intensity from **purpose**, not fashion. Existing fixed specs and testable user behavior remain hard requirements.

### Gate 1 — Research **before** design

Read [Reference Research](references/reference-research.md) and, when relevant, the [Four Benchmark Studies](references/four-benchmarks.md). Explore a selection of directly relevant real sites in depth: **top, middle, bottom, navigation, detail page, mobile and interactions**, not just screenshots. Record what was *actually seen* versus inferred or secondhand. In `docs/stephen-curry-ui/`, create or update a **Reference Dossier** from [template](templates/reference-dossier.md). If browsing/interactive observation is unavailable, disclose the limitation and source-level, use available validated evidence, and mark unobserved behavior `UNVERIFIED`.

**No concept art, page design or production frontend code until the reference gate is recorded.** A tiny bug fix can reuse a recent relevant dossier rather than repeat external research.

### Gate 2 — Compete authentic directions, direct the full site, lock DESIGN.md

Use [Experience Blueprint](templates/experience-blueprint.md) and [Experience Direction](references/experience-direction.md) to define:

- A one-sentence creative thesis and core identity/motif.
- Complete **route × chapter / section** map: entry/prelude, introduction, escalation, turn, peak, payoff/CTA, ending/return, plus navigation, detail and all user states. Adapt the sequence to the project rather than forcing theatrical drama on a dashboard.
- **Pacing map:** stillness/contrast, editorial rhythm, animation intensity, spatial/depth changes, meaningful interaction frequency, transitions and recovery.
- **Interaction contract:** each unique gesture and feedback cycle; keyboard/touch equivalents; audio on/off; reduced-motion and low-end alternatives.
- **Media/technical plan:** source and delivery constraints, performance budget and correctness risks.

For important/high-ambiguity projects, compare 2–3 **substantially distinct full-experience directions** (composition, flow, transition grammar, media strategy, signature interactions, mobile plan); use the visual Explorer where useful. Use smart approval. For routine work, proceed with one appropriate direction and document why. Record the selected system in a project-local [DESIGN.md](templates/DESIGN.template.md).

### Gate 3 — Design **in time**, not only in pixels; prove difficult effects

For flagship/new site work: create desktop/mobile visual direction **and** at least one playable browser prototype for the riskiest interaction, key transition or effect. Create a short frame-by-frame storyboard / timeline plus an interactive state diagram. A GPT Image mockup has no proof of how motion feels. Never sign off a spectacular mockup without verifying feasibility. See [Prototyping and Engineering](references/prototyping-and-engineering.md).

- Concept art and media generation are optional *tools*, not automatic steps. Use the [Asset Manifest](templates/asset-manifest.md).
- Pre-rendered Higgsfield clips can elevate atmosphere, but must not masquerade as real input-responsive effects.
- Do not build the entire project around an unverified shader, scroll hijack or video that won't work on mobile.

### Gate 4 — Implement scene by scene, then propagate the design system across routes

Make the approved creative system real: semantic markup, real data, typography, media, responsive layout, animation timelines, scene state, navigation, route transitions, actionable controls, fallback modes, cleanup and performance instrumentation. Read [Motion Systems](references/motion-and-effects.md), [Prototyping](references/prototyping-and-engineering.md), and [Delivery Standards](references/delivery-standards.md).

Implement **and test** each chapter's opening, middle, transition-out, and relation to the next. Maintain an explicit shared state/progress architecture *only where needed*. Never copy an exotic virtual-scroll technique just because an award site used it; for accessible applications prefer native scroll and enhance it.

### Gate 5 — Full-site audit, blind artistic critique, evidence and iteration

Follow [Whole-Experience QA](references/whole-experience-qa.md) and [QA Matrix](templates/qa-matrix.md). Run real browser checks when possible, using included `scripts/experience_audit.py` for initial all-page captures plus manual scripted interactions and traces. **Capture opening, middle, ending, route changes and all material gesture states across desktop/mobile.** Do not claim a page was fully examined after checking the first fold.

Audit through six expert lenses: Art Director, Motion Director, Creative Technologist, UX Auditor, Performance Engineer, Engineering Reviewer. Where supported, perform a fresh [Blind Jury](references/independent-jury.md) visual review without showing the creator’s rationale. Use [Interface Guidelines](references/interface-guidelines.md) for the code-level baseline. Each finding needs evidence, severity, reproduction steps and fix. Resolve P0/P1 and highest-impact P2, retest impacted states, compare actual media/animation to the plan, and log unresolved evidence gaps. If a tool isn't accessible, label the check `BLOCKED`, not `PASS`.

### Gate 6 — Curate verified lessons and deliver

Deliver completed code/artifacts with links or actual files, a **whole-experience walkthrough** of what was built, source/asset credits, before/after evidence when useful, 6-role QA statuses, tests executed and limitations. Curate reusable lessons **only when verified**, with user consent for shared storage; never reuse private customer materials. See [Knowledge and Privacy](references/knowledge-and-privacy.md).

## Definition of exceptional completion

- **Whole-journey cohesion:** every chapter/route has a purpose; sections connect; interaction behavior is unified; the ending is designed, not abandoned.
- **Visual craft:** consistent type, spacing, grid, imagery, contrast, detail; no filler or generic template sections.
- **Motion craft:** no disconnected entrance presets; signature effects have intention, continuity, responsiveness, recovery and graceful fallbacks.
- **Functional and accessible:** real controls, clear affordances, touch/keyboard alternatives, legible content and reduced-motion behavior.
- **Measured engineering:** no critical runtime errors, functional regressions, or known release-blocking defects; performance observations are recorded under actual test conditions.
- **Evidence:** complete audit matrix, actual captures beyond the hero, and a truthful report of what is still unverified.

**Do not promise perfection or award wins.** Aim beyond the benchmarks, but judge delivery using real observation, business fit, credible comparisons and repairable evidence. The skill is complete only when the **site experience** is validated, not when `SKILL.md` sounds impressive.

## Reference index (load progressively, only what the task requires)

- [Four Benchmark Studies](references/four-benchmarks.md)
- [Reference Research](references/reference-research.md)
- [Experience Direction](references/experience-direction.md)
- [Motion & Effects](references/motion-and-effects.md)
- [Prototyping & Engineering](references/prototyping-and-engineering.md)
- [Media / Higgsfield](references/media-and-higgsfield.md)
- [Whole-Experience QA](references/whole-experience-qa.md)
- [Delivery Standards](references/delivery-standards.md)
- [Knowledge and Privacy](references/knowledge-and-privacy.md)
- [External Skill Research](references/external-skill-findings.md)
- [Creative Exploration](references/creative-exploration.md)
- [Cinematic System](references/cinematic-system.md)
- [Design Governance](references/design-governance.md)
- [Independent Jury](references/independent-jury.md)
- [Interface Guidelines](references/interface-guidelines.md)

**Working templates:** [Living DESIGN.md](templates/DESIGN.template.md), [Scene Map](templates/scene-map.md), [Creative Directions JSON](templates/directions.example.json), [Reference Dossier](templates/reference-dossier.md), [Experience Blueprint](templates/experience-blueprint.md), [Interaction Contract](templates/interaction-contract.md), [Asset Manifest](templates/asset-manifest.md), [QA Matrix](templates/qa-matrix.md), [Handoff](templates/handoff.md).

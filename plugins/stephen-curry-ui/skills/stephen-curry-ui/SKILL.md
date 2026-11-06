---
name: stephen-curry-ui
description: Use for designing, building, redesigning, and refining exceptionally crafted interactive websites or frontend interfaces. This skill requires evidence-backed reference research, whole-site experience direction, interaction and motion prototypes, cohesive effects, production engineering, and full-journey multi-role browser QA, not just hero-section aesthetics. Optimized for OpenCodex with Claude Opus 5.5 as the usual active text model, compatible with GPT text models and optional GPT Image / Higgsfield media tools.
---

# Stephen Curry UI 2.0

**One adaptive, high-ambition creative-web skill.** The four user-provided benchmarks (Son Daven, Silencio, Why Zero, Unseen Studio) are a **baseline for experiential ambition, not a set of visual motifs to copy**. Never confuse a gorgeous first viewport with a great website. Art-direct the **whole journey**: concept, structure, transitions, interactions, media, navigation, closing moment, and mobile experience.

**Non-negotiable thesis:** *A website is a directed experience, not a stack of attractive sections.* Every material visual or technical choice must reinforce the audience, content, brand or interaction. Sophistication is the quality of orchestration, not the count of effects.

## Runtime assumptions and honest capability detection

- Operate inside the user's **OpenCodex** environment. **Claude Opus 5.5** is usually the active coding/creative text model; GPT text models may be selected instead. Use the **current model**. Do **not** invent a separate Claude Code agent or require text-model switching.
- On activation, inspect the repository, current runtime, browsers, image generation access, media/3D tooling, optional Higgsfield access, and actual subagent support. Do not assume a ChatGPT-connected app is directly accessible inside local OpenCodex.
- GPT Image 2.5 (or another explicitly available image model) is useful for original visual assets/concepts; it is **not** a substitute for real DOM, shaders, or interactive implementation. If image generation is unavailable, say so and make browser-native visual prototypes instead.
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
12. **Adaptive Asset Direction:** use the right source: real licensed photo, GPT Image, coded graphics, 3D, or optional Higgsfield video. Log provenance; avoid misrepresenting actual products.

## NEW in 2.0: Four whole-experience engines

**A. Experience Direction Engine:** design an **experience arc** from entry to exit. Specify the narrative beats, emotional energy, scroll/chapter relationships, transitions between sections, navigation, project/detail routes, interaction states, contact/CTA, footer and exit. A bland middle is a failure even if the hero is extraordinary. Read [Experience Direction](references/experience-direction.md).

**B. Interaction & Effects Choreography:** map gesture → feedback → transition → state → recovery/fallback. Use the proper medium for each effect (CSS, GSAP, Canvas, WebGL/Three.js, spatial audio, video); ensure coordinated timelines and coherent visual grammar across scenes, not unrelated demos. Read [Motion Systems](references/motion-and-effects.md).

**C. Feasibility-First Prototyping:** prove the **hardest signature interaction** in a browser early, test touch/keyboard/reduced-motion, validate implementation and frame timing before polishing every section. Treat desktop/mobile visual concepts and **interactive motion prototypes as complementary**. Read [Prototyping and Engineering](references/prototyping-and-engineering.md).

**D. Whole-Journey Quality Gates:** prove every section, connection, page transition, interactive state and device mode was inspected. Combine an evidence matrix, scripted screenshots/traces, role-separated critique, and bounded fix/retest cycles. Read [Multi-role QA](references/whole-experience-qa.md).

## Mandatory staged execution

### Gate 0 — Inspect reality

Before design/code changes, inspect repo structure, dependencies, current screenshots/design language, running pages, existing routes, tools, asset rights, constraints, and the user's actual goal. Identify the scope: brand experience, commerce, portfolio, SaaS, dashboard, etc. Characterize experience intensity from **purpose**, not fashion. Existing fixed specs and testable user behavior remain hard requirements.

### Gate 1 — Research **before** design

Read [Reference Research](references/reference-research.md) and, when relevant, the [Four Benchmark Studies](references/four-benchmarks.md). Explore a selection of directly relevant real sites in depth: **top, middle, bottom, navigation, detail page, mobile and interactions**, not just screenshots. Record what was *actually seen* versus inferred or secondhand. In `docs/stephen-curry-ui/`, create or update a **Reference Dossier** from [template](templates/reference-dossier.md). If browsing/interactive observation is unavailable, disclose the limitation and source-level, use available validated evidence, and mark unobserved behavior `UNVERIFIED`.

**No concept art, page design or production frontend code until the reference gate is recorded.** A tiny bug fix can reuse a recent relevant dossier rather than repeat external research.

### Gate 2 — Write the experience blueprint

Use [Experience Blueprint](templates/experience-blueprint.md) and [Experience Direction](references/experience-direction.md) to define:

- A one-sentence creative thesis and core identity/motif.
- Complete **route × chapter / section** map: entry/prelude, introduction, escalation, turn, peak, payoff/CTA, ending/return, plus navigation, detail and all user states. Adapt the sequence to the project rather than forcing theatrical drama on a dashboard.
- **Pacing map:** stillness/contrast, editorial rhythm, animation intensity, spatial/depth changes, meaningful interaction frequency, transitions and recovery.
- **Interaction contract:** each unique gesture and feedback cycle; keyboard/touch equivalents; audio on/off; reduced-motion and low-end alternatives.
- **Media/technical plan:** source and delivery constraints, performance budget and correctness risks.

For important/high-ambiguity projects, compare 2–3 **substantially distinct full-experience directions** (flow, transition grammar, signature interactions); use smart approval. For routine work, proceed with one appropriate direction and document why.

### Gate 3 — Design **in time**, not only in pixels

For flagship/new site work: create desktop/mobile visual direction **and** at least one playable browser prototype for the riskiest interaction, key transition or effect. Create a short frame-by-frame storyboard / timeline plus an interactive state diagram. A GPT Image mockup has no proof of how motion feels. Never sign off a spectacular mockup without verifying feasibility. See [Prototyping and Engineering](references/prototyping-and-engineering.md).

- Concept art and media generation are optional *tools*, not automatic steps. Use the [Asset Manifest](templates/asset-manifest.md).
- Pre-rendered Higgsfield clips can elevate atmosphere, but must not masquerade as real input-responsive effects.
- Do not build the entire project around an unverified shader, scroll hijack or video that won't work on mobile.

### Gate 4 — Implement scene by scene

Make the approved creative system real: semantic markup, real data, typography, media, responsive layout, animation timelines, scene state, navigation, route transitions, actionable controls, fallback modes, cleanup and performance instrumentation. Read [Motion Systems](references/motion-and-effects.md), [Prototyping](references/prototyping-and-engineering.md), and [Delivery Standards](references/delivery-standards.md).

Implement **and test** each chapter's opening, middle, transition-out, and relation to the next. Maintain an explicit shared state/progress architecture *only where needed*. Never copy an exotic virtual-scroll technique just because an award site used it; for accessible applications prefer native scroll and enhance it.

### Gate 5 — Full-site audit, evidence, iteration

Follow [Whole-Experience QA](references/whole-experience-qa.md) and [QA Matrix](templates/qa-matrix.md). Run real browser checks when possible, using included `scripts/experience_audit.py` for initial all-page captures plus manual scripted interactions and traces. **Capture opening, middle, ending, route changes and all material gesture states across desktop/mobile.** Do not claim a page was fully examined after checking the first fold.

Audit through six expert lenses: Art Director, Motion Director, Creative Technologist, UX Auditor, Performance Engineer, Engineering Reviewer. Each finding needs evidence, severity, reproduction steps and fix. Resolve P0/P1 and highest-impact P2, retest impacted states, compare actual media/animation to the plan, and log unresolved evidence gaps. If a tool isn't accessible, label the check `BLOCKED`, not `PASS`.

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

## Reference index (load progressively)

- [Four Benchmark Studies](references/four-benchmarks.md)
- [Reference Research](references/reference-research.md)
- [Experience Direction](references/experience-direction.md)
- [Motion & Effects](references/motion-and-effects.md)
- [Prototyping & Engineering](references/prototyping-and-engineering.md)
- [Media / Higgsfield](references/media-and-higgsfield.md)
- [Whole-Experience QA](references/whole-experience-qa.md)
- [Delivery Standards](references/delivery-standards.md)
- [Knowledge and Privacy](references/knowledge-and-privacy.md)

**Working templates:** [Reference Dossier](templates/reference-dossier.md), [Experience Blueprint](templates/experience-blueprint.md), [Interaction Contract](templates/interaction-contract.md), [Asset Manifest](templates/asset-manifest.md), [QA Matrix](templates/qa-matrix.md), [Handoff](templates/handoff.md).

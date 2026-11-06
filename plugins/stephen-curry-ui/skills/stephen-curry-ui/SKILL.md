---
name: stephen-curry-ui
description: Use when designing, building, redesigning, or visually refining frontend websites, landing pages, portfolios, stores, SaaS apps, dashboards, or interactive experiences. Applies reference-first creative direction, visual-first concepting, GPT Image assets when available, advanced motion, and evidence-based multi-role QA for premium production results.
---

# Stephen Curry UI

An **adaptive creative director and creative engineering workflow** for exceptional, original frontends. The aesthetic changes with the brand and audience; the craftsmanship does not. The name is an independent project label, not an affiliation or endorsement.

## Operating environment

- Run **inside the current OpenCodex session**. The user's usual primary text model is **Claude Opus 5.5**; **GPT** text models are also valid. Do not invoke or depend on a separate Claude Code application, or assume Codex and Opus are separate workers.
- Use **GPT Image 2.5** through an **available image-generation tool** for concept art and assets where appropriate. Inspect actual tool availability and supported model choices first; never invent a model endpoint or claim an image was generated if the tool is unavailable.
- Six review *roles* do not imply six independent models. Use isolated subagents in parallel only when the current harness actually offers them; otherwise review **sequentially** with distinct checklists, disclosing the loss of independent review.
- Follow the user's language; default to Chinese for explanations. Keep project/code conventions and required web copy as specified.

## The 12 binding principles

1. **Intelligent Hybrid Autonomy:** execute low-risk decisions independently; request **approval** for consequential, ambiguous creative directions or destructive changes. If the user explicitly requests autonomous completion, make and record reasonable creative choices without unnecessary gates.
2. **Reference-First Design:** begin each new design task by inspecting relevant excellent **external work or websites** and existing project context. Save a **Reference Brief** **before concept generation or implementation**. Small changes may reuse a relevant, previously validated brief; log the reuse. If research access is unavailable, record `BLOCKED`, inspect supplied or cached references, and do not pretend research occurred.
3. **Adaptive Creative Exploration:** explore one coherent direction for constrained changes; compare multiple meaningfully different directions for **high-impact** or uncertain work. Do not generate arbitrary variants.
4. **Extreme Visual-First:** for new websites, major redesigns, and other **high-impact** visual work, produce and evaluate **desktop** and **mobile** concepts before production coding. For **small changes**, use an existing design system and verify the rendered result instead of making unnecessary full-page images.
5. **Adaptive Motion Intelligence:** choose animation and effects based on user goals, brand, devices, and content rather than applying the same preset to every project.
6. **Multi-Agent Quality Assurance:** audit design, motion, effects, UX, performance, and engineering as six distinct roles, with reproducible evidence and re-verification.
7. **Deep AI Collaboration:** the active OpenCodex model plans, judges, writes and reviews; available GPT Image tooling supports visual production. Use shared briefs and outputs as handoffs, not imaginary autonomous inter-model conversations.
8. **Unlimited Creative Engineering:** choose technologies freely when justified by design intent, compatibility, maintenance, and real-user performance. Never introduce WebGL or dependencies solely for show.
9. **Adaptive Signature Design:** consider a memorable signature element, but express it through typography, composition, interaction, content, or effects according to the project. Never force spectacle into utilitarian software.
10. **Design Memory & Continuous Learning:** curate **verified** reusable lessons; isolate private project and **client** data. No automatic cross-project learning without a real writable store and appropriate consent.
11. **Maximum Visual Fidelity + Intelligent Adaptation:** compare browser output with approved concepts on multiple viewports; correct unintended differences while preserving semantics, accessibility, real content, and responsiveness.
12. **Adaptive Asset Direction:** art-direct every asset. Prefer authentic, authorized representations for real products and brands; distinguish genuine photography, generated concepts, and code-built UI.

## Mandatory workflow

### 0. Inspect and calibrate

Inspect repository instructions, existing pages/components, design tokens, asset folders, dependencies, scripts, runtime tooling, and user constraints *before edits*. Identify the target audience, primary action, style constraints, content truth, and device priorities. Preserve established project conventions. Apply [project brief](assets/project-brief.template.md) only as much as the task needs.

Decide the work size: `micro` (tight fix), `standard` (page/feature), or `flagship` (new identity/site/ambitious experience). This scales effort, **not** quality.

### 1. Reference gate: STOP before creating

Follow [Research & Creative Strategy](references/research-and-creative.md). Browse or inspect relevant original sources; record URLs, what specifically works, tradeoffs, what not to copy, and access/verification status. Prefer a few strong, relevant references to a long inspiration dump. Save [Reference Brief](assets/reference-brief.template.md) under the project's own documentation area, e.g. `docs/stephen-curry-ui/<project-slug>/reference-brief.md`. Reuse and update it for small changes. If truly offline, say so and use the best available project/user references. **Never fabricate links, awards, permissions, or observed interactions.**

### 2. Direct the design

Synthesize, never trace-copy: define the creative thesis, content hierarchy, typography, grid, palette, imagery, responsive behavior, animation intent, and optional signature element. For standard/flagship work, record meaningful alternatives and the selection rationale. Show references and request approval when the creative uncertainty or business risk is high, unless the user has delegated the decision. Follow [Research & Creative Strategy](references/research-and-creative.md).

### 3. Visual-first + asset production

For major visual work, produce **distinct desktop and mobile visual concepts** (with the image tool if available) and mark them as *nonfunctional concept images*. Define a usable design system and an asset manifest. For motion-intensive pages, specify key interaction states or motion storyboards. Follow [Visual Concepts & Assets](references/visual-first-and-assets.md). When the image tool is **unavailable**, record the limitation and use inspectable layout sketches or runnable lightweight browser concepts; do not claim GPT Image output.

### 4. Engineer the experience

Implement the chosen direction with semantic, real, responsive UI. Honor existing architecture unless a deliberate change is justified. Pick CSS, GSAP, Motion, SVG, Canvas, Three.js, shaders, or native interaction according to the effect's real need. Follow [Motion & Engineering](references/motion-and-engineering.md). Treat keyboard support, reduced motion, responsive imagery, loading/error/empty states, and functional paths as design requirements.

### 5. Evidence-driven critique and repair

Run the site when tools permit; capture actual **desktop**, **tablet** where relevant, and **mobile** states; check interactions and motion over time, not just static screenshots. Compare actual output with concept targets and design references. Run the **six-role** audit in [Quality Gates](references/quality-gates.md). Classify `PASS`, `FAIL`, or `BLOCKED` with evidence; prioritize critical issues and fix root causes. Re-run the affected checks after every repair. Stop when release gates pass or remaining issues are explicit, not because an arbitrary aesthetic score was reached.

### 6. Persist useful learning and hand off

Keep project briefs, reference analysis, asset provenance, QA evidence, and decisions local to the project. Optionally promote **anonymized, verified, non-client-specific** patterns to a consented shared library according to [Memory & Privacy](references/memory-and-privacy.md). Report what shipped, where to view it, checks actually executed, remaining `BLOCKED` items, and any deviations from approved design. **Do not claim** testing, model invocation, independent audit, browser review, or completed assets without evidence.

## Required handoff shape

For standard/flagship work, return: **result → creative rationale and references → responsive/motion highlights → evidence-based six-role QA summary → unresolved items**. For micro fixes, keep the report proportionate, but retain the reference and verification record.

## Supporting material

- [Research & Creative Strategy](references/research-and-creative.md)
- [Visual Concepts & Assets](references/visual-first-and-assets.md)
- [Motion & Engineering](references/motion-and-engineering.md)
- [Six-role Quality Gates](references/quality-gates.md)
- [Memory & Privacy](references/memory-and-privacy.md)
- [Project Brief](assets/project-brief.template.md)
- [Reference Brief](assets/reference-brief.template.md)
- [QA Report](assets/qa-report.template.md)
- [Learning Entry](assets/learning-entry.template.md)

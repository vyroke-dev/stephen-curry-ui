---
name: stephen-curry-ui
description: Orchestrate original, research-led, production-grade website and frontend design with strict project-specific Design System approval, three high-fidelity concepts, independent design jury, Codex implementation, browser verification, and clear quality gates. Use for building, redesigning, auditing, or art-directing websites and UI systems.
---

# Stephen Curry UI 4.2 | Image-Only Design Orchestrator

You are the **lead design director and task orchestrator**, not a substitute for verified tools or independent agents. Preserve the exceptional whole-site visual ambition and audited Python utilities of v3.1. Use the **current Codex coding agent** within the user's **OpenCodex tool environment**; these are different things. Never assume a model/provider, browser, image generator, or future Canvas integration is connected.

## Non-negotiable sequence and gates

1. **Inspect reality.** Read `AGENTS.md`, code, existing DS, assets, current tests and available tools. Preserve correct systems. Write a capability matrix of available/unknown/blocked.
2. **Maximum Depth Research First.** Research brand, target users, competitors, positioning, references, market, UX and technical feasibility. Mark observed vs inferred facts, source/date and unresolved unknowns. Use [research skill](../stephen-curry-research/SKILL.md). Unresearchable brand intent, authority, licensing and high-impact tradeoffs require focused, one-at-a-time **Grilling**; don't ask questions already answered.
3. **Experience architecture.** Define sitemap, critical journeys, navigation, content model and device priorities. Device strategy is project-specific and requires user confirmation after research, not a fixed global choice. [Experience skill](../stephen-curry-experience/SKILL.md).
4. **IMAGE-ONLY Design System FIRST.** Audit existing approved systems and Brand DNA; establish requirements in research notes without creating coded design. Use the actual built-in image-generation tool to create the seven mandatory Design System boards: Brand/Art Direction, Colors, Typography, Layout/Spacing, Component Library, Responsive, and Motion/Interaction. Save authentic generated raster files, prompts, tool output records and versioned references. Visually inspect, independently review, and obtain authorized approval of **the image boards themselves** before designing any pages. **Do not author executable tokens or code components as a substitute for this design phase.** For new designs, a written/token-only DS is NOT completed design. Read [DS](../stephen-curry-design-system/SKILL.md) and [Image-Only protocol](references/image-only-design-pipeline.md).
5. **IMAGE-ONLY high-fidelity website concepts.** Only after approved generated-image DS boards, invoke the verified built-in image-generation tool again to create >=3 meaningfully distinct website UI image concepts. Each includes real generated desktop and mobile designs, and supplementary screens where necessary. These are images, not coded designs. **No HTML/CSS/JSX/React/SVG/Python/canvas drawing or code-rendered screenshots may produce Design System boards, UI concepts, component visuals or design alternatives.** No code design explorer, coded wireframe, coded Figma imitation or visual mockup. If image generation is unavailable, STOP as `IMAGE_GENERATION_BLOCKED` and request a user-visible handoff to a supported image-generation surface; never silently substitute code. See [Image-Only protocol](references/image-only-design-pipeline.md) and [Creative](../stephen-curry-creative/SKILL.md).
6. **Independent jury and evidence arbitration.** Review both the seven actual generated Design System boards and three generated concept sets, prompt/asset records and approval logs, not code-generated mockups. Dispatch **four actual independent agent executions** for `art_director`, `ux_expert`, `design_system_auditor`, `frontend_qa`, with same artifact revision but role-specific concerns. The baseline v3.1 six-lens QA checklist is supplemental, **not** a replacement for four real reviewers. Never fake subagent independence if unsupported. Reviewers may not modify app files. See [Jury protocol](references/v4-jury-protocol.md).
7. **Progressive validation.** Only after genuine image-generated DS boards, approved concept images, independent jury and approval, implement a running prototype of the leading concept; browser A/B the top two only if evidence warrants it. Use original assets/motion tools when available, with art direction, licenses and `prefers-reduced-motion`. [Assets](../stephen-curry-assets-motion/SKILL.md).
8. **Codex implementation.** Start **all coded UI implementation** only after the approved image-generated DS boards and approved generated-image concepts; images are visual specifications, not DOM or runnable applications. Transcribe approved visual decisions into executable tokens/component implementation only at this implementation gate. Reuse existing repo architecture, headless accessible primitives, verified dependencies, approved DS. Build entire experience, not a pretty hero with dead middle/end. [Frontend](../stephen-curry-frontend/SKILL.md).
9. **Browser-native QA and adaptive repair.** Capture entry, middle, closing, routes, mobile and critical interactive states. Test keyboard, touch, motion, layout, console, performance and WCAG 2.2 AA target. Use available original scripts below. A failed/unavailable browser check is **BLOCKED**, not PASS. Repair only with concrete before/after evidence, bounded retries and rollback. [QA](../stephen-curry-visual-qa/SKILL.md).
10. **Release and learn.** Enforce independent blocking gates, contract validation, truthful test provenance and privacy. Curate verified design knowledge without cross-project private data. [Evaluation](../stephen-curry-evaluation/SKILL.md).

## Workflow invariants

- The **approved generated Design System boards** (plus their recorded decisions) and signed-off strategic decisions are authoritative during design; executable tokens are derived later and cannot independently invent a design. All exceptions require versioned change proposals; critical accessibility/security failures cannot be overridden by aesthetic score.
- Four independent specialist agents must review the **same frozen artifact version**. Use actual isolated executions, not four subsections of one model output. If runtime lacks subagents, stop at independent-jury gate and surface it as blocked. Different models are optional.
- **Art Direction has creative autonomy within strategic alignment**: meaningfully original layout, storytelling, microinteractions, cinema/3D where justified; no template bans or forced trends.
- **Hybrid source of truth**: user-approved generated design images and linked decision records in the creative phase, implementation code after release of the code gate. No Canvas dependency: run with ordinary repository files, Codex tools and a browser if available. Historical architecture decision #43 remains undecided and does not affect standalone use. Structured design documents are authoritative during exploration; code is authoritative after implementation.
- **Research evidence ≠ AI original judgment ≠ user-approved decision.** Keep these distinct and attributable.
- **Approval gate**: AI cannot impersonate the user or attest its own strategic approval. When no trusted host approval surface exists, stop and ask for explicit consent.
- **Model routing** based on measured capabilities when available; otherwise current supported model, never invent model availability. Do not silently spend on media generation.
- **Quality evidence** is separate from a score. Objective blockers always prevail. No fabricated benchmark ranking or real-user test.
- **Adaptive fault recovery**: version check → stage changes → run checks → commit or rollback; stop on repeated failure or resource budget.
- Research may be extensive but must have source quality and stopping criteria to prevent endless searching.

## Output records and utilities

Create project evidence in `docs/stephen-curry-ui/` (or an agreed equivalent) with `research.md`, `experience-architecture.md`, `brand-dna.md`, `design-system-boards.json`, `design-system-images/*` (seven generated raster boards plus prompts/records), `concepts.json`, `concept-images/*` (actual generated PNG/JPEG/WebP + prompts + provenance), `jury/*.json`, `design-system.json` (implementation-only executable spec, AFTER visual approval), `quality-report.json`, `approval-log.md`, `version-manifest.json`. Validate against `contracts/schemas/` at the Skill Suite repository root. Repo-local `tools/scui.py` supports offline contract and gate checking; it is **not** a host authorization system.

Preserved v3.1 *non-design-generation* utilities in `scripts/`: `experience_audit.py`, `experience_matrix.py`, `motion_evidence.py`, `visual_metrics.py`, `blind_jury.py`, `design_guard.py`, `validate_package.py`. These are local evidence helpers, not autonomous Agent runners. Check dependencies before calling them.

Follow [whole-experience direction](references/experience-direction.md), [cinematic system](references/cinematic-system.md), [motion & effects](references/motion-and-effects.md), [reference research](references/reference-research.md), [delivery standards](references/delivery-standards.md), [whole-experience QA](references/whole-experience-qa.md), and [project-specific approval gates](references/v4-governance.md). Templates remain in `templates/`.

## Delivery contract

Report **what was built**, files changed, actual tests (commands/results), screenshots/evidence, blocking issues, decisions awaiting human approval, and integration capabilities genuinely verified. Never claim production readiness just because SKILL.md exists. The user prefers Chinese unless they request another language. Project code and visible copy follow the project's conventions.

## Standalone runtime and logged-in Codex usage

- This Skill works directly in a local project. No Canvas application, MCP Canvas server, cloud design workspace or separate API key is required for the Skill itself.
- Use the Codex account and models already available in the installed CLI. Never claim the subscription guarantees specific tools, model access, multiple agents or image generation; detect them first.
- Do not start Codex App Server or build an agent execution sandbox for Skill use. Use the existing authorized Codex session, approval policy and working directory.
- Offline support tools: when installed globally, use `~/.agents/skills/stephen-curry-ui/support/tools/scui.py`; for project installs, use `tools/scui.py` at the project root. Missing optional tooling must be reported, not fabricated.
- If four independent agent executions are unavailable, provide a clearly labeled single-agent preliminary review, and stop before claiming the independent-jury gate passed.

## Image-only visual generation is a hard gate

- Required sequence: Research and architecture → built-in image generation of seven Design System visual boards → genuine DS image approval → built-in image generation of three high-fidelity website concept sets (desktop/mobile) → independent jury and user approval → code implementation and browser QA.
- Discover a real callable image tool in the current host. Codex login, model name, subscription or package metadata do not prove image generation is available.
- If missing, report `IMAGE_GENERATION_BLOCKED`, stop image design, and request explicit handoff to a supported image-generation surface with exported original images and records. Never substitute coded mockups.
- Pure maintenance work which does not create any new visual design may skip visual generation, but must not claim a new design has been created.

## HARD BOUNDARY: ALL VISUAL DESIGN MUST BE IMAGE-GENERATED

- Applies to **every visual design artifact**: Brand DNA art direction, color boards, typography boards, layouts, spacing boards, component visual libraries, responsive treatments, motion/interaction visual references, page concepts, and variants.
- Research prose and requirements are allowed before visual generation, but NOT labeled as a finished visual Design System or finished design.
- **Absolutely no design-by-code:** HTML/CSS/JS/SVG/React/Canvas/Python/CSS art, Figma-like generated markup, code-rendered mockups, and code-based illustrations are forbidden as design production methods even when displayed as images.
- Coding is permitted *only after the user's approval of genuine generated image boards and generated page images*, to implement and verify the chosen design. Capturing browser screenshots for implementation QA is allowed, never as replacement design evidence.
- If no actual built-in image generator is available, stop the visual stage. A handoff to an actual host image generator with exported originals is permitted after notifying the user; do not claim that Codex CLI inherently exposes ChatGPT image-generation.
- Do not generate tokens/components from scratch as *the design*; transcribe reviewed visual decisions into implementation specifications only after the visual gate.
- Board and concept manifests are machine-checkable but cannot alone prove genuine generator provenance or human approval. Preserve tool logs and request trusted user approval.

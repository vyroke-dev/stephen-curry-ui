# Multi-role quality gates

Use **six independent perspectives** for every nontrivial frontend deliverable. If actual subagents exist, pass the same brief, approved concepts, reference notes, build URL and evidence to each role, ideally in parallel. If subagents do not exist, audit **sequentially** in six labeled passes; this is role-based review, not six independent AI agents.

## Six review roles

| Reviewer | Must investigate | Evidence examples |
| --- | --- | --- |
| **Art Director** | Originality, creative thesis, typography, layout rhythm, visual hierarchy, content/asset consistency, desktop/mobile fidelity, signature element relevance | Screenshot comparisons, annotated visual diffs |
| **Motion Director** | Timing, choreography, scroll and hover behavior, transitions, interruptions, accessibility of motion, reduced-motion experience | Screen recording, interaction traces, timed test |
| **Creative Technologist** | Visual effects, shaders, 3D/Canvas/WebGL correctness, layering, context recovery, GPU cost and fallback behavior | Runtime video, error log, fallback capture |
| **UX Auditor** | Usability, IA, navigation, forms, states, keyboard/focus, semantics, WCAG-related checks, touch targets, truthful content | Guided flow test, keyboard run, accessibility report |
| **Performance Engineer** | LCP/INP/CLS, image weight, response/startup costs, scroll smoothness, memory/CPU and device/network variance | Measured performance trace with configuration |
| **Engineering Reviewer** | Real functionality, code quality, maintainability, correctness, typecheck/lint/tests/build, accessibility regressions, security, asset rights and deployment safety | Command output, console log, source review |

Skip only inapplicable subchecks, **not the whole role**. Example: a basic static site has no WebGL, so Creative Technologist checks effect-free fallback and marks 3D-specific items `N/A`.

## Findings protocol

Each finding must have:

`ID | Role | Severity (P0/P1/P2/P3) | Repro steps | Evidence/path | Expected | Actual | Suggested fix | Status (PASS/FAIL/BLOCKED/N/A)`

- `P0`: critical safety/data loss or unusable core app, release-blocking.
- `P1`: broken core user journey, major visual distortion, severe accessibility failure or reproducible catastrophic motion/performance issue, release-blocking.
- `P2`: visible quality defect, noncritical friction, noticeable roughness; fix before flagship handoff if feasible.
- `P3`: polish idea, low impact; prioritize by benefit, not novelty.

`PASS` requires an observed check, not intuition. `BLOCKED` identifies missing tool, credentials, environment or assets. `N/A` explains why a check does not apply. No fabricated Awwwards score or “pixel-perfect” claim without measured evidence.

## Iterative refinement loop

1. Capture first-pass screenshots at representative viewports and actual interaction evidence.
2. Compare against approved concept and reference *principles*; identify unintended divergence versus necessary responsive adaptation.
3. Run six-role review and combine duplicate findings by root cause; **do not blindly execute contradictory reviewer requests**.
4. Fix P0/P1, then highest-impact P2 aesthetic/motion issues; review resource cost for effects. Record changes.
5. Re-run tests, build, rendering and affected interaction traces. If any release-blocker remains, report it instead of declaring completion.
6. Repeat as justified by new evidence, not a fixed quota or an infinite loop. Get creative approval if a fix would change the agreed direction substantially.

## Mandatory minimum to claim a high-quality production build

- Actual viewport screenshots, not generated concept images, covering desktop and mobile.
- Key user flows tested, including keyboard/reduced-motion when relevant.
- Motion reviewed through interactive observation or time-based evidence if motion exists.
- Build/typecheck/test results recorded where the repository offers them.
- Six role reports or a consolidated six-role table with evidence and explicit `BLOCKED` entries.
- No known unresolved P0/P1; outstanding P2/P3 and unmeasured areas stated plainly.

Use [QA report template](../assets/qa-report.template.md) or its equivalent in project files.

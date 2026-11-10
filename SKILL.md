---
name: stephen-curry-ui
description: Orchestrate distinctive, research-led website and frontend work from focused fixes to full experiences. Use for building, redesigning, reviewing, or art-directing websites and UI systems; scale research, concepts, approvals, and QA to the scope.
---

# Stephen Curry UI 4.1 | Master Orchestrator

Act as the design and engineering lead for the requested outcome. Preserve the project's useful systems and the suite's whole-experience craft. Use the current coding agent and tools actually available in the host. Never assume a model, browser, image generator, independent agents, or Canvas integration is connected.

## Choose the smallest workflow that fits

- **Focused change:** inspect the relevant code and design rules, make the requested change, and check the affected behavior. Do not require a research dossier, new Design System, three concepts, or a jury for a label fix or contained defect.
- **Page or feature:** inspect the related journeys, content, design system, and implementation; research only the open decisions; prototype or compare options when that helps resolve meaningful uncertainty; verify the affected routes and states.
- **New site, broad redesign, or high-consequence experience:** use the full workflow below. Preserve the ambition to design the whole journey, including its middle, ending, mobile behavior, and interactions.

Honor an existing approved direction and the user's explicit choices. Ask a focused question only when unresolved information materially changes the outcome, authorization, rights, or cost. Otherwise state a reversible assumption and proceed. Do not create records or ceremony that do not help the work.

## Full-experience workflow

1. **Inspect.** Read applicable `AGENTS.md`, the requested scope, existing code, design system, assets, tests, and available tools. Preserve working systems. For complex work, summarize available, unknown, and blocked capabilities.
2. **Research.** Investigate the brand, users, competitors, references, UX, and technical limits relevant to the brief. Separate observed facts, user-supplied claims, inference, judgment, and open questions; cite sources and access dates. Stop when the evidence is sufficient for decisions. Use the [research skill](../stephen-curry-research/SKILL.md).
3. **Map the experience.** Define the routes, core journeys, content model, navigation, states, and device priorities that matter. Recommend a device strategy from evidence; ask only if the choice is consequential and not already specified. Use the [experience skill](../stephen-curry-experience/SKILL.md).
4. **Set brand and design rules.** Reuse the existing system when sound. For a full track, define project-specific Brand DNA and an executable Design System covering tokens, components, states, responsive behavior, motion, assets, and accessibility. Get explicit user approval of the new or materially revised system before formal page design. A direct user approval can be recorded; metadata alone is not consent. Read [brand](../stephen-curry-brand/SKILL.md) and [Design System](../stephen-curry-design-system/SKILL.md).
5. **Explore concepts when useful.** For a new site or broad redesign without a chosen direction, create at least three materially different high-fidelity concepts, varying composition, narrative, and interaction grammar. Respect the approved system. Do not force concept generation when the user has already selected a direction or asked for a focused change. If visual tooling is unavailable, label the visual deliverable blocked; descriptions are not mockups. Use the [creative skill](../stephen-curry-creative/SKILL.md).
6. **Review independently.** Full-experience work uses four real, separate reviewer executions—`art_director`, `ux_expert`, `design_system_auditor`, and `frontend_qa`—on the same frozen artifact revision. Reviewers do not edit app files. Never simulate independence with four sections from one response. If real independent runs are unavailable, mark that gate blocked and hold dependent decisions or release; use a clearly labeled single-agent review for smaller work. See the [jury protocol](references/v4-jury-protocol.md).
7. **Prototype and make assets.** Prototype the leading direction where interaction or uncertainty warrants it. Compare the top two in a browser only when evidence could change the decision. Use assets and motion intentionally, with provenance, rights, fallbacks, and `prefers-reduced-motion`. Detect media tools at runtime; do not spend credits silently. See [assets and motion](../stephen-curry-assets-motion/SKILL.md).
8. **Implement.** Reuse the repository architecture, accessible primitives, verified dependencies, and approved direction. Complete the relevant journeys and states instead of polishing only the hero. Use the [frontend skill](../stephen-curry-frontend/SKILL.md).
9. **Verify in the browser.** For full experiences, inspect entry, middle, ending, routes, mobile layouts, and critical interaction states. Check keyboard, touch, motion, layout, console, performance, and accessibility to a WCAG 2.2 AA target where applicable. Report unavailable checks as blocked, never passed. Use the available helpers and [visual QA skill](../stephen-curry-visual-qa/SKILL.md).
10. **Close with evidence.** Resolve objective blockers, validate relevant contracts, record test provenance and remaining uncertainty, and keep project-private information out of shared knowledge. Use the [evaluation skill](../stephen-curry-evaluation/SKILL.md) when formal arbitration or release evidence is needed.

## Rules that apply at every scope

- Distinguish research evidence, AI judgment, assumptions, and user-approved decisions.
- Approval records document consent; they do not create authorization. Never infer approval from a filename, status field, or the assistant's own assessment.
- Critical security, privacy, accessibility, and core-journey defects cannot be outweighed by an aesthetic score. Do not invent user research, benchmarks, browser results, or tool access.
- Keep research bounded by decision value. Do not copy protected work or reuse another client's private information.
- Use rollback or a stable checkpoint for risky changes; stop after repeated failure or when additional iteration no longer improves the result.
- No Canvas or separate agent server is required. Do not build an execution sandbox for this skill; use the authorized host session and its existing permissions.

## Project records and offline helpers

For substantial work, place only useful evidence in `docs/stephen-curry-ui/` (or an agreed project location): research, experience architecture, Brand DNA, Design System, concepts, jury reviews, QA, approvals, and version manifest. Small changes can use the existing project notes and diff without creating this full record set.

Schemas are bundled at `support/contracts/schemas/`. The offline checker is `support/tools/scui.py`; preserve the `support/` directory when using it from a project copy. It validates structured data and local gate consistency only—it does not authenticate approvals, run agents, test a browser, or certify design quality. The preserved `scripts/` utilities (`experience_audit.py`, `experience_matrix.py`, `style_explorer.py`, `motion_evidence.py`, `visual_metrics.py`, `blind_jury.py`, `design_guard.py`, `validate_package.py`) gather local evidence; they are not autonomous reviewers. Check each helper's dependencies and limits before use.

Follow [experience direction](references/experience-direction.md), [cinematic system](references/cinematic-system.md), [motion and effects](references/motion-and-effects.md), [reference research](references/reference-research.md), [delivery standards](references/delivery-standards.md), [whole-experience QA](references/whole-experience-qa.md), and [project-specific governance](references/v4-governance.md) when relevant. Templates are in `templates/`.

## Delivery

Report what changed, files, checks actually run, rendered evidence actually seen, material limitations, and any decisions still needing the user. Do not claim production readiness because the skill or a contract exists. Prefer Chinese for communication unless the user requests another language; follow project conventions for code and UI copy.

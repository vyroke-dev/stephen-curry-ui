---
name: stephen-curry-visual-qa
description: Inspect rendered website behavior and visual quality with evidence; use browser checks for the affected states or full journeys according to scope.
---

# Browser-Native Visual QA

1. Confirm the app, relevant routes, legal scope, test accounts, and browser tools actually available. If browser verification cannot run, mark that check blocked; do not invent a screenshot. Continue with other checks that remain possible.
2. For a focused change, inspect its affected route and states. For a whole experience, capture entry, middle, ending, important routes, responsive breakpoints, interactions, and reduced-motion behavior.
3. Review hierarchy, type, imagery, overflow, layout, motion, keyboard/focus/touch, core flows, console errors, and measured performance where relevant. Compare against the user's brief and approved Design System.
4. For a major release or required independent sign-off, give the same frozen evidence pack to four independent jury executions. Otherwise conduct a proportionate review and label it accurately.
5. Record concrete findings with severity, reproduction steps, screenshots/logs, impact, and uncertainty. Fix root causes, check the changed behavior again, and look for regressions.
6. Use manual or assistive-technology plans where automation cannot establish an accessibility claim. Never claim WCAG certification from a partial automated check.

Available helpers include `../stephen-curry-ui/scripts/experience_audit.py`, `experience_matrix.py`, `motion_evidence.py`, `visual_metrics.py`, and `blind_jury.py`. They gather local evidence; they do not run independent AI reviewers. Read `../stephen-curry-ui/references/whole-experience-qa.md` for full-journey review.

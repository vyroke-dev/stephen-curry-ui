---
name: stephen-curry-visual-qa
description: Use to audit browser-rendered website quality over full journeys and multiple devices, find specific evidence-backed defects and validate fixes without inventing browser results.
---

# Browser-Native Visual Intelligence

1. Confirm runnable app, routes, test credentials, legal scope and actual browser tooling. If unavailable, label **BLOCKED**; do not replace with an invented screenshot.
2. Capture entry/middle/end, all material routes, navigation, hover/focus/forms, responsive breakpoints, mobile and relevant reduced-motion states. Compare to approved DS and prototype.
3. Assess: visual hierarchy, typography, assets, overlap/overflow, layout, responsiveness, motion continuity, accessibility, core flows, real console errors, performance evidence.
4. Route the same frozen evidence pack and version to 4 independent Jury Agents. Record severity, steps, actual screenshots/logs and uncertainties.
5. Fix high-impact/root-cause defects using bounded edits, inspect diff, retest changed flows, and compare before/after evidence. Detect regression and roll back safely when needed.
6. Add manual/assistive-technology test plans when automation cannot validate WCAG; no fake compliance certification.

Preserved helpers: `../stephen-curry-ui/scripts/experience_audit.py`, `experience_matrix.py`, `motion_evidence.py`, `visual_metrics.py`, `blind_jury.py`. They collect local evidence; they do not execute independent AI reviewers. Read `../stephen-curry-ui/references/whole-experience-qa.md`.


**Image-only design boundary:** All new visual design artifacts, including Brand/Design System boards and page concept visuals, must come from genuine built-in image generation, never coded drawing, HTML/CSS/SVG/React mockups or code-built screenshots. Code is authorized only to implement already approved generated-image designs. See the main image-only protocol.

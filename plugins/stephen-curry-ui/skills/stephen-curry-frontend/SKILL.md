---
name: stephen-curry-frontend
description: Use for Codex implementation of approved brand-specific, accessible, production-quality frontend pages with measured responsive behavior and maintainable code.
---

# Production-Ready Design Engineering

1. Inspect source and dependencies, reuse correct architecture, audited headless primitives and existing DS. Project-level tech stack is A+B+C: optional validated defaults, user overrides, research-driven selection. Obtain approval for high-impact migration.
2. Start formal coding **only after real high-fidelity generated-image concepts are reviewed and the chosen direction is approved**. Do not use HTML/CSS mockups to replace missing images. Work from approved concepts and tokens. Keep reusable design components brand-specific; avoid vendor-template sameness, over-abstraction and gratuitous effects.
3. Implement **full journey** and real content: navigation, routes, empty/loading/error states, forms, actions, CTA, middle and closing sections, responsive/device-specific patterns.
4. Use semantic HTML, WCAG 2.2 AA target, focus, keyboard, touch, contrast, zoom, reduced-motion and safe interaction primitives.
5. Respect security boundaries, CSP, sanitized inputs, no secrets, SEO essentials and asset budgets.
6. Implement small targeted tests and run build/lint/typing/browser verification where available. Do not call an untested implementation production ready.
7. Agent coding changes use dependency graph; no overlapping file owners in concurrent tasks. Maintain snapshots and scoped diffs for rollback.

Read `../stephen-curry-ui/references/prototyping-and-engineering.md` and `../stephen-curry-ui/references/delivery-standards.md`.


**Image-only design boundary:** All new visual design artifacts, including Brand/Design System boards and page concept visuals, must come from genuine built-in image generation, never coded drawing, HTML/CSS/SVG/React mockups or code-built screenshots. Code is authorized only to implement already approved generated-image designs. See the main image-only protocol.

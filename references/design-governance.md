# Living DESIGN.md and design system governance

**Only after approval of actual image-generated Design System boards and website concepts**, maintain an implementation `DESIGN.md` from [template](../templates/DESIGN.template.md). It is never a substitute for the generated visual designs. It is the committed shared specification for layout, content hierarchy, responsive behavior, motion, asset direction, media licensing, code routes and QA evidence.

## Contract

- Ground each design token in a visual principle and actual page; don't add empty unimplemented tokens.
- Define hierarchy: display, heading, body, caption, label and numeric; specify families, weights, fallbacks, tracking, fluid sizes and line lengths.
- Record color semantics (background, foreground, accent, border, focus, semantic success/error) and readability. A palette is not a design system by itself.
- Define composition/grid decisions at narrow phone, touch tablet and large desktop. Record exceptions for scene-specific layouts.
- Explicitly define **motion tokens** (durations, easing, interaction state, reduced motion) and **effects parameters** (DPR, bloom, shader quality, fallback).
- Maintain an asset provenance ledger with right-to-use status and distinguish actual vs generated branded imagery.
- For multiple routes, build one representative interior/detail page and a homepage chapter before propagating the shared system. Audit consistency **and** route-specific identity.
- Reconcile actual code with DESIGN.md after meaningful creative decisions; refuse silent drift.

## How to check

`python scripts/design_guard.py --contract templates/design-contract.example.json --css path/to/site.css`

This original tool compares declared CSS variables to observed tokens. A PASS establishes **contract alignment for those tokens only**, not visual excellence, responsive layout accuracy, copy correctness or functioning animation. Other QA gates remain mandatory.

## Permanent constraints

Keep client-specific assets and strategy in that client project; portable insights are curated only after verification and consent. Preserve existing project architecture and copy truth. The independent reviewer must receive actual site evidence, *not* this design rationale, during initial blind judging.


**Version 4.2 precedence:** Any legacy suggestion to use code-rendered visuals for creative exploration or Design System design is superseded. All formal design visuals must be created by genuine image generation; coded work is implementation only after visual approvals.

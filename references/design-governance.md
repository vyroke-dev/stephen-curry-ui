# Living design guidance and system governance

For a new or substantially redesigned site, keep a project-local `DESIGN.md` as a shared source for composition, content hierarchy, responsive behavior, motion, asset direction, routes, and QA evidence. For a focused change, follow the existing system and update its documentation only if a lasting rule changes.

## Useful system contracts

- Ground tokens in visual principles and actual screens; do not define empty, unused values.
- Define the typography hierarchy and readable line lengths.
- Give colors semantic roles for backgrounds, text, accents, borders, focus, and status.
- Establish responsive composition for relevant devices and record intentional exceptions.
- Define motion and effect limits, including reduced motion and fallbacks, where used.
- Track asset provenance and rights. Distinguish actual from generated branded imagery.
- For multi-route work, check a representative interior alongside the home route.
- Reconcile implementation with `DESIGN.md` after consequential design decisions.

## Check limits

`python scripts/design_guard.py --contract templates/design-contract.example.json --css path/to/site.css` compares declared CSS variables with observed tokens. A pass establishes alignment for those tokens only. It does not prove visual quality, responsive accuracy, content correctness, or working animation. Run other relevant QA checks for the task.

Keep client-specific assets and strategy in that client project. Share verified portable insight only when rights and consent permit. Blind reviewers should receive rendered evidence, not the creator's rationale during an initial critique.

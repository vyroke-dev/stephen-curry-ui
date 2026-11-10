---
name: stephen-curry-design-system
description: Create, audit, or evolve a project-specific Design System for new or substantial website and UI work; use the existing system for focused changes.
---

# Executable Design System

1. Inspect the current tokens, components, usage, and accessibility behavior. Reuse a sound system instead of rebuilding it.
2. For a new or substantial system, define semantic color and type roles, spacing, layout, component anatomy and states, responsive behavior, motion, assets, and accessibility obligations.
3. Tie tokens to actual screens and the verified stack. Cover focus, contrast, reduced motion, forms, errors, zoom, and touch behavior where applicable.
4. Provide representative component previews and use a drift check only for the facts that tool can measure. Arrange browser review for visual and behavior claims.
5. For a major unapproved system change, get the user's approval before formal page design when the project calls for that checkpoint. Approval can be given in the conversation; a local file cannot manufacture it.
6. Freeze and version consequential systems. Record proposed deviations and their impact; avoid formal change control for a contained fix that follows existing rules.

Read `../stephen-curry-ui/references/design-governance.md`; use `../stephen-curry-ui/scripts/design_guard.py` only for its CSS-token checks.

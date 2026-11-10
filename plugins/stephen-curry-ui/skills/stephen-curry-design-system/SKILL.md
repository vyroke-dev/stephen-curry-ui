---
name: stephen-curry-design-system
description: Create and review image-generated project-specific Design System boards before any coded design or page image generation.
---

# Image-Only Design System (mandatory)

1. Inspect existing approved brand/design assets and technical constraints; research may be prose, **not code-based design**.
2. Discover a genuinely callable built-in image-generation tool; Codex login does not guarantee tool access. If unavailable, stop with `IMAGE_GENERATION_BLOCKED`, prepare prompts for an explicit image-generation handoff and wait for user-exported genuine images.
3. Generate **seven visual boards, using the actual image-generation tool**: `brand-art-direction`, `color-system`, `typography`, `layout-spacing`, `component-library`, `responsive`, `motion-interaction`. Each is a generated PNG/JPEG/WebP image. Save prompts and actual generation records alongside. Supplement boards if a single image would be illegible.
4. Compare boards together for consistency: color, type, components, responsive, focus states and readable motion direction. Images are artistic intent, not a guarantee of exact font/color tokens or working interactions.
5. Four independent jury agents review the boards with evidence where supported; otherwise mark independent review blocked. Require meaningful user approval of the **images** before page concept images. Do not treat a machine-readable approval flag as proof of actual consent.
6. Freeze approved board revision and define change controls. Only **after** page concepts are also approved may the implementation team derive executable token JSON, components and frontend rules by faithfully interpreting the images. Verify contrast, keyboard, reduced motion and WCAG 2.2 AA in implementation.
7. Do not generate visual board designs from HTML, CSS, SVG, React, Python, Canvas APIs, or any code. No CSS specimen, coded color palette, generated token sheet, browser screenshot or text-only document substitutes for generated visual boards.

See `../stephen-curry-ui/references/image-only-design-pipeline.md` and `../stephen-curry-ui/references/design-governance.md`.

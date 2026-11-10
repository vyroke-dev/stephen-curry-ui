# Stephen Curry UI 4.2 · Image-Only Design Protocol

## Hard sequence

Research and requirements → image-generated Design System boards → visual board jury and actual approval → image-generated three website concept sets → concept jury and actual approval → **implementation** (derive executable tokens and code) → real browser QA.

There is **no code-produced visual design stage**. No HTML/CSS/SVG/JS/React/Python rendering, browser screenshots of coded mockups, Canvas drawing or code-based visual specimens are valid design artifacts.

## Tool capability and handoff

- Detect the actual built-in image-generation tool exposed by the host; do not infer it from Codex login.
- Call that tool for each design board and concept, export actual raster files and record tool/prompt references.
- If unavailable: `IMAGE_GENERATION_BLOCKED`; stop design and ask the user to use a supported image-generation surface. Import authentic user-exported generated files with records after explicit handoff. Never silently substitute code or another commercial tool.
- Missing provenance means `UNVERIFIED`, not a passing design stage. Local PNG bytes and metadata alone cannot prove a model generated an image.

## Mandatory Design System image boards

Generate all seven board IDs (additional boards are welcome):
1. `brand-art-direction`: brand world, material, light, photo/illustration style, visual DNA
2. `color-system`: brand colors, semantic roles, visual relationships and contrasts
3. `typography`: editorial hierarchy, display/body examples, type personality
4. `layout-spacing`: grids, whitespace, rhythm and composition
5. `component-library`: navigation, buttons, cards, fields, dialogs and variants/states
6. `responsive`: desktop/tablet/mobile interpretations and touch-friendly UX
7. `motion-interaction`: visual storyboards of transitions, focus, hover and reduced-motion alternatives

Generate actual image files for each. Each board must include a prompt record, tool identifier, actual generation record, relevant research/Brand DNA reference and declared limitations. Visual board text can be unreliable; implementation must verify factual claims, fonts, exact colors, accessibility and feasibility.

Store under `docs/stephen-curry-ui/design-system-images/<board-id>/` with `board.png`, `prompt.md`, `generation.json`. Register in `design-system-boards.json` using `contracts/schemas/design-system-boards.schema.json`.

Freeze a version; review actual image pixels, consistency and accessibility targets, use four independent jurors when supported, then obtain real user approval through a trusted interface. A JSON `approved` field is not authorization by itself.

## Mandatory page images

Only after board approval, produce >=3 truly different full-page visual concepts; each includes separate generated desktop and mobile images, representative mid-page and CTA treatment, actual prompt & tool records and image inspection. All follow the same approved board revision. No coded images, diagram exports or text-only concept counts.

## After image approval

Only at the implementation gate may the coding agent derive token JSON, component definitions, responsive CSS, motion code and React pages from the approved images. Browser screenshots, diffs and tests are implementation QA, **not retroactive design generation**. Changes to approved visuals require image regeneration or explicit approval.

## Gate checks and their limits

- `python3 tools/scui.py check-design-boards --file ... --ds-version ... --evidence-root ...`
- `python3 tools/scui.py check-concepts --file ... --ds-version ... --evidence-root ...`
- `python3 tools/scui.py check-design-gates --boards-file ... --concepts-file ... --ds-version ... --evidence-root ...`

These only verify structure, path containment, raster signatures and record consistency. They cannot prove tool provenance, genuine image content, independent jury executions, or human authorization. Keep those items explicitly pending until separately verified.

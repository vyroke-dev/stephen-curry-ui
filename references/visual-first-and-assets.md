# Visual concepts, imagery and art direction

## When to concept first

- **Mandatory for flagship/high-impact:** new websites, major redesigns, important landing pages, new visual systems, and other work with high visual uncertainty. Produce separate desktop and mobile visual concepts **before production implementation**. Examine at least the hero, a representative interior section, key interaction states, and a realistic mobile navigation/content arrangement.
- **Conditional for standard:** create a focused concept for the visually consequential region; do not generate a full site image when design tokens and component patterns already resolve the work.
- **For micro edits:** inspect the original design and implement directly, then validate a rendered screenshot.
- A concept image is a visual target, **not source code** and **not proof** of usability, typography accuracy, or functioning interactions.

## Asset direction decision

For every visible media slot, decide among:

- **Actual supplied media** for truthful brand/product/person representation, with known rights.
- **GPT Image 2.5** or another available generation tool for original illustrative/conceptual imagery when permitted and appropriate; keep prompts, resulting paths, and disclosure notes in the asset manifest.
- **Code-native artwork** (SVG/CSS/Canvas/WebGL) for responsive geometric or interactive visuals.
- **Licensed stock or real photography** when authenticity is required, with license/provenance logged.
- **Video/3D models** only when meaningful for the audience and technically viable.

Never use synthetic “product photos” that materially misrepresent a purchasable item. Avoid fabricating client logos or testimonial photos. Verify asset URLs and licensing before production use.

## Prompt pattern (for available image generators)

> Create an ORIGINAL [type of image] for [project and audience]. Art direction: [materials, light, palette, composition, mood]. Viewport/aspect: [required]. Content-safe region: [where typography/buttons must remain legible]. Include [critical authentic details only when accurately supplied]. Exclude [unwanted stock tropes]. This is [concept art / production asset], not a finished functional website. Output should coordinate with [existing palette, type and neighboring imagery].

Generate or refine image assets **only when an image tool actually exists**. Prefer controlled iterations of one strong direction over dozens of low-signal options. Inspect for anatomy/object errors, accidental text, seams, poor crops, contrast conflicts and generated watermark-like artifacts.

## Deliverable expectations

1. **Concept pair:** desktop + mobile for flagship work; distinguish intended breakpoints and show readable content hierarchy.
2. **Design system:** type families/weights/scale, color roles/contrast, spacing rhythm, grid rules, radii, image treatment, motion personality, interaction states.
3. **Asset manifest:** original filename/path, purpose, source (supplied/generated/licensed/code), rights/provenance where needed, crop/focal point, export format, sizes and responsive strategy.
4. **Fidelity plan:** what must match; which image artifacts can be reinterpreted to protect accessibility, content accuracy and responsive behavior.

## Implementation caveats

- Generated mockups may have impossible kerning, decorative text or inconsistent product detail. Rebuild actual text and controls as accessible DOM/UI, not flattened screenshots.
- Responsive work should recompose for phone readability; a cropped desktop picture is insufficient.
- Optimize AVIF/WebP where appropriate, use `srcset`/`sizes` and lazy loading intelligently; prioritize actual LCP media.
- On image-tool failure, report `BLOCKED` for image generation and proceed with an honest design-system sketch or coded reference mockup if possible.

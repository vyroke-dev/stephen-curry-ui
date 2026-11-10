# Image-first UI concept generation + optional production media direction

## Priority override: mandatory built-in generated UI concepts

For **new UI visual design**, first generate and approve the seven mandatory Design System visual boards using built-in image generation. Only then generate three actual high-fidelity website image concept sets. They are not optional production decoration. Use the locally exposed built-in image-generation tool if available. If unavailable, block concept stage and request an explicit authorized image-generation handoff. **Never replace it with coded HTML/CSS mockups.** This priority overrides any older fallback language below. See `image-only-design-pipeline.md`.

The optional decisions below concern **production media assets (video, 3D, hero photographs)**, not the mandatory image-first concept stage.

## What was actually verified (2026-11-07)

Read-only inspection of the connected **Higgsfield** model catalog showed image models including `gpt_image_2_5` (Flare/Sunburst variants), `gpt_image_2_6`, image-to-video candidates such as `flux_3_video` and `seedance_2_0`, and 3D-to-GLB providers such as `tripo_h3_1_image_to_3d`, `tripo_h3_1_multiview_to_3d`, `hunyuan3d_v3_image_to_3d` and `meshy_v6_text_to_3d`. These are **catalog capabilities**, not proof of the user's local OpenCodex access or result quality. Availability and credit price can change.

Higgsfield can be valuable for:
- **Atmospheric moving assets:** a carefully art-directed cinematic loop behind a passage, editorial scene transition, short campaign film or ambient environmental motion.
- **Shot development:** image-to-video camera movement, material and lighting explorations, alternative frames for a sequence.
- **Stills and concept boards:** coherent image assets when the available model and reference strategy fit the brand.
- **3D starting meshes:** GLB draft objects that can be retopologized, optimized, rigged or re-lit and then rendered interactively via Three.js.
- **Post-production:** upscaling, reframing and editing provided the output is actually reviewed.

**It is NOT the primary tool for:** live scroll-scrubbing geometry, real-time cursor physics, event-dependent responsive motion, accessible menu/navigation, reliable HTML typography, composable app UI or complete web interaction logic. Implement those in OpenCodex with code and a browser.

## Tool selection decision tree

1. Does the visual need to **respond immediately to live user input**, or change with browser state? **Yes → write interactive Canvas/WebGL/DOM code.** Pre-rendered videos are an inferior substitute.
2. Does it need a controlled **cinematic shot** with limited interactivity? **Yes → consider Higgsfield video** if the media quality actually beats lighter code/native-media alternatives.
3. Is it a static concept/hero/editorial image? **Yes → use available GPT Image 2.5 or other capable image generation**, only when generated art is better than licensed/authentic assets.
4. Is an actual branded product, a factual location or a real person being shown? **Use authorized truthful media** unless generated concepts are explicitly labeled and permitted.
5. Does 3D require realtime perspective changes? If generated GLB is used, test mesh scale, topology, materials, and renderability; optimize before shipment.

## Cost, model and consent gate

- Detect Higgsfield availability **in the current runtime**. ChatGPT plugin connection does **not** automatically expose the same app inside local OpenCodex. Use a documented connector, explicit export/import, or a manual asset handoff.
- Before paid generations, inspect model constraints and estimate credits/cost when possible. Request user confirmation for material spending, not for each free text note. **Never consume credits or claim media jobs started without an actual authorized tool call.**
- Keep generated assets in a project manifest with tool/provider/model/date/prompt (where appropriate), source IDs, resolution, usage rights, optimization, review status, and fallback.
- Prefer one carefully iterated asset over bulk speculative generation. Do not make the user buy video credits to get decorative movement that CSS could create better.

## Production delivery requirements

**Video:** inspect quality, temporal consistency, faces/products/logos, beginning/end seam for purported loops, encoding format, file size, color banding, responsive aspect/crops and mobile poster. Add pause/mute where relevant. Use real `video` element or proper compositing with preload control. Respect reduced-motion and audio choice.

**3D:** inspect geometry density/UV/texture resolution, PBR accuracy, GLB loading, mesh compression, texture compression, LOD, lighting, context loss, and low-device fallbacks. Generated GLB is not inherently web-optimized.

**Image:** inspect hallucinated type, content inaccuracies, art-direction drift, crop/focal point, legibility with overlay text, format, LCP strategy and asset license.

**Failure mode:** Higgsfield and production media are optional and may use authorized alternatives. However, missing **built-in Design System board or UI concept image generation** MUST pause the **new visual-design concept stage** and remain BLOCKED until real image artifacts are delivered. Do not switch to code-native mockups to pass the image-first gate. Existing-site maintenance tasks can proceed if no new visual concept is in scope.

Sources: https://higgsfield.ai/ ; https://higgsfield.ai/ai-video-editor


**Version 4.2 precedence:** Any legacy suggestion to use code-rendered visuals for creative exploration or Design System design is superseded. All formal design visuals must be created by genuine image generation; coded work is implementation only after visual approvals.

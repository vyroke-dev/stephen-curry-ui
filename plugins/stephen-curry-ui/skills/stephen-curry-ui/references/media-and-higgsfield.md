# Optional image and media tools

Media tools can produce stills, video, or starting 3D assets when a suitable tool is actually available. Catalogs, model names, pricing, and host integrations change; inspect the current connected tool instead of relying on a list in this document. A ChatGPT plugin connection does not by itself prove that the same tool is available inside another local coding-agent runtime.

Use generated media when it improves the brief over rights-cleared supplied assets or code-native art. Do not assume generated output is factual, correctly branded, licensed, or ready to ship. Real people, products, logos, and locations require truthful authorized media unless a clearly labeled fictional concept is permitted.

## Choose the right medium

1. If a visual must respond immediately to browser state or live input, implement it with HTML, Canvas, WebGL, or DOM code.
2. Consider video for a directed cinematic shot with limited interaction when its quality justifies the weight and fallback work.
3. Consider generated stills for concept or editorial imagery when they fit the brand better than authorized photography or illustration.
4. Treat generated 3D meshes as drafts; inspect and optimize geometry, materials, scale, and runtime behavior before shipping.

## Cost, rights, and review

- Detect current provider availability and constraints. Never claim a job began unless an actual tool call confirms it.
- Do not spend credits or money without the user's authorization. Estimate cost where the provider exposes it.
- Record provider, model, date, prompt when appropriate, source IDs, rights, resolution, optimization, review status, and fallback for shipped assets.
- Iterate deliberately; do not bulk-generate decorative variations without a decision purpose.

## Production checks

For video, inspect temporal consistency, beginning/end seam, codec, file size, crops, poster, pause/mute behavior, preload, and reduced motion.

For 3D, inspect geometry, textures, compression, loading, lighting, context loss, and low-device fallback.

For images, inspect typography artifacts, factual errors, composition, crop, legibility, file format, loading impact, and rights.

If a provider is unavailable or unsuitable, continue with authorized media or code-native alternatives and report the limitation. No media provider is a dependency of this Skill.

# Interaction & Effects Choreography

## One contract per meaningful interactive beat

Use [interaction contract template](../templates/interaction-contract.md) to define:

`trigger → intent → affordance → start → continuous response → completion → recovery/interrupt → navigation/state outcome → mobile + keyboard equivalent → reduced-motion fallback → measured cost`

For example, *hold to reveal* should specify pointer-down and touch behavior, cancel on pointer-up/leave as intended, non-pointer equivalent (button/keyboard), progress ring, scene brightness, sound timing, completion consequence, replay/skip and downstream route state. Merely having an `onMouseDown` handler is not a complete experience.

## Motion layers should have a common director

1. **Editorial micro-motion:** hover, focus, selection, state change, labels, numbers, typography.
2. **Section-level choreography:** entrances/exits, pinned scenes, masks, type transformation, object continuity.
3. **Route transition:** how projects/sections pass objects and context across pages.
4. **World-level motion:** camera, materials, shaders, particles and spatial interaction.
5. **Audio layer (optional):** ambience, feedback, scene cues, silence, consent and mute.

For higher-complexity stories, define a shared **progress and state model** with scene lifecycle: `prepare`, `enter`, `scrub`, `update`, `exit`, `dispose`, `restore`. This pattern is a model, not a mandate to replace native scrolling. Re-entering at any route or scroll position must reconstruct a consistent visual state.

## Choosing implementation technology

| Effect goal | Prefer first | Escalate only if warranted |
| --- | --- | --- |
| UI hover/reveal/state | Native CSS/WAAPI, accessible DOM | GSAP/Motion for complex coordinated timelines |
| Story-driven scroll | Native scroll + GSAP ScrollTrigger | Dedicated progress controller if design demands it and alternative controls exist |
| Fluid page transitions | Router-aware state + simple overlays/view transitions | Shared element or WebGL transitions with context preservation |
| Image distortions/displacement | Pre-rendered media or Canvas when sufficient | WebGL fragment shaders, masked textures, FBO simulation |
| Spatial project explorer | Accessible DOM list + optional canvas layer | Three.js/R3F or raw WebGL with orbit/drag/picking if tested |
| Physically meaningful simulation | CSS/canvas for simple forms | GPU particles/physics when necessary |
| Cinematic atmospheric media | Optimized still or Higgsfield-origin video | Interactive scene only when response to input is essential |
| Soundscape | User-controlled Web Audio / Howler | Spatial/realtime audio only if meaningful |

The user allows full technical freedom, **not unlimited network bytes, GPU time, dependencies or fragility**. Preserve repo conventions. Disable unused render loops and ensure cleanup/unmount works.

## The anti-gimmick standard

The whole site should have **one coherent effect vocabulary**, perhaps with a few deliberate exceptions. More visually elaborate is not automatically more distinctive. Design rhythm requires high-impact moments, quiet moments, and informative moments. Never place a 3D scene in a checkout step simply to “feel premium”.

## Timing and synchronization

- Prefer one clock or progress model for linked scene animation. Pair sound cues with the actual visible frame, not unreliable timers.
- Define input interruption/exit for timelines. Stop animations/observers/audio/render loops when routes unmount.
- Explicitly manage preload, cold shader compilation, texture upload, context loss and renderer disposal when using GPU effects.
- Verify touch drag, overscroll, gesture conflicts, nested scrollers, pointer capture, browser back and mobile address-bar resize.
- Test reduced motion with essential state changes still comprehensible. If a gate requires movement, provide a simple accessible alternate activation.

## Deliverable test

A **motion storyboard** should show at least 3 representative points in every signature sequence: before input, while effect is active, after resolution; for important gates include cancel/reverse state. Supplement still frames with a **playable prototype or recorded browser interaction**, since pictures cannot prove timing.

Sources: https://gsap.com/docs/v3/Plugins/ScrollTrigger/ ; https://tympanus.net/codrops/2026/07/17/zero-the-engineering-behind-a-defiant-interactive-narrative/

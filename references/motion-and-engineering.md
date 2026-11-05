# Adaptive motion and creative engineering

## Select motion by intent

| Type | Appropriate motion | Avoid |
| --- | --- | --- |
| Creative portfolio/agency | Reveal choreography, tactile transitions, selective immersive scenes | Slow intros that block access |
| Luxury commerce | Refined easing, photographic transitions, product detail reveals | Checkout friction and distracting cursors |
| SaaS/dashboard | Fast state feedback, hierarchy changes, understandable data transitions | Scroll hijack and novelty loaders |
| Corporate/service | Trust-building subtle motion and purposeful section reveals | Impressive effects that delay contact actions |
| Entertainment | Immersive audio/visual layers when the audience expects them | Mandatory GPU-heavy effects on low-end devices |

Write a motion intent for major effects: **trigger, state change, duration/easing, user benefit, mobile alternative, reduced-motion behavior, and fallback**. Animation is not proof of quality. Evaluate actual scroll/video playback where tooling allows.

## Technical freedom with engineering discipline

- Respect existing repository architecture and user constraints. For a new project, choose the simplest framework that fits routing, content, interactivity and deployment. React/Next.js, Astro, Vue or plain HTML/CSS are valid; no mandatory stack.
- **CSS transitions** first for simple effects; use GSAP/Motion for orchestrated state/timelines; SVG/Canvas for custom art; Three.js/WebGL/WebGPU/shaders only for genuinely spatial or intensive creative interaction.
- Isolate GPU effects from essential navigation and content. Provide fallback content and lifecycle cleanup. Avoid unnecessary 3D bundles on routes that do not need them.
- Use semantic HTML, accessible controls, real route/form behavior, keyboard and focus management, errors/loading/empty states, and logical heading hierarchy.
- Preserve meaningful design intent at responsive breakpoints, including touch hit areas and readable type. Do not lock layouts to one screenshot size.
- Support `prefers-reduced-motion`, and honor device limitations without reducing essential content or functionality.
- Optimize measured performance rather than guessed micro-optimizations. Useful targets for public pages at the 75th percentile are LCP ≤2.5s, INP ≤200ms, CLS ≤0.1; interpret real data by page context and record test conditions. Do not claim targets met without measurement.
- Audit image weight, long tasks, script hydration cost, animation FPS/frame timing, memory leaks, layout shifts, and fallback behavior.

## Practical verification matrix

- **Responsive:** narrow phone, large phone, tablet if applicable, desktop; capture representative interaction states.
- **Functional:** navigation, keyboard controls, forms, links, state changes, errors, navigation/history, focus.
- **Visual:** hero composition, text wrapping, image focal points, dark/light states, spacing rhythm, crop.
- **Motion:** entering, exiting, scrolling, hover/touch, tab focus, interruption, reduced-motion mode, low-power fallback.
- **Engineering:** test scripts, build, lint/typecheck when available, console/network errors, component cleanup, SEO and metadata for public sites.

Evidence can come from browser automation, recordings, screenshots, traces, or test output. If unavailable, explicitly mark the specific checks `BLOCKED`; a code walkthrough is not equivalent to a real device test.

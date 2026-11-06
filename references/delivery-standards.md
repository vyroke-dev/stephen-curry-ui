# Production, accessibility and verification standards

## Functional truth before launch

- Every CTA, nav item, menu, filter, purchase/sign-up/contact path must resolve to a real destination or obvious explicitly scoped placeholder. Do not claim it functions if it does not.
- Honor existing architecture and project requirements. The creative objective never authorizes breaking validation, data integrity, security, accessibility or correct existing behavior.
- Mark assumptions, missing legal/brand/product facts, permissions and asset provenance. Never generate fabricated testimonials, fake metrics or fictional investor guarantees.
- Handle loading, empty, error, offline (when relevant), disabled and focus states, including route refresh/back navigation and component disposal.

## Accessibility is part of a premium experience

- Target WCAG 2.2 AA in practical review, recognizing formal compliance requires more than automated tests.
- Semantic text/navigation/buttons, heading structure, readable colors/type, keyboard and focus handling, visible focus, sensible touch targets, informative alt text.
- No gesture-only gate without alternate keyboard/tap route; no information available only in WebGL textures or audio; no screenreader-invisible essential content.
- Support `prefers-reduced-motion`; motion should be replaceable without removing functionality. Provide user controls for audio, pause and other continuous attention-grabbing media as applicable. Do not auto-enable sound without user intent.
- Avoid creating content at risk of photosensitive reaction, disorientation or compulsory animation.

Sources: https://www.w3.org/TR/WCAG22/ ; https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion ; https://w3c.github.io/wcag/understanding/pause-stop-hide.html

## Measured performance, not performance theater

- Public web performance baseline targets (75th percentile field measurements): LCP ≤2.5s, INP ≤200ms, CLS ≤0.1, unless project requirements establish stricter goals. Do not compare synthetic lab-only timings to field percentiles.
- Motion runtime: record test device, browser, throttling, viewport, scene, observed frame pacing/long frames. 60fps is a *goal for suitable devices*, not a result to announce without a trace.
- Optimize images/video, LOD and texture atlases, shader warmup, idle GPU uploads, load order and hydration. Keep unnecessary JS/3D off other routes.
- Define adaptive quality tiers and visual fallbacks for WebGL-intensive work. Preserve story and functionality when GPU quality lowers.
- Test interactive performance and memory after multiple route changes; clean listeners, render loops, media streams and textures on unmount.

Sources: https://web.dev/articles/vitals ; https://developer.chrome.com/docs/devtools/performance

## Tool evidence boundaries

- Generated images are not browser screenshots. A storyboard is not a usability test. A desktop Chrome test is not an Android-device result.
- The included audit script collects screenshots, page/runtime errors, basic structural probes and optional scripted actions. It does **not** prove 60fps, WCAG compliance, successful backend behavior or a perfect visual score.
- For a critical animation use a screen recording/trace with timing and actual inputs; for a perf target use genuine traces or appropriate field data; for visual fidelity compare against intended concepts across viewport changes.

# Feasibility-first creative engineering

## Prototype the risky thing early

An award-caliber interactive website can fail at the exact moment its central effect moves from a still mockup to a real browser. Before polishing the full UI, isolate the **most technically uncertain and important interaction** as a small functioning proof of concept (PoC).

1. Define the desired perceptual outcome (e.g., “draw a loop to fracture the world”), not a library preference.
2. Make a smallest valid web demo with the real input type, motion, state changes, and a placeholder asset.
3. Test at a normal desktop size, a narrow phone and a low-power setting or throttled environment when available.
4. Test input interruption, keyboard alternative, touch handling, reduced motion, and deep linking/return.
5. If successful, incorporate its interface and performance footprint into the Experience Blueprint. If failed, redesign the experience while preserving the user-facing thesis.

A coherent storyboard plus a proven interaction is more useful than 10 static full-page design generations. Save actual PoC code/URL, screenshots, a short screen recording where available, and observed tradeoffs.

## Architecture guidance

- For real sites, provide meaningful HTML text/links and a robust content/navigation layer even if WebGL is visually dominant.
- Use native scrolling by default. A custom progress engine needs a strong reason and explicit accessibility, browser history, keyboard and mobile recovery plan.
- A scene-based story may use lifecycle hooks to allocate/cleanup meshes, audio, postprocessing and assets; keep state deterministic and centralize timeline ownership. Avoid several animation libraries competing for the same properties.
- Keep dynamic content states and routes resilient to reload, back/forward, error and slow network.
- Handle shader compilation warmup, compressed texture upload, LOD, memory, render resolution and context restoration. For complex art, prefer asset-specific compression review rather than blurring everything indiscriminately.
- Prefer consistent design behavior across desktop/mobile, though fidelity and effects can adapt. Accessibility is not a disposable alternate website.

## Time budget and quality budget are linked

Every expensive effect must justify its GPU, bandwidth and interaction costs. Set a provisional asset/performance budget based on actual task context and device audience, then **measure** against it. Do not claim a specific total download size or FPS unless collected with tools. Consider adaptive quality tiers for high-end effects; keep content and progression equivalent in low mode.

Useful baseline public-site Core Web Vitals targets, measured at the 75th percentile in field data, are LCP ≤2.5s, INP ≤200ms and CLS ≤0.1. Lab tests and local Chrome measurements are not equivalent to real-world field data. Some experiential sites may need carefully explained tradeoffs, but fundamental usability is never optional.

Sources: https://web.dev/articles/vitals ; https://developer.chrome.com/docs/devtools/performance ; https://tympanus.net/codrops/2026/07/17/zero-the-engineering-behind-a-defiant-interactive-narrative/

# Independent creative jury: review what shipped, not what was intended

## Purpose

Self-congratulation is a failure mode. Separate creative production from critique. For a high-impact or production release, create a **blind evidence packet** with actual rendered screenshots, observed interactions, viewport labels and technical measurements. Withhold internal concepts, source code, reasoning, moodboards, DESIGN.md and the builder's self-evaluation from the first independent artistic pass.

Create with `python scripts/blind_jury.py --audit /path/to/.scui-audit/report.json --out /path/to/.scui-jury` when browser audit evidence exists. It creates a local, de-identified **file-named** packet, not an automatic independent model. The images themselves may show brand/customer data, so keep the packet local/private and enforce access controls. This tool does not send the pack anywhere.

## Roles

- **Art Direction Critic:** whole-site aesthetic clarity, distinctive identity, composition/typography across pages, quality of middle and final scenes, originality, content truth.
- **Motion & Film Critic:** interaction energy, frame-to-frame choreography, transition tone, interruption and scroll continuity, audio choices (where applicable).
- **Creative Technology Critic:** realtime effects quality, performance integration, actual gesture responsiveness, shader/memory and graceful fallback.
- **UX/Accessibility Critic:** task clarity, affordances, keyboard/focus/touch, motion reduced settings, media controls, form feedback.
- **Performance Critic:** measured render/network responsiveness, asset weight, stable frame pacing, device/CPU tiers, mobile degradation.
- **Engineering Critic:** source correctness, builds, tests, JS errors, real content, security, SEO and responsive integrity.

These are **roles**. Use fresh, separate subagents when supported. If not, run isolated sequential passes with separate prompts and call it *sequential role review*, not independent blind agents.

## Judgment protocol

1. Inspect at least **entry, mid-journey, ending, routes, and material states**. A pretty hero cannot redeem an empty middle.
2. Report findings with precise evidence references and reproduction steps, severity, audience impact, fix rationale and confidence.
3. Use directional scores only for internal comparison; do not claim Awwwards jury certification. Separate subjective art judgment from factual WCAG/technical checks.
4. Combine reviewer findings, deduplicate by root cause, prioritize P0/P1 critical defects and consequential P2 defects.
5. Re-run relevant view/interaction/performance tests, preferably by the same reviewer after fixes; have the final critic assess the result without access to the builder's justifications.
6. If only still screenshots were supplied, **block motion and interactivity claims** until footage or actual browser observation exists.

See [Whole Experience QA](whole-experience-qa.md) and [Interface Baseline](interface-guidelines.md).

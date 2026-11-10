---
name: stephen-curry-evaluation
description: Use to evaluate independent Design Jury findings, hard release gates, originality, real UX evidence, reliability and fair comparative design benchmarks.
---

# Evidence-Based Arbitration and Benchmark

1. Require exactly four independently attributable Juror reports for the same frozen artifact and Design System versions. Reject missing or duplicated execution IDs, contradictory version metadata, missing evidence and malformed schema.
2. Resolve objective defects using reproducible evidence; critical accessibility/security/core-flow failures block release regardless of aesthetics. Do not decide by simple voting.
3. Compare subjective art directions using Brand DNA, documented rationale, originality, target user and optional blinded human study; avoid pretending judges are objective ground truth.
4. Measure actual regression and iteration improvements; no infinite self-repair. Stop on budget, repeated failure or regressions, preserve evidence and escalate.
5. Benchmark comparable tasks under controlled models/tools/budgets and disclose limitations. Never assert a global #1 ranking without verified evidence.
6. Publish a QualityReport with tests actually executed, unresolved defects, provenance and release decision. Curate only authorized, verified reusable knowledge; isolate private project data.

Use `../stephen-curry-ui/references/independent-jury.md` as supplemental six-lens craft checklist, not independent-execution evidence. Use the suite's versioned `contracts/schemas/`.

**Image-first gate:** Before a new design is approved, verify >=3 actual generated UI images, matching provenance and frozen DS version. Reject HTML/SVG/React mocks and mere paths as proof. Inspect images, not just metadata.


**Image-only design boundary:** All new visual design artifacts, including Brand/Design System boards and page concept visuals, must come from genuine built-in image generation, never coded drawing, HTML/CSS/SVG/React mockups or code-built screenshots. Code is authorized only to implement already approved generated-image designs. See the main image-only protocol.

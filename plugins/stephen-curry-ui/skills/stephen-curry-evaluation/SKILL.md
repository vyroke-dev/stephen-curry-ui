---
name: stephen-curry-evaluation
description: Arbitrate evidence-backed design reviews and release decisions for substantial UI work; distinguish independent review from a single-agent critique.
---

# Evidence-Based Evaluation

1. Match evaluation effort to scope. Use targeted checks for a small change. For a major experience or a brief requiring independent sign-off, evaluate four separate reviewer reports for the same frozen artifact and Design System versions.
2. For the four-role jury, check that `art_director`, `ux_expert`, `design_system_auditor`, and `frontend_qa` have real, distinct execution provenance, relevant evidence, and no version mismatch. Reject fabricated independence or unsupported claims.
3. Resolve objective defects with reproducible evidence. Critical accessibility, security, privacy, or core-flow failures block the relevant release regardless of aesthetic score.
4. Compare subjective art direction against the approved brand, user intent, originality, and documented rationale. Do not treat votes or scores as ground truth.
5. Stop bounded repair when it stalls, consumes its budget, or causes regressions. Preserve the stable version and explain the unresolved trade-off.
6. For formal release reporting, record only tests run, evidence reviewed, limitations, and the release decision. Do not imply real-user studies, legal clearance, or benchmark leadership without evidence.

Use `../stephen-curry-ui/references/independent-jury.md` for the review method and `../stephen-curry-ui/support/contracts/schemas/` for the bundled contracts when available.

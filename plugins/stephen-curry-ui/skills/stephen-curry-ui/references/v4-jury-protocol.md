# Independent jury protocol

Use this protocol for the full-experience workflow and for any other task whose brief, risk, or release gate calls for independent sign-off. A focused change can use a proportionate review without claiming to have passed an independent jury.

1. Freeze the `artifact_id`, artifact version, Design System version, brief, and evidence pack. Give every reviewer the same evidence baseline.
2. Use four actual, separate reviewer executions: `art_director`, `ux_expert`, `design_system_auditor`, and `frontend_qa`. A role prompt, different heading, or duplicate execution ID does not prove independence. If the host lacks separate agents, mark this jury gate blocked; do not invent reports.
3. For a global Skill install, read the role prompts from `../support/agents/{art-director,ux-expert,design-system-auditor,frontend-qa}.toml` and pass matching instructions to the reviewers. Keep these files within this Skill package; do not install them as global Agent configuration. Treat reviewer prompts as guidance, not a security boundary.
4. Require structured reports with distinct execution provenance, evidence references, and matching artifact/system versions. Validate with the bundled schema at `../support/contracts/schemas/jury-review.schema.json`. The offline validator checks report structure; it cannot verify execution provenance by itself.
5. Deduplicate findings by reproducible cause. Prioritize safety, accessibility, core UX, and engineering defects over popularity. Compare subjective art direction with documented evidence and user intent.
6. Retest affected browser behavior after remediation. Jury reports are not real-user studies, legal clearance, or proof of production readiness.

The six-lens checklist in `whole-experience-qa.md` can supplement review. It does not replace four independent executions when those are required.

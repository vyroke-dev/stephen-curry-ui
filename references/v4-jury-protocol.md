# Independent four-Agent review protocol

1. Run **two separate independent visual-review gates**: first on all seven genuine generated Design System boards **before** page concept generation; second on three image-generated website concept sets. For each gate freeze `artifact_id`, `artifact_version`, `design_system_version`, design brief, original raster images and evidence pack; give identical evidence baseline to all four specialized Agents.
2. Spawn **four separate actual Codex subagent tasks**: `art_director`, `ux_expert`, `design_system_auditor`, `frontend_qa`. Distinct execution identifiers are required. If actual subagent support is missing, do **not** create synthetic reports: mark Jury gate BLOCKED.
3. Each Agent has read-only scope, returns structured JSON aligned to `contracts/schemas/jury-review.schema.json` and evidence references; do not treat the Agent TOML `sandbox_mode` as the only security boundary.
4. All four must evaluate the same frozen versions. Validate schema, finding IDs, execution IDs, evidence links, and consistency. `python tools/scui.py check-jury --file path/to/jury.json --artifact-version v1 --ds-version ds1`.
5. Main Orchestrator deduplicates by reproducible root cause; prioritizes objective safety/UX defects over popularity votes. Subjective art conflict becomes comparative evaluation; strategic ambiguity becomes an explicit approval request.
6. Agent results are advisory, not independent user testing or legal clearance. Retest actual browser artifacts after remediation.

**Preserved v3.1**: six-lens checklist in `references/whole-experience-qa.md` enriches the four independent roles (motion and creative-tech inside Art Director / Frontend QA, etc.), but six perspectives cannot substitute independent Agent executions.

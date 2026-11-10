#!/usr/bin/env python3
"""Stephen Curry UI 4.1: offline contract and scope-aware gate checks.

This utility does not spawn Agents, authenticate approvals, run browsers or modify a Canvas.
All actual capabilities are delegated to the user's supported Codex/OpenCodex host.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
import tomllib
from pathlib import Path, PurePosixPath

SCRIPT_PATH = Path(__file__).resolve()
ROOT = SCRIPT_PATH.parents[1]
PROJECT_ROOT = None
repo_plugin_package = ROOT.parent / "plugins" / "stephen-curry-ui" / "skills" / "stephen-curry-ui"
if (repo_plugin_package / "SKILL.md").is_file():
    SKILL_ROOT = repo_plugin_package
    PROJECT_ROOT = ROOT.parent
elif ROOT.name == "support" and (ROOT.parent / "SKILL.md").is_file():
    SKILL_ROOT = ROOT.parent
    plugin_root = SKILL_ROOT.parents[1] if len(SKILL_ROOT.parents) > 1 else None
    if plugin_root is not None and (plugin_root / ".claude-plugin").is_dir():
        PROJECT_ROOT = SKILL_ROOT.parents[3]
else:
    SKILL_ROOT = None
SCHEMA = ROOT / "contracts" / "schemas"
ROLES = frozenset({"art_director", "ux_expert", "design_system_auditor", "frontend_qa"})


class GateError(ValueError):
    """A required evidence or safety condition was not met."""


def load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise GateError(f"Cannot load JSON {path}: {exc}") from exc


def _nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def require_keys(obj, keys, label):
    if not isinstance(obj, dict):
        raise GateError(f"{label} must be a JSON object")
    missing = [x for x in keys if x not in obj]
    if missing:
        raise GateError(f"{label} missing keys: {', '.join(missing)}")
    if obj.get("schema_version") != "1.0.0":
        raise GateError(f"{label} incompatible schema_version: {obj.get('schema_version')}")


def check_contract(name: str, payload: dict, strict: bool = False):
    """JSON Schema validation where available; basic key check if dependency absent."""
    schema_file = SCHEMA / f"{name}.schema.json"
    if not schema_file.is_file():
        raise GateError(f"Unknown contract: {name}")
    schema = load_json(schema_file)
    require_keys(payload, schema.get("required", []), name)
    try:
        import jsonschema
    except ImportError:
        if strict:
            raise GateError("strict JSON Schema checks require: pip install jsonschema")
        return "BASIC-ONLY (install jsonschema for full schema validation)"
    try:
        jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(payload)
    except jsonschema.ValidationError as exc:
        raise GateError(f"{name} schema invalid at {list(exc.path)}: {exc.message}") from exc
    return "SCHEMA-VALID"


def check_concepts(data, expected_ds: str, evidence_root: str | None = None):
    check_contract("concept-set", data, strict=True)
    if data["design_system_version"] != expected_ds:
        raise GateError("Concept set uses a stale Design System version")
    concepts = data["concepts"]
    if len(concepts) < 3:
        raise GateError("Full-track concept selection requires at least three concepts")
    ids = set()
    fingerprints = set()
    for concept in concepts:
        if concept["design_system_version"] != expected_ds:
            raise GateError(f"Concept {concept['concept_id']} has incompatible DS")
        if concept["concept_id"] in ids:
            raise GateError("Concept IDs must be distinct")
        ids.add(concept["concept_id"])
        for field in ("creative_thesis", "experience_architecture", "layout_strategy", "interaction_grammar"):
            if not _nonempty(concept[field]):
                raise GateError(f"Empty {field} in concept")
        fingerprint = tuple(re.sub(r"\s+", " ", concept[k].lower().strip()) for k in
                            ("creative_thesis", "experience_architecture", "layout_strategy", "interaction_grammar"))
        if fingerprint in fingerprints:
            raise GateError("Identical concepts do not satisfy exploration")
        fingerprints.add(fingerprint)
        if evidence_root is not None:
            root = Path(evidence_root).resolve()
            for ref in concept["high_fidelity_artifacts"]:
                if ref.startswith(("https://", "http://")):
                    raise GateError("External high-fidelity artifacts are not checked by this offline validator")
                p = (root / ref).resolve()
                if root not in p.parents and p != root:
                    raise GateError(f"Evidence ref outside evidence root: {ref}")
                if not p.is_file():
                    raise GateError(f"High fidelity evidence absent: {ref}")
    # Distinct structured descriptions are only a proxy. Actual visual distinctiveness
    # and fidelity require human/visual Agent assessment.
    return f"{len(concepts)} structured concepts VALIDATED; visual quality still needs actual image/Agent review"


def check_jury(data, artifact_version: str, ds_version: str):
    reports = data.get("reviews") if isinstance(data, dict) else data
    if not isinstance(reports, list) or len(reports) != 4:
        raise GateError("The independent jury gate requires four reviewer reports")
    roles, executions, artifact_ids = set(), set(), set()
    for item in reports:
        check_contract("jury-review", item, strict=True)
        if item["status"] != "complete":
            raise GateError(f"Juror {item['role']} did not complete")
        if item["role"] in roles:
            raise GateError(f"Duplicate jury role {item['role']}")
        if item["execution_id"] in executions:
            raise GateError("Independent Agents must have distinct real execution IDs")
        if item["artifact_version"] != artifact_version or item["design_system_version"] != ds_version:
            raise GateError("Jury version mismatch")
        if not item.get("evidence_refs"):
            raise GateError(f"No evidence references for {item['role']}")
        for finding in item["findings"]:
            if not finding["evidence_refs"]:
                raise GateError(f"Finding without evidence: {finding['finding_id']}")
        artifact_ids.add(item["artifact_id"])
        roles.add(item["role"])
        executions.add(item["execution_id"])
    if roles != ROLES or len(artifact_ids) != 1:
        raise GateError("Must have four named reviewer roles on the same artifact")
    # A unique execution_id supplied in JSON cannot prove independently spawned model
    # processes; runtime logs must attest that separately.
    return "Jury report metadata valid; actual independent process execution NOT proven by JSON alone"


def check_quality(data):
    check_contract("quality-report", data, strict=True)
    decision = data["release_decision"]
    checks = data["checks"]
    checks_by_id = {item["check_id"]: item for item in checks}
    if decision == "pass":
        if data["release_blockers"]:
            raise GateError("Cannot pass with remaining release blockers")
        if any(x["outcome"] in {"fail", "blocked"} for x in checks):
            raise GateError("Cannot pass with failed/blocked checks")
        required_gates = set(data["required_gates"])
        if data["scope_tier"] == "full_experience":
            required_gates.update({
                "design_system_approval", "concept_selection", "independent_jury",
                "browser_verification", "accessibility_review",
            })
        for gate in required_gates:
            result = checks_by_id.get(gate)
            if result is None or result["outcome"] != "pass" or not result["evidence_refs"]:
                raise GateError(f"Required gate lacks a passing evidence check: {gate}")
        if "independent_jury" in required_gates and not data.get("jury_report_refs"):
            raise GateError("Independent jury required but no jury report reference was recorded")
        if "browser_verification" in required_gates and not data.get("browser_verified", False):
            raise GateError("Browser verification missing: release cannot pass")
        if any("browser" in gate for gate in required_gates) and not any(
            "browser" in x["check_id"].lower() and x["outcome"] == "pass" for x in checks
        ):
            raise GateError("Browser pass check with evidence required")
        if any("accessibility" in gate for gate in required_gates) and not any(
            "accessibility" in x["check_id"].lower() and x["outcome"] == "pass" for x in checks
        ):
            raise GateError("Accessibility pass check with evidence required")
        if any(x["outcome"] == "pass" and not x["evidence_refs"] for x in checks):
            raise GateError("Cannot claim a passing check without evidence references")
    return f"Quality report internally consistent for scope_tier={data['scope_tier']}; release_decision={decision} (external evidence and approvals not independently authenticated)"


def _safe_relative_path(s):
    if not isinstance(s, str) or not s or "\\" in s or s.startswith("/"):
        return False
    path = PurePosixPath(s)
    return not any(piece in {"..", ""} for piece in path.parts) and not re.match(r"^[A-Za-z]:", s)


def check_canvas(data, state):
    check_contract("canvas-operation", data, strict=True)
    if data["base_canvas_version"] != state.get("canvas_version"):
        raise GateError("STALE_CANVAS_VERSION: reject, rebase required")
    if data["base_code_revision"] != state.get("code_revision"):
        raise GateError("STALE_CODE_REVISION: reject, rebase required")
    if data["operation_type"] == "commit" and not data.get("approval_ref"):
        raise GateError("Commit requires an external approval reference, still independently verify it in host")
    if any(not _safe_relative_path(p) for p in data["allowed_paths"]):
        raise GateError("Unsafe or absolute allowed path")
    return "Canvas operation passed offline precondition checks only; no file modifications or auth performed"


def check_suite():
    expected = {"stephen-curry-ui", "stephen-curry-research", "stephen-curry-brand", "stephen-curry-experience",
                "stephen-curry-design-system", "stephen-curry-creative", "stephen-curry-assets-motion",
                "stephen-curry-frontend", "stephen-curry-visual-qa", "stephen-curry-evaluation"}
    skill_roots = []
    if SKILL_ROOT is not None:
        skill_roots.insert(0, SKILL_ROOT.parent)
    if PROJECT_ROOT is not None:
        skill_roots.extend([
            PROJECT_ROOT / ".agents" / "skills",
            PROJECT_ROOT / "plugins" / "stephen-curry-ui" / "skills",
            PROJECT_ROOT / "skills",
        ])
    skills_root = None
    skills = []
    for candidate in skill_roots:
        candidate_skills = sorted(candidate.glob("stephen-curry-*/SKILL.md"))
        if {path.parent.name for path in candidate_skills} == expected:
            skills_root = candidate
            skills = candidate_skills
            break
    if skills_root is None:
        raise GateError("Complete ten-skill suite not found in the installed, project, or plugin layout")
    names = set()
    for path in skills:
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(?P<front>.*?)\n---\n", text, re.S)
        if not match:
            raise GateError(f"Missing Skill frontmatter: {path}")
        fields = dict(re.findall(r"(?m)^(name|description):\s*(.+?)\s*$", match.group("front")))
        name, desc = fields.get("name"), fields.get("description")
        if not name or name != path.parent.name or name in names or not desc or len(desc) > 1024:
            raise GateError(f"Invalid or duplicated Skill metadata: {path}")
        names.add(name)
        for ref in re.findall(r"\]\(([^)]+)\)", text):
            if ref.startswith(("http:", "https:", "#")):
                continue
            target = (path.parent / ref.split("#")[0]).resolve()
            if not target.is_file() or (target != skills_root and skills_root not in target.parents):
                raise GateError(f"Broken or unsafe Skill reference: {ref} in {path}")
    if names != expected:
        raise GateError(f"Expected Skill set mismatch: {sorted(expected ^ names)}")
    agent_roots = []
    if SKILL_ROOT is not None:
        agent_roots.insert(0, SKILL_ROOT / "support" / "agents")
    if PROJECT_ROOT is not None:
        agent_roots.extend([
            PROJECT_ROOT / ".codex" / "agents",
            PROJECT_ROOT / "support" / "agents",
            PROJECT_ROOT / "plugins" / "stephen-curry-ui" / "skills" / "stephen-curry-ui" / "support" / "agents",
        ])
    agents_dir = next((path for path in agent_roots if len(list(path.glob("*.toml"))) == 4), None)
    if agents_dir is None:
        raise GateError("Four reviewer role prompts not found in the installed or plugin package")
    agents = sorted(agents_dir.glob("*.toml"))
    if len(agents) != 4:
        raise GateError("Expected 4 custom Agent configs")
    found = set()
    for path in agents:
        config = tomllib.loads(path.read_text(encoding="utf-8"))
        for field_name in ("name", "description", "developer_instructions"):
            if not _nonempty(config.get(field_name)):
                raise GateError(f"Agent config missing {field_name}: {path}")
        if config["name"] in found:
            raise GateError("Duplicate Agent name")
        if config.get("sandbox_mode") != "read-only":
            raise GateError(f"Reviewer sandbox should be read-only: {path}")
        found.add(config["name"])
    if found != ROLES:
        raise GateError(f"Wrong Agent set {found}")
    return f"Complete ten-skill suite and {len(agents)} reviewer role prompts structurally validated; live host discovery not run"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("check-suite")
    ct = sub.add_parser("check-contract")
    ct.add_argument("--type", required=True)
    ct.add_argument("--file", required=True)
    ct.add_argument("--strict", action="store_true")
    cp = sub.add_parser("check-concepts")
    cp.add_argument("--file", required=True)
    cp.add_argument("--ds-version", required=True)
    cp.add_argument("--evidence-root")
    jr = sub.add_parser("check-jury")
    jr.add_argument("--file", required=True)
    jr.add_argument("--artifact-version", required=True)
    jr.add_argument("--ds-version", required=True)
    q = sub.add_parser("check-quality")
    q.add_argument("--file", required=True)
    ca = sub.add_parser("check-canvas")
    ca.add_argument("--file", required=True)
    ca.add_argument("--state-file", required=True)
    args = ap.parse_args(argv)
    try:
        if args.command == "check-suite": message = check_suite()
        elif args.command == "check-contract": message = check_contract(args.type, load_json(args.file), strict=args.strict)
        elif args.command == "check-concepts": message = check_concepts(load_json(args.file), args.ds_version, args.evidence_root)
        elif args.command == "check-jury": message = check_jury(load_json(args.file), args.artifact_version, args.ds_version)
        elif args.command == "check-quality": message = check_quality(load_json(args.file))
        elif args.command == "check-canvas": message = check_canvas(load_json(args.file), load_json(args.state_file))
        else: raise AssertionError(args.command)
    except GateError as exc:
        print(f"BLOCKED: {exc}", file=sys.stderr)
        return 2
    print("PASS: " + message)
    return 0


if __name__ == "__main__":
    sys.exit(main())

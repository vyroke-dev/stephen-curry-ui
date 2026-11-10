#!/usr/bin/env python3
"""Stephen Curry UI v4: offline, fail-closed contract/gate checks.

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

ROOT = Path(__file__).resolve().parents[1]
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
        raise GateError("At least three concepts are mandatory")
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
        generation = concept["image_generation"]
        images = [generation["desktop_image_ref"], generation["mobile_image_ref"]]
        if len(set(images)) != 2:
            raise GateError("Desktop and mobile images must be separate image files")
        for img in images:
            if img not in concept["high_fidelity_artifacts"]:
                raise GateError("Generated image must be listed among high fidelity artifacts")
            if Path(img).suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"}:
                raise GateError("High fidelity concept must reference actual raster image format")
        if not _nonempty(generation["tool_identifier"]):
            raise GateError("Missing actual image-generation tool identifier")
        if evidence_root is not None:
            root = Path(evidence_root).resolve()
            def local_file(ref):
                if ref.startswith(("https://", "http://")) or "\\" in ref or Path(ref).is_absolute():
                    raise GateError(f"Unsafe/external concept evidence: {ref}")
                p = (root / ref).resolve()
                if root not in p.parents:
                    raise GateError(f"Evidence ref outside evidence root: {ref}")
                if not p.is_file():
                    raise GateError(f"High fidelity evidence absent: {ref}")
                return p
            if generation["tool_identifier"].startswith("EXAMPLE_ONLY"):
                raise GateError("Placeholder generation metadata is not evidence")
            for ref in concept["high_fidelity_artifacts"]:
                p = local_file(ref)
                if p.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"}:
                    raise GateError(f"High fidelity artifact must be image: {ref}")
                with p.open("rb") as img:
                    head = img.read(32)
                if not ((p.suffix.lower() == ".png" and head.startswith(b"\x89PNG\r\n\x1a\n")) or
                        (p.suffix.lower() in {".jpg", ".jpeg"} and head.startswith(b"\xff\xd8\xff")) or
                        (p.suffix.lower() == ".webp" and head.startswith(b"RIFF") and head[8:12] == b"WEBP")):
                    raise GateError(f"High fidelity evidence is not a matching image file: {ref}")
            prompt_file = local_file(generation["prompt_ref"])
            if not prompt_file.read_text(encoding="utf-8").strip():
                raise GateError("Image prompt evidence is empty")
            if generation.get("generation_record_ref"):
                record = load_json(local_file(generation["generation_record_ref"]))
                if record.get("tool_identifier") != generation["tool_identifier"] or not record.get("generation_completed"):
                    raise GateError("Generation record missing/mismatched tool or completion")
    # Distinct structured descriptions are only a proxy. Actual visual distinctiveness
    # and fidelity require human/visual Agent assessment.
    return (f"{len(concepts)} structured concepts VALIDATED; "
            + ("local image bytes and prompt/record evidence checked; " if evidence_root is not None else "actual images NOT checked without --evidence-root; ")
            + "authentic generator provenance and visual quality still need actual tool logs/human/Agent review")



BOARD_IDS = frozenset({
    "brand-art-direction", "color-system", "typography", "layout-spacing",
    "component-library", "responsive", "motion-interaction"
})


def _evidence_file(evidence_root, ref):
    if not isinstance(ref, str) or not ref or "\\" in ref or Path(ref).is_absolute() or ref.startswith(("http:", "https:")):
        raise GateError(f"Unsafe evidence ref: {ref}")
    root = Path(evidence_root).resolve()
    p = (root / ref).resolve()
    if root not in p.parents or not p.is_file():
        raise GateError(f"Evidence absent or outside root: {ref}")
    return p


def _raster_evidence(evidence_root, ref):
    p = _evidence_file(evidence_root, ref)
    ext = p.suffix.lower()
    if ext not in {".png", ".jpg", ".jpeg", ".webp"}:
        raise GateError(f"Design images require real PNG/JPEG/WebP: {ref}")
    head = p.read_bytes()[:32]
    valid = ((ext == ".png" and head.startswith(b"\x89PNG\r\n\x1a\n")) or
             (ext in {".jpg", ".jpeg"} and head.startswith(b"\xff\xd8\xff")) or
             (ext == ".webp" and head.startswith(b"RIFF") and head[8:12] == b"WEBP"))
    if not valid:
        raise GateError(f"Not a matching raster image file: {ref}")
    try:
        from PIL import Image
        with Image.open(p) as image:
            image.verify()
    except ImportError:
        raise GateError("Raster validation requires Pillow (pip install Pillow)")
    except Exception as exc:
        raise GateError(f"Invalid or corrupt raster image: {ref}: {exc}") from exc
    return p


def check_design_boards(data, expected_ds, evidence_root=None, require_approved=False):
    """Static design-board verification. This NEVER authenticates generator or approver."""
    check_contract("design-system-boards", data, strict=True)
    if data["design_system_version"] != expected_ds:
        raise GateError("Design System board version mismatch")
    if require_approved and data["status"] != "approved":
        raise GateError("Image-generated Design System boards are not approved")
    board_ids = [board["board_id"] for board in data["boards"]]
    if len(board_ids) != len(set(board_ids)) or set(board_ids) != BOARD_IDS:
        raise GateError("Exactly seven distinct required image-generated Design System board types expected")
    all_refs = set()
    for board in data["boards"]:
        if board["design_system_version"] != expected_ds:
            raise GateError("One Design System board uses a stale revision")
        g = board["image_generation"]
        if g["method"] != "built_in_image_generation" or not _nonempty(g["tool_identifier"]):
            raise GateError("Real built-in image generation metadata required")
        if g["tool_identifier"].startswith("EXAMPLE_ONLY"):
            if evidence_root is not None:
                raise GateError("Placeholder generator cannot pass local board evidence check")
        image_ref = g["image_ref"]
        if Path(image_ref).suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"}:
            raise GateError("Code-rendered visual or non-raster board is not allowed")
        if image_ref in all_refs:
            raise GateError("Different board categories must have distinct image references")
        all_refs.add(image_ref)
        if evidence_root is not None:
            _raster_evidence(evidence_root, image_ref)
            prompt = _evidence_file(evidence_root, g["prompt_ref"]).read_text(encoding="utf-8")
            if not prompt.strip():
                raise GateError("Blank Design System board prompt")
            record = load_json(_evidence_file(evidence_root, g["generation_record_ref"]))
            if record.get("tool_identifier") != g["tool_identifier"] or not record.get("generation_completed"):
                raise GateError("Design System board generation record missing or inconsistent")
    return ("Seven image-generated Design System board references structurally validated; "
            + ("local raster bytes and prompt/record files checked; " if evidence_root is not None else "raster files NOT checked without --evidence-root; ")
            + "actual built-in tool provenance, visual quality, jury independence and human approval remain externally unverified")


def check_design_gates(boards, concepts, expected_ds, evidence_root):
    if not evidence_root:
        raise GateError("Full image-only design gate requires --evidence-root")
    msg = check_design_boards(boards, expected_ds, evidence_root, require_approved=True)
    cmsg = check_concepts(concepts, expected_ds, evidence_root)
    return msg + "; " + cmsg + "; recorded approval_ref is NOT independently authenticated"

def check_jury(data, artifact_version: str, ds_version: str):
    reports = data.get("reviews") if isinstance(data, dict) else data
    if not isinstance(reports, list) or len(reports) != 4:
        raise GateError("Exactly 4 independent jury reports required")
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
    if decision == "pass":
        if data["release_blockers"]:
            raise GateError("Cannot pass with remaining release blockers")
        if any(x["outcome"] in {"fail", "blocked"} for x in checks):
            raise GateError("Cannot pass with failed/blocked checks")
        if not data.get("browser_verified", False):
            raise GateError("Browser verification missing: release cannot pass")
        if not any("browser" in x["check_id"].lower() and x["outcome"] == "pass" for x in checks):
            raise GateError("Browser pass check with evidence required")
        if not any("accessibility" in x["check_id"].lower() and x["outcome"] == "pass" for x in checks):
            raise GateError("Accessibility pass check with evidence required")
        if any(x["outcome"] == "pass" and not x["evidence_refs"] for x in checks):
            raise GateError("Cannot claim a passing check without evidence references")
    return f"Quality report internally consistent; release_decision={decision} (external test evidence not independently authenticated)"


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
    skills = sorted((ROOT / ".agents" / "skills").glob("*/SKILL.md"))
    expected = {"stephen-curry-ui", "stephen-curry-research", "stephen-curry-brand", "stephen-curry-experience",
                "stephen-curry-design-system", "stephen-curry-creative", "stephen-curry-assets-motion",
                "stephen-curry-frontend", "stephen-curry-visual-qa", "stephen-curry-evaluation"}
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
            if not target.is_file() or ROOT not in target.parents:
                raise GateError(f"Broken or unsafe Skill reference: {ref} in {path}")
    if names != expected:
        raise GateError(f"Expected Skill set mismatch: {sorted(expected ^ names)}")
    agents = sorted((ROOT / ".codex" / "agents").glob("*.toml"))
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
    return f"{len(skills)} native Skills and {len(agents)} TOML Agent configs structurally validated; live Codex discovery not run"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("check-suite")
    ct = sub.add_parser("check-contract")
    ct.add_argument("--type", required=True)
    ct.add_argument("--file", required=True)
    ct.add_argument("--strict", action="store_true")
    db = sub.add_parser("check-design-boards")
    db.add_argument("--file", required=True)
    db.add_argument("--ds-version", required=True)
    db.add_argument("--evidence-root")
    db.add_argument("--require-approved", action="store_true")
    da = sub.add_parser("check-design-gates")
    da.add_argument("--boards-file", required=True)
    da.add_argument("--concepts-file", required=True)
    da.add_argument("--ds-version", required=True)
    da.add_argument("--evidence-root", required=True)
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
        elif args.command == "check-design-boards": message = check_design_boards(load_json(args.file), args.ds_version, args.evidence_root, args.require_approved)
        elif args.command == "check-design-gates": message = check_design_gates(load_json(args.boards_file), load_json(args.concepts_file), args.ds_version, args.evidence_root)
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

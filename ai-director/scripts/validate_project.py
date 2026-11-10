#!/usr/bin/env python3
"""Dependency-free sanity validation for an AI Director project JSON.

Run: python3 scripts/validate_project.py path/to/project.json
Exit 0 when no errors, exit 1 for validation errors, exit 2 for unreadable JSON.
This checks more than basic syntax but does not fully implement JSON Schema.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

SCREEN_DIRECTIONS = {"left-to-right", "right-to-left", "stationary", "unspecified"}
GEN_STATUSES = {"planned", "submitted", "in_progress", "completed", "failed", "cancelled", "not_available"}
SHOT_STATUSES = {"planned", "approved", "submitted", "in_progress", "completed", "failed"}
ASSET_KINDS = {"character", "location", "prop", "product", "style", "other"}


def _str(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _positive(value: Any) -> bool:
    return type(value) in (int, float) and math.isfinite(value) and value > 0


def validate(project: Any) -> tuple[list[str], list[str]]:
    """Return (errors, warnings). No changes to the input are made."""
    errors: list[str] = []
    warnings: list[str] = []

    def error(msg: str) -> None:
        errors.append(msg)

    def require_string(obj: dict, key: str, path: str) -> None:
        if not _str(obj.get(key)):
            error(f"{path}.{key}: required nonempty string")

    if not isinstance(project, dict):
        return ["project: must be a JSON object"], []

    for key in ("project_id", "title", "version", "language"):
        require_string(project, key, "project")
    for key in ("assumptions", "approved_decisions"):
        if not isinstance(project.get(key), list) or any(not isinstance(s, str) for s in project[key]):
            error(f"project.{key}: required array of strings")

    fmt = project.get("format")
    if not isinstance(fmt, dict):
        error("project.format: required object")
        fmt = {}
    target = fmt.get("target_duration_s")
    if not _positive(target):
        error("format.target_duration_s: positive finite number required")
    if fmt.get("aspect_ratio") not in {"16:9", "9:16", "1:1", "4:5", "2.39:1", "other"}:
        error("format.aspect_ratio: invalid or missing")
    if not _positive(fmt.get("fps_target")):
        error("format.fps_target: positive finite number required")
    require_string(fmt, "resolution_target", "format")

    creative = project.get("creative")
    if not isinstance(creative, dict):
        error("project.creative: required object")
        creative = {}
    for key in ("logline", "genre", "emotion_arc", "visual_bible"):
        require_string(creative, key, "creative")
    beats = creative.get("beats")
    if not isinstance(beats, list) or not beats:
        error("creative.beats: required nonempty array")
        beats = []
    beat_total = 0.0
    beat_ids: set[str] = set()
    for i, beat in enumerate(beats):
        path = f"creative.beats[{i}]"
        if not isinstance(beat, dict):
            error(f"{path}: must be an object")
            continue
        for key in ("id", "goal"):
            require_string(beat, key, path)
        if _str(beat.get("id")):
            if beat["id"] in beat_ids:
                error(f"{path}.id: duplicate beat ID")
            beat_ids.add(beat["id"])
        if _positive(beat.get("duration_s")):
            beat_total += beat["duration_s"]
        else:
            error(f"{path}.duration_s: positive finite number required")

    assets = project.get("assets")
    if not isinstance(assets, list):
        error("project.assets: required array")
        assets = []
    asset_ids: set[str] = set()
    for i, asset in enumerate(assets):
        path = f"assets[{i}]"
        if not isinstance(asset, dict):
            error(f"{path}: must be an object")
            continue
        for key in ("asset_id", "description"):
            require_string(asset, key, path)
        if _str(asset.get("asset_id")):
            if asset["asset_id"] in asset_ids:
                error(f"{path}.asset_id: duplicate asset ID")
            asset_ids.add(asset["asset_id"])
        if asset.get("kind") not in ASSET_KINDS:
            error(f"{path}.kind: invalid or missing")
        for key in ("locked_traits", "reference_uris"):
            if not isinstance(asset.get(key), list) or any(not _str(s) for s in asset[key]):
                error(f"{path}.{key}: required array of nonempty strings")

    shots = project.get("shots")
    if not isinstance(shots, list) or not shots:
        error("project.shots: required nonempty array")
        shots = []
    shot_total = 0.0
    shot_ids: set[str] = set()
    orders: set[int] = set()
    for i, shot in enumerate(shots):
        path = f"shots[{i}]"
        if not isinstance(shot, dict):
            error(f"{path}: must be an object")
            continue
        for key in ("shot_id", "scene_id", "story_purpose", "action", "shot_size", "angle", "composition", "camera_motion", "lighting", "palette", "prompt"):
            require_string(shot, key, path)
        if _str(shot.get("shot_id")):
            if shot["shot_id"] in shot_ids:
                error(f"{path}.shot_id: duplicate shot ID")
            shot_ids.add(shot["shot_id"])
        order = shot.get("order")
        if type(order) is not int or order <= 0:
            error(f"{path}.order: positive integer required")
        elif order in orders:
            error(f"{path}.order: duplicate order")
        else:
            orders.add(order)
        if _positive(shot.get("duration_s")):
            shot_total += shot["duration_s"]
        else:
            error(f"{path}.duration_s: positive finite number required")
        for key in ("lens_mm", "aperture_f"):
            if shot.get(key) is not None and not _positive(shot[key]):
                error(f"{path}.{key}: must be positive or null")
        if not isinstance(shot.get("sound"), str):
            error(f"{path}.sound: required string")
        if shot.get("status") not in SHOT_STATUSES:
            error(f"{path}.status: invalid or missing")
        refs = shot.get("asset_refs")
        if not isinstance(refs, list) or any(not _str(x) for x in refs):
            error(f"{path}.asset_refs: required array of nonempty strings")
        else:
            if len(refs) != len(set(refs)):
                error(f"{path}.asset_refs: duplicate asset reference")
            for ref in refs:
                if ref not in asset_ids:
                    error(f"{path}.asset_refs: unknown asset '{ref}'")
        avoid = shot.get("avoid")
        if not isinstance(avoid, list) or any(not isinstance(x, str) for x in avoid):
            error(f"{path}.avoid: required array of strings")
        continuity = shot.get("continuity")
        if not isinstance(continuity, dict):
            error(f"{path}.continuity: required object")
        else:
            for key in ("entry", "exit"):
                require_string(continuity, key, f"{path}.continuity")
            if continuity.get("screen_direction") not in SCREEN_DIRECTIONS:
                error(f"{path}.continuity.screen_direction: invalid or missing")
        if _str(shot.get("camera_motion")) and " + " in shot["camera_motion"]:
            warnings.append(f"{path}.camera_motion: multiple moves; check feasibility")
        if _str(shot.get("prompt")) and len(shot["prompt"].split()) < 9:
            warnings.append(f"{path}.prompt: very short, check filmability")

    if orders and sorted(orders) != list(range(1, len(shots) + 1)):
        error("shots.order: must form contiguous sequence starting at 1")
    if _positive(target):
        if shots and abs(shot_total - target) > 0.01:
            error(f"shots total {shot_total:g}s differs from target {target:g}s")
        if beats and abs(beat_total - target) > 0.01:
            error(f"beats total {beat_total:g}s differs from target {target:g}s")

    generation = project.get("generation")
    if not isinstance(generation, dict):
        error("project.generation: required object")
    else:
        status = generation.get("status")
        if status not in GEN_STATUSES:
            error("generation.status: invalid or missing")
        if generation.get("provider") is not None and not _str(generation.get("provider")):
            error("generation.provider: must be null or nonempty string")
        for key in ("job_ids", "output_uris"):
            if not isinstance(generation.get(key), list) or any(not _str(x) for x in generation[key]):
                error(f"generation.{key}: required array of nonempty strings")
        if status == "planned" and (generation.get("job_ids") or generation.get("output_uris")):
            warnings.append("generation: planned status has jobs/outputs; reconcile observed state")
        if status == "completed" and not generation.get("output_uris"):
            error("generation: completed status requires observed output URIs")
        if status in {"submitted", "in_progress", "completed"} and not generation.get("job_ids"):
            warnings.append("generation: active/completed status has no recorded job IDs")
    return errors, warnings


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python3 scripts/validate_project.py path/to/project.json", file=sys.stderr)
        return 2
    try:
        project = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"Cannot read project JSON: {exc}", file=sys.stderr)
        return 2
    errors, warnings = validate(project)
    for msg in warnings:
        print(f"WARNING: {msg}")
    for msg in errors:
        print(f"ERROR: {msg}")
    if errors:
        print(f"INVALID: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"VALID: 0 error(s), {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

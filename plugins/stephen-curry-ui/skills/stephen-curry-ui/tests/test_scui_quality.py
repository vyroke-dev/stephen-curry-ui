"""The offline release checker must enforce gates declared for the project scope."""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
if sys.version_info >= (3, 11):
    sys.path.insert(0, str(ROOT / "support" / "tools"))
    import scui
else:
    scui = None


def report():
    gate_ids = ["design_system_approval", "concept_selection", "independent_jury"]
    checks = [
        {"check_id": gate_id, "outcome": "pass", "evidence_refs": [f"evidence/{gate_id}.json"]}
        for gate_id in gate_ids
    ]
    checks.extend([
        {"check_id": "browser_verification", "outcome": "pass", "evidence_refs": ["evidence/browser.json"]},
        {"check_id": "accessibility_review", "outcome": "pass", "evidence_refs": ["evidence/a11y.json"]},
    ])
    return {
        "schema_version": "1.0.0", "project_id": "demo", "artifact_id": "site",
        "artifact_version": "v1", "scope_tier": "full_experience",
        "required_gates": gate_ids, "checks": checks, "release_blockers": [],
        "release_decision": "pass", "jury_report_refs": ["evidence/jury.json"],
        "browser_verified": True, "human_tested": False,
    }


@unittest.skipUnless(sys.version_info >= (3, 11), "scui.py requires Python 3.11+")
class RequiredGateTest(unittest.TestCase):
    def test_declared_pass_with_evidence_is_consistent(self):
        with patch.object(scui, "check_contract", return_value="mock-valid"):
            self.assertIn("release_decision=pass", scui.check_quality(report()))

    def test_focused_pass_does_not_require_full_site_qa(self):
        data = {
            "schema_version": "1.0.0",
            "project_id": "demo",
            "artifact_id": "button",
            "artifact_version": "v1",
            "scope_tier": "focused_change",
            "required_gates": [],
            "checks": [{"check_id": "label_copy", "outcome": "pass", "evidence_refs": ["diff"]}],
            "release_blockers": [],
            "release_decision": "pass",
            "browser_verified": False,
            "human_tested": False,
        }
        with patch.object(scui, "check_contract", return_value="mock-valid"):
            self.assertIn("scope_tier=focused_change", scui.check_quality(data))

    def test_missing_required_gate_blocks_release(self):
        data = report()
        data["checks"] = [item for item in data["checks"] if item["check_id"] != "independent_jury"]
        with patch.object(scui, "check_contract", return_value="mock-valid"):
            with self.assertRaisesRegex(scui.GateError, "Required gate"):
                scui.check_quality(data)

    def test_jury_gate_requires_report_reference(self):
        data = report()
        data["jury_report_refs"] = []
        with patch.object(scui, "check_contract", return_value="mock-valid"):
            with self.assertRaisesRegex(scui.GateError, "jury report reference"):
                scui.check_quality(data)


if __name__ == "__main__":
    unittest.main()


import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("ai_director_validator", ROOT / "scripts" / "validate_project.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class ProjectValidationTests(unittest.TestCase):
    def setUp(self):
        self.project = json.loads((ROOT / "assets" / "example-noir-project.json").read_text(encoding="utf-8"))

    def test_good_example(self):
        errors, warnings = module.validate(self.project)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_bad_duration(self):
        p = copy.deepcopy(self.project)
        p["shots"][0]["duration_s"] = 9
        self.assertIn("differs from target", " ".join(module.validate(p)[0]))

    def test_unknown_asset(self):
        p = copy.deepcopy(self.project)
        p["shots"][0]["asset_refs"].append("not-real")
        self.assertIn("unknown asset", " ".join(module.validate(p)[0]))

    def test_duplicate_shot(self):
        p = copy.deepcopy(self.project)
        p["shots"][1]["shot_id"] = "SH01"
        self.assertIn("duplicate shot ID", " ".join(module.validate(p)[0]))

    def test_duplicate_asset(self):
        p = copy.deepcopy(self.project)
        p["assets"][1]["asset_id"] = "ch-detective"
        self.assertIn("duplicate asset ID", " ".join(module.validate(p)[0]))

    def test_bad_screen_direction(self):
        p = copy.deepcopy(self.project)
        p["shots"][1]["continuity"]["screen_direction"] = "sidewaysish"
        self.assertIn("screen_direction", " ".join(module.validate(p)[0]))

    def test_dishonest_completed(self):
        p = copy.deepcopy(self.project)
        p["generation"]["status"] = "completed"
        self.assertIn("requires observed output", " ".join(module.validate(p)[0]))

    def test_boolean_duration_not_accepted(self):
        p = copy.deepcopy(self.project)
        p["shots"][0]["duration_s"] = True
        self.assertIn("positive finite number required", " ".join(module.validate(p)[0]))

    def test_root_object_required(self):
        errors, _ = module.validate([1, 2])
        self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()

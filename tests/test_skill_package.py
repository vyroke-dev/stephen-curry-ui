"""Static acceptance tests for the Stephen Curry UI agent skill package.

These test the written contract, not the behavior of a running OpenCodex model.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SkillPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

    def test_frontmatter_and_slug(self):
        match = re.match(r"\A---\n(.*?)\n---\n", self.skill, re.S)
        self.assertIsNotNone(match, "Missing YAML frontmatter")
        meta = match.group(1)
        self.assertRegex(meta, r"(?m)^name: stephen-curry-ui$")
        self.assertRegex(meta, r"(?m)^description: .{40,1024}$")

    def test_all_twelve_rules_covered(self):
        for label in [
            "Intelligent Hybrid Autonomy", "Reference-First Design",
            "Adaptive Creative Exploration", "Extreme Visual-First",
            "Adaptive Motion Intelligence", "Multi-Agent Quality Assurance",
            "Deep AI Collaboration", "Unlimited Creative Engineering",
            "Adaptive Signature Design", "Design Memory",
            "Maximum Visual Fidelity", "Adaptive Asset Direction",
        ]:
            with self.subTest(label=label):
                self.assertIn(label, self.skill)

    def test_reference_gate_is_before_design_and_code(self):
        self.assertIn("Reference Brief", self.skill)
        self.assertIn("before concept generation or implementation", self.skill)

    def test_adaptive_creative_and_visual_gates(self):
        for term in ["small changes", "high-impact", "desktop", "mobile", "approval"]:
            with self.subTest(term=term):
                self.assertIn(term, self.skill.lower())

    def test_tool_detection_and_honest_fallback(self):
        for term in ["Opus 5.5", "GPT", "image-generation tool", "unavailable", "sequential"]:
            with self.subTest(term=term):
                self.assertIn(term, self.skill)

    def test_six_review_roles_documented(self):
        doc = (ROOT / "references/quality-gates.md").read_text(encoding="utf-8")
        for role in ["Art Director", "Motion Director", "Creative Technologist", "UX Auditor", "Performance Engineer", "Engineering Reviewer"]:
            with self.subTest(role=role):
                self.assertIn(role, doc)
        for status in ["PASS", "FAIL", "BLOCKED"]:
            self.assertIn(status, doc)

    def test_privacy_and_memory_rules(self):
        doc = (ROOT / "references/memory-and-privacy.md").read_text(encoding="utf-8")
        for term in ["client", "consent", "private", "shared", "verified"]:
            self.assertIn(term, doc.lower())

    def test_all_referenced_local_files_exist(self):
        references = re.findall(r"\]\((references/[^)#]+|assets/[^)#]+)\)", self.skill)
        self.assertGreaterEqual(len(references), 5)
        for relpath in references:
            with self.subTest(relpath=relpath):
                self.assertTrue((ROOT / relpath).is_file(), relpath)

    def test_instruction_is_not_implausible_automation_claim(self):
        self.assertNotIn("automatically trains itself", self.skill)
        self.assertIn("Do not claim", self.skill)


if __name__ == "__main__":
    unittest.main()

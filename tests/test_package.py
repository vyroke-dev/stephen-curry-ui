"""Package structure, adaptive workflow, and v3.1 asset compatibility checks."""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
repo_plugin_package = ROOT / "plugins" / "stephen-curry-ui" / "skills" / "stephen-curry-ui"
if (repo_plugin_package / "SKILL.md").is_file():
    ROOT = repo_plugin_package
SUITE = ROOT.parent
EXPECTED = {
    "stephen-curry-ui", "stephen-curry-research", "stephen-curry-brand",
    "stephen-curry-experience", "stephen-curry-design-system",
    "stephen-curry-creative", "stephen-curry-assets-motion",
    "stephen-curry-frontend", "stephen-curry-visual-qa",
    "stephen-curry-evaluation",
}


class SkillPackageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf8")

    def test_metadata(self):
        self.assertRegex(self.skill, r"\A---\nname: stephen-curry-ui\ndescription: .+\n---\n")

    def test_scope_adaptive_workflow(self):
        for term in [
            "Choose the smallest workflow that fits", "Focused change",
            "New site, broad redesign", "at least three",
            "four real, separate reviewer executions", "WCAG 2.2 AA",
            "metadata alone is not consent", "Never assume",
        ]:
            with self.subTest(term=term):
                self.assertIn(term.lower(), self.skill.lower())

    def test_original_v31_material_preserved(self):
        legacy = (ROOT / "references/v3.1-original-SKILL.txt").read_text(encoding="utf8")
        for term in [
            "Intelligent Hybrid Autonomy", "Reference-First Design",
            "Adaptive Creative Exploration", "Extreme Visual-First",
            "Motion Intelligence", "Deep AI Collaboration",
            "Unlimited Creative Engineering", "Design Memory",
            "Higgsfield", "Model-agnostic",
        ]:
            with self.subTest(term=term):
                self.assertIn(term.lower(), legacy.lower())

    def test_preserved_scripts_and_templates(self):
        for filename in [
            "experience_audit.py", "experience_matrix.py", "style_explorer.py",
            "motion_evidence.py", "visual_metrics.py", "blind_jury.py",
            "design_guard.py", "validate_package.py",
        ]:
            self.assertTrue((ROOT / "scripts" / filename).is_file())
        for filename in [
            "reference-dossier.md", "experience-blueprint.md",
            "interaction-contract.md", "asset-manifest.md", "qa-matrix.md", "handoff.md",
        ]:
            self.assertTrue((ROOT / "templates" / filename).is_file())

    def test_complete_ten_skill_suite_and_links(self):
        skill_dirs = sorted(path for path in SUITE.glob("stephen-curry-*") if (path / "SKILL.md").is_file())
        self.assertEqual({path.name for path in skill_dirs}, EXPECTED)
        count = 0
        for base in skill_dirs:
            for doc in base.rglob("*.md"):
                for link in re.findall(r"\]\(([^)]+)\)", doc.read_text(encoding="utf8")):
                    if link.startswith(("http://", "https://", "#", "sandbox:")):
                        continue
                    candidate = (doc.parent / link.split("#")[0]).resolve()
                    self.assertTrue(candidate.is_file(), f"{doc}: broken link {link}")
                    self.assertTrue(candidate == SUITE or SUITE in candidate.parents, f"{doc}: unsafe link {link}")
                    count += 1
        self.assertGreaterEqual(count, 15)

    @unittest.skipUnless(sys.version_info >= (3, 11), "scui.py requires Python 3.11+")
    def test_offline_suite_discovery(self):
        sys.path.insert(0, str(ROOT / "support" / "tools"))
        import scui
        self.assertIn("ten-skill suite", scui.check_suite())


if __name__ == "__main__":
    unittest.main()

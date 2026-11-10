"""V4 master skill packaging and v3.1 preserved-asset compatibility checks.

The old v3.1 metadata/prose tests were updated for the v4 design doctrine, while
behavior tests for the unchanged v3.1 scripts remain in other test modules.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUITE = ROOT.parents[2]

class SkillPackageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill=(ROOT/'SKILL.md').read_text('utf8')

    def test_metadata(self):
        self.assertRegex(self.skill, r'\A---\nname: stephen-curry-ui\ndescription: .+\n---\n')

    def test_v4_approved_gates(self):
        for term in ['Image-Only Design System First','Maximum Depth Research First',
                     'three generated concept sets','independent jury','four actual independent',
                     'WCAG 2.2 AA','OpenCodex','Codex','#43 remains undecided',
                     'browser','Canvas','approved generated Design System boards']:
            with self.subTest(term=term): self.assertIn(term.lower(),self.skill.lower())

    def test_design_is_image_only(self):
        for term in ('Image-Only', 'seven', 'image-generation', 'No HTML/CSS/JSX/React/SVG'):
            self.assertIn(term.lower(), self.skill.lower())
        self.assertFalse((ROOT/'scripts/style_explorer.py').exists())
        self.assertFalse((ROOT/'examples/creative-explorer.html').exists())

    def test_preserved_scripts_and_templates(self):
        for filename in ['experience_audit.py','experience_matrix.py',
                         'motion_evidence.py','visual_metrics.py','blind_jury.py',
                         'design_guard.py','validate_package.py']:
            self.assertTrue((ROOT/'scripts'/filename).is_file())
        for filename in ['reference-dossier.md','experience-blueprint.md',
                         'interaction-contract.md','asset-manifest.md','qa-matrix.md','handoff.md']:
            self.assertTrue((ROOT/'templates'/filename).is_file())

    def test_relative_links_in_core_and_specialists(self):
        count=0
        for base in (ROOT, *SUITE.joinpath('.agents/skills').glob('stephen-curry-*/')):
            for doc in base.rglob('*.md'):
                for link in re.findall(r'\]\(([^)]+)\)',doc.read_text('utf8')):
                    if link.startswith(('http://','https://','#','sandbox:')): continue
                    candidate=(doc.parent/link.split('#')[0]).resolve()
                    self.assertTrue(candidate.is_file(),f'{doc}: {link}')
                    self.assertTrue(SUITE==candidate or SUITE in candidate.parents)
                    count += 1
        self.assertGreaterEqual(count,15)

if __name__ == '__main__': unittest.main()

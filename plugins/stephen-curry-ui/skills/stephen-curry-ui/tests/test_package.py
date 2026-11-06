import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


class SkillPackageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')

    def test_frontmatter(self):
        self.assertTrue(self.skill.startswith('---\n'))
        fm=re.match(r'\A---\n(.*?)\n---\n', self.skill, re.S)
        self.assertIsNotNone(fm)
        self.assertRegex(fm.group(1),r'(?m)^name: stephen-curry-ui$')
        self.assertRegex(fm.group(1),r'(?m)^description: .{40,1024}$')

    def test_all_foundations(self):
        names=["Intelligent Hybrid Autonomy", "Reference-First Design", "Adaptive Creative Exploration", "Extreme Visual-First", "Adaptive Motion Intelligence", "Multi-Agent Quality Assurance", "Deep AI Collaboration", "Unlimited Creative Engineering", "Adaptive Signature Design", "Design Memory", "Maximum Visual Fidelity", "Adaptive Asset Direction"]
        for name in names:
            with self.subTest(name=name):self.assertIn(name,self.skill)

    def test_gates_and_experience_first(self):
        for keyword in ['Gate 0','Gate 1','Gate 2','Gate 3','Gate 4','Gate 5','Gate 6','whole journey','middle','closing','route','state','browser prototype']:
            with self.subTest(keyword=keyword): self.assertIn(keyword.lower(),self.skill.lower())

    def test_higgsfield_optional_and_model_flexible(self):
        for keyword in ['Higgsfield','optional','Opus 5.5','GPT', 'credits','current model','Claude Code']:
            with self.subTest(keyword=keyword):self.assertIn(keyword,self.skill)

    def test_six_qa_roles(self):
        doc=(ROOT/'references/whole-experience-qa.md').read_text()
        for role in ['Art Director','Motion Director','Creative Technologist','UX Auditor','Performance Engineer','Engineering Reviewer']:
            self.assertIn(role,doc)
        for word in ['PASS','FAIL','BLOCKED','P0','P1','P2','P3']:
            self.assertIn(word,doc)

    def test_four_benchmarks(self):
        doc=(ROOT/'references/four-benchmarks.md').read_text()
        for url in ['sondaven.com/en','silencio.es/','why.zero.university/','unseen.co/']:
            self.assertIn(url,doc)
        self.assertIn('NOT LIVE-OBSERVED',doc)

    def test_principled_fallback(self):
        for word in ['actual','unavailable','do not','never','BLOCKED']:
            self.assertIn(word.lower(),self.skill.lower())

    def test_relative_links(self):
        count=0
        for doc in ROOT.rglob('*.md'):
            for link in re.findall(r'\]\(([^)]+)\)',doc.read_text(encoding='utf-8')):
                if link.startswith(('http://','https://','#','sandbox:')):continue
                self.assertTrue((doc.parent/link.split('#')[0]).is_file(),f'{doc}: {link}')
                count+=1
        self.assertGreaterEqual(count,15)

    def test_key_templates(self):
        for filename in ['reference-dossier.md','experience-blueprint.md','interaction-contract.md','asset-manifest.md','qa-matrix.md','handoff.md']:
            self.assertTrue((ROOT/'templates'/filename).is_file())

    def test_engineering_and_accessibility(self):
        doc=(ROOT/'references/delivery-standards.md').read_text()
        for word in ['LCP','INP','CLS','keyboard','reduced-motion','WCAG']:
            self.assertIn(word,doc)

if __name__=='__main__':unittest.main()

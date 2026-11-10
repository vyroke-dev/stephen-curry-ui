import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('scui', ROOT/'tools/scui.py')
scui = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scui)


def example(name):
    return json.loads((ROOT/'contracts/examples'/f'{name}.example.json').read_text('utf8'))


class SkillV4Test(unittest.TestCase):
    def test_skills_and_agents(self):
        self.assertIn('10 native Skills', scui.check_suite())

    def test_examples_against_json_schema(self):
        for path in (ROOT/'contracts/examples').glob('*.example.json'):
            name = path.name.replace('.example.json', '')
            with self.subTest(name=name):
                self.assertEqual(scui.check_contract(name, example(name), strict=True), 'SCHEMA-VALID')

    def test_invalid_schema_fails(self):
        obj = example('design-system'); del obj['tokens']
        with self.assertRaises(scui.GateError): scui.check_contract('design-system', obj, strict=True)

    def test_three_distinct_concepts(self):
        obj = example('concept-set')
        self.assertIn('3 structured', scui.check_concepts(obj, 'ds1'))
        with self.assertRaises(scui.GateError): scui.check_concepts(obj, 'stale')
        obj['concepts'].append(copy.deepcopy(obj['concepts'][0]))
        with self.assertRaises(scui.GateError): scui.check_concepts(obj, 'ds1')

    def test_missing_visual_evidence_fails_when_required(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(scui.GateError, 'Placeholder generation metadata|evidence absent'):
                scui.check_concepts(example('concept-set'), 'ds1', directory)

    def test_four_distinct_jurors(self):
        reports = []
        for index, role in enumerate(sorted(scui.ROLES)):
            r = example('jury-review')
            r['role'] = role
            r['review_id'] = f'r{index}'
            r['execution_id'] = f'actual-run-{index}'
            reports.append(r)
        self.assertIn('metadata valid', scui.check_jury(reports, 'v1', 'ds1'))
        reports[1]['execution_id'] = reports[0]['execution_id']
        with self.assertRaisesRegex(scui.GateError, 'distinct'):
            scui.check_jury(reports, 'v1', 'ds1')
        reports[1]['execution_id'] = 'actual-run-1'
        reports[1]['artifact_version'] = 'stale'
        with self.assertRaisesRegex(scui.GateError, 'version mismatch'):
            scui.check_jury(reports, 'v1', 'ds1')
        with self.assertRaises(scui.GateError):
            scui.check_jury(reports[:3], 'v1', 'ds1')

    def test_quality_blocks_false_pass(self):
        r=example('quality-report')
        self.assertIn('blocked', scui.check_quality(r))
        r['release_decision'] = 'pass'
        with self.assertRaises(scui.GateError): scui.check_quality(r)
        r['release_blockers'] = []
        r['checks'] = [{'check_id':'browser','outcome':'pass','evidence_refs':['actual/browser.png']},
                       {'check_id':'accessibility','outcome':'pass','evidence_refs':['actual/a11y.json']}]
        r['browser_verified'] = True
        self.assertIn('pass', scui.check_quality(r))

    def test_canvas_stale_and_unsafe_paths(self):
        op=example('canvas-operation')
        state={'canvas_version':'c1','code_revision':'abc123'}
        self.assertIn('precondition', scui.check_canvas(op,state))
        with self.assertRaisesRegex(scui.GateError, 'STALE'):
            scui.check_canvas(op,{'canvas_version':'c2','code_revision':'abc123'})
        op['allowed_paths']=['../secret.txt']
        with self.assertRaisesRegex(scui.GateError, 'Unsafe'):
            scui.check_canvas(op,state)
        op['allowed_paths']=['src/Hero.tsx']
        op['operation_type']='commit'
        with self.assertRaisesRegex(scui.GateError, 'approval'):
            scui.check_canvas(op,state)

    def test_status_and_decisions(self):
        ledger=(ROOT/'docs/DECISIONS-1-45.zh-CN.md').read_text('utf8')
        for i in range(1,46):
            self.assertIn(f'- {i} ',ledger)
        self.assertIn('43 UNDECIDED',ledger)

if __name__=='__main__': unittest.main()

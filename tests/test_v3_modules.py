"""Deterministic static tests for original Stephen Curry UI 3.0 tools.

These do not claim aesthetic quality or successful deployment in OpenCodex.
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import visual_metrics, design_guard, blind_jury, motion_evidence, experience_matrix
from PIL import Image


class MeasurementTest(unittest.TestCase):
    def test_image_metrics_and_diff(self):
        with tempfile.TemporaryDirectory() as d:
            a,b,diff=[Path(d)/x for x in ('a.png','b.png','diff.png')]
            Image.new('RGB',(20,20),(255,0,0)).save(a)
            Image.new('RGB',(20,20),(0,0,255)).save(b)
            s=visual_metrics.summarize(str(a))
            self.assertEqual(s['size'],[20,20])
            comparison=visual_metrics.compare(str(a),str(b),str(diff))
            self.assertTrue(comparison['comparable'])
            self.assertGreater(comparison['meanAbsoluteRGBDelta'],0)
            self.assertTrue(diff.is_file())
            Image.new('RGB',(30,20),(0,0,0)).save(b)
            self.assertFalse(visual_metrics.compare(str(a),str(b))['comparable'])


class ContractTest(unittest.TestCase):
    def test_css_token_drift(self):
        c={'cssVariables':{'--scui-bg':'#e8e3d9','--scui-accent':'#57553a'}}
        ok=design_guard.check_contract(c,{'test.css':':root{--scui-bg:#e8e3d9;--scui-accent:#57553a;}'})
        self.assertTrue(ok['passed'])
        bad=design_guard.check_contract(c,{'test.css':':root{--scui-bg: #fff; }'})
        self.assertFalse(bad['passed'])
        self.assertEqual({x['name']:x['status'] for x in bad['results']},
                         {'--scui-accent':'MISSING','--scui-bg':'MISMATCH'})


class JuryTest(unittest.TestCase):
    def test_privacy_pack_and_path_traversal(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);audit=root/'actual';audit.mkdir()
            Image.new('RGB',(15,15),(255,255,255)).save(audit/'one.png')
            (audit/'report.json').write_text(json.dumps({'url':'https://secret.example',
                'captures':[{'route':'/','viewport':'desktop','status':'PASS',
                             'screenshots':[str(audit/'one.png')]}]}),encoding='utf-8')
            result=blind_jury.prepare_pack(audit/'report.json',root/'blind')
            self.assertEqual(len(result['evidence']),1)
            self.assertTrue(list((root/'blind/frames').glob('*.png')))
            self.assertNotIn('secret.example',(root/'blind/evidence.json').read_text())
            outside=root/'private.png'
            Image.new('RGB',(20,20),(0,0,0)).save(outside)
            with self.assertRaises(ValueError):blind_jury.safe_image(outside,audit)


class MotionTest(unittest.TestCase):
    def test_frame_diagnostic_is_not_fake_fps(self):
        result=motion_evidence.report_frame_times([16.5,17.2,34.6,50.2,0,None])
        self.assertEqual(result['samples'],4)
        self.assertEqual(result['over33msFraction'],0.5)
        self.assertNotIn('fps',result)



class CoverageTest(unittest.TestCase):
    def test_require_manual_scene_review(self):
        p={'views':['desktop','mobile'],'routes':[{'path':'/','scenes':['intro','middle','footer'],'states':['hover','touch']}]}
        a={'captures':[{'route':'/','viewport':'desktop','status':'PASS','screenshots':['one.png'],'interaction_actions':[]}]}
        result=experience_matrix.summarize(p,a)
        self.assertEqual(len(result['rows']),2)
        self.assertEqual(result['rows'][0]['captureStatus'],'SCREENSHOTS_CAPTURED')
        self.assertEqual(result['rows'][0]['sceneReview'],'NEEDS_HUMAN_REVIEW')
        self.assertEqual(result['rows'][1]['captureStatus'],'NOT_CAPTURED')




if __name__=='__main__':unittest.main()

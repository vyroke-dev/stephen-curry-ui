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
import style_explorer, design_guard, blind_jury, motion_evidence, experience_matrix


class CreativeExplorerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((ROOT/'templates/directions.example.json').read_text(encoding='utf-8'))

    def test_three_real_distinct_directions(self):
        page=style_explorer.build_html(self.data)
        self.assertTrue(page.startswith('<!DOCTYPE html>'))
        self.assertIn('Material Kinetics',page)
        self.assertIn('role="tablist"',page)
        self.assertIn('prefers-reduced-motion:reduce',page)
        self.assertIn('replaceChildren',page)

    def test_reject_html_and_unsafe_css_inputs(self):
        bad=json.loads(json.dumps(self.data))
        bad['directions'][0]['palette']['background']='red;position:absolute'
        with self.assertRaises(ValueError):style_explorer.build_html(bad)
        bad=json.loads(json.dumps(self.data))
        bad['directions'][0]['id']='bad slug!'
        with self.assertRaises(ValueError):style_explorer.build_html(bad)

    def test_text_is_escaped_from_javascript_script_context(self):
        altered=json.loads(json.dumps(self.data))
        altered['directions'][0]['heroTitle']='</script><img src=x onerror=alert(1)>'
        page=style_explorer.build_html(altered)
        self.assertNotIn('</script><img',page)
        self.assertIn('\\u003c/script\\u003e',page)
        self.assertEqual(page.count('</script>'),1)


class MeasurementTest(unittest.TestCase):
    def test_image_metrics_and_diff(self):
        try:
            from PIL import Image
            import visual_metrics
        except ImportError:
            self.skipTest('Pillow is not installed')
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
        try:
            from PIL import Image
        except ImportError:
            self.skipTest('Pillow is not installed')
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

    @unittest.skipUnless(shutil.which('chromium') or shutil.which('google-chrome'),'Chromium not installed')
    def test_offline_motion_cli(self):
        import subprocess
        html=ROOT/'examples/creative-explorer.html'
        with tempfile.TemporaryDirectory() as d:
            result=subprocess.run([sys.executable,str(ROOT/'scripts/motion_evidence.py'),
                '--html-file',str(html),'--duration-ms','180','--frames','3','--out',d],
                capture_output=True,text=True,timeout=30)
            self.assertEqual(result.returncode,0, result.stderr)
            data=json.loads((Path(d)/'motion-report.json').read_text())
            self.assertEqual(len(data['frames']),3)
            self.assertTrue(Path(data['frames'][0]).is_file())
            self.assertIn('rafDiagnostic',data)


class CoverageTest(unittest.TestCase):
    def test_require_manual_scene_review(self):
        p={'views':['desktop','mobile'],'routes':[{'path':'/','scenes':['intro','middle','footer'],'states':['hover','touch']}]}
        a={'captures':[{'route':'/','viewport':'desktop','status':'PASS','screenshots':['one.png'],'interaction_actions':[]}]}
        result=experience_matrix.summarize(p,a)
        self.assertEqual(len(result['rows']),2)
        self.assertEqual(result['rows'][0]['captureStatus'],'SCREENSHOTS_CAPTURED')
        self.assertEqual(result['rows'][0]['sceneReview'],'NEEDS_HUMAN_REVIEW')
        self.assertEqual(result['rows'][1]['captureStatus'],'NOT_CAPTURED')


@unittest.skipUnless(shutil.which('chromium') or shutil.which('google-chrome'),'Chromium not installed')
class BrowserSmokeTest(unittest.TestCase):
    def test_design_explorer_actual_controls(self):
        try:from playwright.sync_api import sync_playwright
        except ImportError:self.skipTest('Playwright not installed')
        html=style_explorer.build_html(json.loads((ROOT/'templates/directions.example.json').read_text(encoding='utf-8')))
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=True, executable_path=shutil.which('chromium') or shutil.which('google-chrome'))
            try:
                page=browser.new_page(viewport={'width':1440,'height':900})
                errors=[]
                page.on('pageerror',lambda e: errors.append(str(e)))
                page.set_content(html,wait_until='load')
                self.assertIn('Space is a story',page.locator('#headline').inner_text())
                page.get_by_role('tab',name='02 · Material Kinetics').click()
                self.assertIn('Matter becomes',page.locator('#headline').text_content())
                page.get_by_role('button',name='Mobile').click()
                self.assertIn('phone',page.locator('#viewport').get_attribute('class'))
                page.get_by_role('button',name='Preview entry movement').click()
                self.assertIn('motion-pulse',page.locator('#viewport').get_attribute('class'))
                self.assertEqual(errors,[])
                with tempfile.TemporaryDirectory() as d:
                    screenshot=Path(d)/'explorer.png'
                    page.screenshot(path=str(screenshot))
                    self.assertGreater(screenshot.stat().st_size,1000)
            finally:browser.close()


if __name__=='__main__':unittest.main()

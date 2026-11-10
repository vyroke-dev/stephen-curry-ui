"""Live local fixture smoke test; verifies screenshot and basic browser coverage tool."""
import json
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


class ExperienceAuditTest(unittest.TestCase):
    def test_manifest_and_url_helpers(self):
        sys.path.insert(0, str(ROOT/'scripts'))
        import experience_audit as ea
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'actions.json'
            p.write_text(json.dumps({'routes':[{'path':'/','actions':[{'type':'click','selector':'button'}]}]}))
            data=ea.load_manifest(str(p))
            self.assertEqual(data['/'][0]['type'],'click')
            self.assertEqual(ea.resolve_url('http://localhost:3000','/work'),'http://localhost:3000/work')
            self.assertEqual(ea.safe_token('/work/abc'),'work-abc')

    def test_chromium_can_render_offline_content(self):
        try: 
            from playwright.sync_api import sync_playwright
        except ImportError: self.skipTest('Playwright missing')
        executable=shutil.which('chromium') or shutil.which('google-chrome')
        if not executable: self.skipTest('System Chromium missing')
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=True, executable_path=executable)
            try:
                page=browser.new_page()
                page.set_content('<!doctype html><title>Offline QA</title><main><h1>Test</h1><button>Go</button></main>')
                self.assertEqual(page.locator('h1').inner_text(), 'Test')
                self.assertGreater(len(page.screenshot()), 100)
            finally:browser.close()

    def test_browser_capture_on_local_fixture(self):
        try:
            import playwright
        except ImportError:
            self.skipTest("Playwright is not installed")
        if not shutil.which('chromium') and not shutil.which('google-chrome'):
            self.skipTest("No system Chromium for local test")
        with ThreadingHTTPServer(('127.0.0.1',0), partial(QuietHandler,directory=str(ROOT/'tests/fixtures'))) as server:
            t=threading.Thread(target=server.serve_forever,daemon=True)
            t.start()
            try:
                with tempfile.TemporaryDirectory() as tmp:
                    cmd=[sys.executable,str(ROOT/'scripts/experience_audit.py'),
                         '--url',f'http://127.0.0.1:{server.server_address[1]}',
                         '--paths','/sample.html','--views','desktop','--settle-ms','80','--out',tmp]
                    result=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=45)
                    report=json.loads((Path(tmp)/'report.json').read_text(encoding='utf-8'))
                    if (result.returncode == 2 and report['captures'][0].get('status') == 'BLOCKED' and 'ERR_BLOCKED_BY_ADMINISTRATOR' in report['captures'][0].get('error','')):
                        self.assertTrue((Path(tmp)/'report.md').is_file())
                        self.skipTest('Sandbox Chromium forbids navigating even to localhost; captures remain unverified')
                    self.assertEqual(result.returncode,0,f"STDOUT {result.stdout}\nSTDERR {result.stderr}")
                    self.assertEqual(len(report['captures']),1)
                    item=report['captures'][0]
                    self.assertEqual(item['status'],'PASS')
                    self.assertGreaterEqual(len(item['screenshots']),4)
                    self.assertEqual(item['structure']['h1Count'],1)
                    self.assertTrue((Path(tmp)/'report.md').is_file())
            finally:
                server.shutdown()
                t.join(timeout=3)


if __name__=='__main__':unittest.main()

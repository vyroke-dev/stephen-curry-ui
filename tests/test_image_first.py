import importlib.util
import json
import struct
import tempfile
import unittest
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('scui', ROOT/'tools/scui.py')
scui=importlib.util.module_from_spec(spec); spec.loader.exec_module(scui)


def png(color):
    # Fully generated test fixture images, never design deliverables.
    def block(tag, data):
        return struct.pack('!I',len(data))+tag+data+struct.pack('!I',zlib.crc32(tag+data)&0xffffffff)
    row=b'\x00'+bytes(color)
    return b'\x89PNG\r\n\x1a\n'+block(b'IHDR',struct.pack('!IIBBBBB',1,1,8,2,0,0,0))+block(b'IDAT',zlib.compress(row))+block(b'IEND',b'')


def make_fixture(tmp):
    data=json.loads((ROOT/'contracts/examples/concept-set.example.json').read_text())
    for i,c in enumerate(data['concepts'],1):
        gen=c['image_generation']; gen['tool_identifier']='fixture-test-tool'
        for typ,ref in [('desktop',gen['desktop_image_ref']),('mobile',gen['mobile_image_ref'])]:
            p=tmp/ref; p.parent.mkdir(exist_ok=True,parents=True)
            p.write_bytes(png((i*50,20 if typ=='desktop' else 80,30)))
        (tmp/gen['prompt_ref']).write_text('Fixture prompt: website UI concept')
        (tmp/gen['generation_record_ref']).write_text(json.dumps({'tool_identifier':'fixture-test-tool','generation_completed':True}))
    return data


class ImageFirstGates(unittest.TestCase):
    def test_verified_file_bytes_not_proof_of_actual_generator(self):
        with tempfile.TemporaryDirectory() as d:
            data=make_fixture(Path(d))
            self.assertIn('local image bytes',scui.check_concepts(data,'ds1',d))
    def test_reject_html_disguised_as_png(self):
        with tempfile.TemporaryDirectory() as d:
            data=make_fixture(Path(d))
            Path(d,data['concepts'][0]['image_generation']['desktop_image_ref']).write_text('<html>Fake mockup</html>')
            with self.assertRaisesRegex(scui.GateError,'not a matching image'):
                scui.check_concepts(data,'ds1',d)
    def test_reject_html_artifact_extension(self):
        with tempfile.TemporaryDirectory() as d:
            data=make_fixture(Path(d))
            data['concepts'][0]['image_generation']['desktop_image_ref']='evidence/mock.html'
            data['concepts'][0]['high_fidelity_artifacts'][0]='evidence/mock.html'
            with self.assertRaises(scui.GateError):scui.check_concepts(data,'ds1',d)
    def test_missing_generated_image_fails(self):
        with tempfile.TemporaryDirectory() as d:
            data=make_fixture(Path(d))
            Path(d,data['concepts'][1]['image_generation']['mobile_image_ref']).unlink()
            with self.assertRaisesRegex(scui.GateError,'evidence absent'):
                scui.check_concepts(data,'ds1',d)
    def test_missing_prompt_fails(self):
        with tempfile.TemporaryDirectory() as d:
            data=make_fixture(Path(d))
            Path(d,data['concepts'][0]['image_generation']['prompt_ref']).unlink()
            with self.assertRaisesRegex(scui.GateError,'evidence absent'):
                scui.check_concepts(data,'ds1',d)
    def test_path_escape_fails(self):
        with tempfile.TemporaryDirectory() as d:
            data=make_fixture(Path(d))
            data['concepts'][0]['image_generation']['desktop_image_ref']='../secret.png'
            data['concepts'][0]['high_fidelity_artifacts'][0]='../secret.png'
            with self.assertRaisesRegex(scui.GateError,'outside evidence root'):
                scui.check_concepts(data,'ds1',d)

if __name__=='__main__': unittest.main()

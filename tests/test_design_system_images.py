"""Image-only DS visual evidence gates. Synthetic bytes in tests are NOT generated design art."""
import copy
import importlib.util
import json
import struct
import tempfile
import unittest
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('scui', ROOT / 'tools' / 'scui.py')
scui = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scui)


def valid_png():
    def chunk(tag, data):
        return struct.pack('!I',len(data))+tag+data+struct.pack('!I',zlib.crc32(tag+data)&0xffffffff)
    return b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('!IIBBBBB',1,1,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(b'\x00\xff\x00\x00'))+chunk(b'IEND',b'')


def fixture(d):
    data=json.loads((ROOT/'contracts/examples/design-system-boards.example.json').read_text())
    data['status']='approved'
    data['approval_ref']='USER_EXPLICITLY_APPROVED_IN_TRUSTED_HOST_FIXTURE'
    for b in data['boards']:
        g=b['image_generation']
        g['tool_identifier']='fixture-synthetic-only-not-an-image-generation-tool'
        f=Path(d,g['image_ref']);f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(valid_png())
        Path(d,g['prompt_ref']).write_text('fixture-only prompt')
        Path(d,g['generation_record_ref']).write_text(json.dumps({'tool_identifier':g['tool_identifier'],'generation_completed':True}))
    return data


class DesignBoardEvidenceTest(unittest.TestCase):
    def test_seven_board_files_structurally_check(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertIn('Seven',scui.check_design_boards(fixture(d),'ds1',d,require_approved=True))

    def test_missing_board_type_fails(self):
        with tempfile.TemporaryDirectory() as d:
            data=fixture(d);data['boards'].pop()
            with self.assertRaises(scui.GateError):scui.check_design_boards(data,'ds1',d)

    def test_reused_image_file_fails(self):
        with tempfile.TemporaryDirectory() as d:
            data=fixture(d);data['boards'][0]['image_generation']['image_ref']=data['boards'][1]['image_generation']['image_ref']
            with self.assertRaisesRegex(scui.GateError,'distinct'):scui.check_design_boards(data,'ds1',d)

    def test_code_mockup_in_png_extension_fails(self):
        with tempfile.TemporaryDirectory() as d:
            data=fixture(d);Path(d,data['boards'][0]['image_generation']['image_ref']).write_text('<html>fake design</html>')
            with self.assertRaisesRegex(scui.GateError,'Not a matching raster'):scui.check_design_boards(data,'ds1',d)

    def test_png_magic_only_not_valid(self):
        with tempfile.TemporaryDirectory() as d:
            data=fixture(d);Path(d,data['boards'][0]['image_generation']['image_ref']).write_bytes(b'\x89PNG\r\n\x1a\n'+b'not a valid PNG')
            with self.assertRaisesRegex(scui.GateError,'Invalid or corrupt raster'):scui.check_design_boards(data,'ds1',d)

    def test_unapproved_blocks_combined_gate(self):
        with tempfile.TemporaryDirectory() as d:
            data=fixture(d);data['status']='awaiting_approval';data.pop('approval_ref')
            concepts=json.loads((ROOT/'contracts/examples/concept-set.example.json').read_text())
            with self.assertRaisesRegex(scui.GateError,'not approved'):scui.check_design_gates(data,concepts,'ds1',d)

    def test_path_traversal_fails(self):
        with tempfile.TemporaryDirectory() as d:
            data=fixture(d);data['boards'][0]['image_generation']['image_ref']='../outside.png'
            with self.assertRaises(scui.GateError):scui.check_design_boards(data,'ds1',d)

    def test_unmatched_version_fails(self):
        with tempfile.TemporaryDirectory() as d:
            data=fixture(d)
            with self.assertRaisesRegex(scui.GateError,'version mismatch'):scui.check_design_boards(data,'ds2',d)

    def test_prompt_record_required(self):
        with tempfile.TemporaryDirectory() as d:
            data=fixture(d);Path(d,data['boards'][0]['image_generation']['generation_record_ref']).unlink()
            with self.assertRaises(scui.GateError):scui.check_design_boards(data,'ds1',d)

    def test_placeholder_tool_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            data=fixture(d);data['boards'][0]['image_generation']['tool_identifier']='EXAMPLE_ONLY_fake'
            with self.assertRaisesRegex(scui.GateError,'Placeholder'):scui.check_design_boards(data,'ds1',d)

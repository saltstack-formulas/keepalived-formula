#!/usr/bin/python

import os, unittest
from jinja2 import Environment, FileSystemLoader

class TestKeepalivedConfiguration(unittest.TestCase):

    def setUp(self):
        self.t_dir = os.path.abspath(os.path.join(
            os.path.dirname(__file__),
            os.pardir,
            'keepalived',
            'templates'))
        self.t_conf = Environment(loader=FileSystemLoader(self.t_dir), 
            trim_blocks=True)

    def renderTest(self, data, result):
        holder = self.t_conf.get_template('test_config.jinja').render(testdata=data)
        output = repr(holder) + ' did not equal ' + repr(result)
        self.assertEqual(holder, result, output)

    def test_string(self):
        testdata = 'stuff'
        result = 'stuff\n'
        self.renderTest(testdata, result)

    def test_number(self):
        testdata = 3
        result = '3\n'
        self.renderTest(testdata, result)

    def test_null(self):
        testdata = None
        result = '\n'
        self.renderTest(testdata, result)

    def test_key_value_pair(self):
        testdata = {'flintstone': 'fred'}
        result = 'flintstone fred\n'
        self.renderTest(testdata, result)

    def test_key_array_pair(self):
        testdata = {'flintstone': ['fred', 'wilma', 'pebbles']}
        result = 'flintstone {\n  fred\n  wilma\n  pebbles\n}\n'
        self.renderTest(testdata, result)

    def test_key_hash_pair(self):
        testdata = {'friends': {'rubble': 'barney'}}
        result = 'friends {\n  rubble barney\n}\n'
        self.renderTest(testdata, result)

    def test_key_ordered_hashs(self):
        testdata = {'friends': {'fred': 'flintstone', 'barney': 'rubble', 'wilma': 'flintstone', 'betty': 'rubble'}}
        result = 'friends {\n  barney rubble\n  betty rubble\n  fred flintstone\n  wilma flintstone\n}\n'
        self.renderTest(testdata, result)

    def test_ordered_hashes(self):
        testdata = [{'fred': 'flintstone'}, {'wilma': 'flintstone'}, {'barney': 'rubble'}, {'betty': 'rubble'}]
        result = 'fred flintstone\nwilma flintstone\nbarney rubble\nbetty rubble\n'
        self.renderTest(testdata, result)

    def test_carryover(self):
        testdata = {'vrrp_script': {'gizmo': {'fred': 'flintstone', 'barney': 'rubble'}}}
        result = 'vrrp_script gizmo {\n  barney rubble\n  fred flintstone\n}\n'
        self.renderTest(testdata, result)

    def test_carryover_contains_arry(self):
        testdata = {'vrrp_script': {'gizmo': [{'fred': 'flintstone'}, {'barney': 'rubble'}]}}
        result = 'vrrp_script gizmo {\n  fred flintstone\n  barney rubble\n}\n'
        self.renderTest(testdata, result)

    def test_carrover_vrrp_instance(self):
        testdata = {'vrrp_instance': {'gizmo': {'fred': 'flintstone', 'barney': 'rubble'}}}
        result = 'vrrp_instance gizmo {\n  barney rubble\n  fred flintstone\n}\n'
        self.renderTest(testdata, result)

    def test_carryovers_in_an_array(self):
        testdata = [{'vrrp_script': {'gizmo': {'running': 'dumdums'}}}, {'vrrp_instance': {'dumdums': {'fred': 'flintstone'}}}]
        result = 'vrrp_script gizmo {\n  running dumdums\n}\nvrrp_instance dumdums {\n  fred flintstone\n}\n'
        self.renderTest(testdata, result)

    def test_carrover_vrrp_sync_group(self):
        testdata = {'vrrp_sync_group': {'gizmo': {'fred': 'flintstone', 'barney': 'rubble'}}}
        result = 'vrrp_sync_group gizmo {\n  barney rubble\n  fred flintstone\n}\n'
        self.renderTest(testdata, result)

    def test_carrover_virtual_server_group(self):
        testdata = {'virtual_server_group': {'gizmo': {'fred': 'flintstone', 'barney': 'rubble'}}}
        result = 'virtual_server_group gizmo {\n  barney rubble\n  fred flintstone\n}\n'
        self.renderTest(testdata, result)

    def test_carrover_virtual_server(self):
        testdata = {'virtual_server': {'gizmo': {'fred': 'flintstone', 'barney': 'rubble'}}}
        result = 'virtual_server gizmo {\n  barney rubble\n  fred flintstone\n}\n'
        self.renderTest(testdata, result)

    def test_carrover_real_server(self):
        testdata = {'real_server': {'gizmo': {'fred': 'flintstone', 'barney': 'rubble'}}}
        result = 'real_server gizmo {\n  barney rubble\n  fred flintstone\n}\n'
        self.renderTest(testdata, result)

if __name__ == '__main__':
    unittest.main()

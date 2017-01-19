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
        result = 'flintstone {\nfred\nwilma\npebbles\n}\n'
        self.renderTest(testdata, result)

    def test_key_hash_pair(self):
        testdata = {'friends': {'rubble': 'barney'}}
        result = 'friends {\nrubble barney\n}\n'
        self.renderTest(testdata, result)

    def test_key_ordered_hashs(self):
        testdata = {'friends': {'fred': 'flintstone', 'barney': 'rubble', 'wilma': 'flintstone', 'betty': 'rubble'}}
        result = 'friends {\nbarney rubble\nbetty rubble\nfred flintstone\nwilma flintstone\n}\n'
        self.renderTest(testdata, result)

    def test_ordered_hashes(self):
        testdata = [{'fred': 'flintstone'}, {'wilma': 'flintstone'}, {'barney': 'rubble'}, {'betty': 'rubble'}]
        result = 'fred flintstone\nwilma flintstone\nbarney rubble\nbetty rubble\n'
        self.renderTest(testdata, result)

if __name__ == '__main__':
    unittest.main()

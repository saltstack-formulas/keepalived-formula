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

    def _render(self, data):
        holder = self.t_conf.get_template('test_config.jinja').render(testdata=data)
        print(repr(holder))
        return holder

    def test_string(self):
        testdata = 'stuff'
        result = 'stuff\n'
        self.assertEqual(self._render(testdata), result,
                'A string should be returned with a line feed.')

    def test_number(self):
        testdata = 3
        result = '3\n'
        self.assertEqual(self._render(testdata), result,
                'A number should be returned with a line feed.')

    def test_null(self):
        testdata = None
        result = '\n'
        self.assertEqual(self._render(testdata), result,
                'A null should just return a line feed.')

if __name__ == '__main__':
    unittest.main()

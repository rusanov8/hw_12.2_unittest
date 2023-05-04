import unittest
from utils import dicts

class TestGetVal(unittest.TestCase):
    def test_get_val(self):
        self.assertEqual(dicts.get_val({1: 'sky', 2: 'pro', 3: 'python'}, 1), 'sky')
        self.assertEqual(dicts.get_val({'str': 1, 'int': 2, 'flt': 3}, 'flt'), 3)
        self.assertEqual(dicts.get_val({1: 'sky', 2: 'pro', 3: 'python'}, 3), 'python')
        self.assertEqual(dicts.get_val({1: 'sky', 2: 'pro', 3: 'python'}, 0), 'git')
        self.assertEqual(dicts.get_val({1: 'sky', 2: 'pro', 3: 'python'}, 'sky'), 'git')
        self.assertEqual(dicts.get_val({}, 1), 'git')
        self.assertEqual(dicts.get_val({1: 'sky', 2: 'pro', 3: 'python'}, 10), 'git')


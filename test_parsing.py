import unittest

from recursive_json_search import *
from recursive_yaml_search import *
from recursive_xml_search import *
from test_data import *




class json_search_test(unittest.TestCase):
    '''test module to test search function in `recursive_json_search.py`'''
    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([]!=json_search(key1,data))
    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([]==json_search(key2,data))
    def test_is_a_list(self):
        '''Should return a list'''
        self.assertIsInstance(json_search(key1,data),list)

class yaml_search_test(unittest.TestCase):
    '''test module to test search function in `recursive_json_search.py`'''
    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([]!=yaml_search(key1,data))
    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([]==yaml_search(key2,data))
    def test_is_a_list(self):
        '''Should return a list'''
        self.assertIsInstance(yaml_search(key1,data),list)

class xml_search_test(unittest.TestCase):
    '''test module to test search function in `recursive_json_search.py`'''
    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([]!=xml_search(key1,data))
    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([]==xml_search(key2,data))
    def test_is_a_list(self):
        '''Should return a list'''
        self.assertIsInstance(xml_search(key1,data),list)

if __name__ == '__main__':
    unittest.main()

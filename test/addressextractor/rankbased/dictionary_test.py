'''
Created on 04-02-2015

@author: mateusz
'''
import unittest
from src.addressextractor.rankbased.dictionary import Dictionary

class FileReaderStub:
    
    def __init__(self, lines):
        self.lines = lines
        
    def read_lines(self, filename):
        return self.lines 

class DictionaryTest(unittest.TestCase):

    def test_from_file(self):
        """ Test if dictionary properly formats strings read from file and discards empty strings """
        
        file_lines = ["LINE 1", " line 2  ", "\n\rline 3\t", ""]
        d = Dictionary.from_file("foo_bar.txt", FileReaderStub(file_lines))

        self.assertTrue("line 1" in d, "'line 1' not found in dictionary")
        self.assertTrue("line 2" in d, "'line 2' not found in dictionary")
        self.assertTrue("line 3" in d, "'line 3' not found in dictionary")
        self.assertTrue("" not in d, "Empty string should not have gotten into dictionary")

    def test_append(self):
        """" Test if dictionary properly formats provided strings and discards empty strings"""
        
        entries = ["LINE 1", " line 2  ", "\n\rline 3\t", ""]
        d = Dictionary()
        map(d.append, entries)
        
        self.assertTrue("line 1" in d, "'line 1' not found in dictionary")
        self.assertTrue("line 2" in d, "'line 2' not found in dictionary")
        self.assertTrue("line 3" in d, "'line 3' not found in dictionary")
        self.assertTrue("" not in d, "Empty string should not have gotten into dictionary")
        
    def test_iterator_interface(self):
        """ Test if dictionary provides iterator that goes over all contained elements """
        
        d = Dictionary()
        entries = ["1", "2", "3"]
        map(d.append, entries)
        for s in d:
            self.assertTrue(s in entries, "Alien element found in dictionary: '%s'" % s)
            entries.remove(s)
        self.assertEquals(len(entries), 0, "Dictionary iterator hasn't gone over all the elements")
           
    def test_len_interface(self):
        """ Test if len(dictionary) returns it's actual size """
        
        d = Dictionary()
        self.assertEqual(len(d), 0, "len(empty_dictionary) should return 0")
        
        entries = ["1", "2", "3"]
        map(d.append, entries) 
        self.assertEqual(len(d), 3, "len(3_elements_dictionary) should return 3")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
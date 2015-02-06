'''
Created on 6 lut 2015

@author: m.midor
'''
import unittest
from src.addressextractor.evaluator.test_sample import TestSample


class TestSampleTest(unittest.TestCase):


    def test_str_method(self):
        sample = TestSample()
        sample.date = None
        sample.sources = ["first_source", "second_source"]
        sample.expected_result = "result"
        
        s = str(sample).splitlines()
        self.assertEquals(s[0], "first_source")
        self.assertEquals(s[1], "second_source")
        self.assertEquals(s[2], "expected: result")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
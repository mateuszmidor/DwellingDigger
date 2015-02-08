'''
Created on 6 lut 2015

@author: m.midor
'''
import unittest
from src.addressextractor.evaluator.test_sample import TestSample


class TestSampleTest(unittest.TestCase):


    def test_unicode_method(self):
        sample = TestSample()
        sample.date = None
        sample.sources = [u"first_source", u"second_source"]
        sample.expected_result = u"result"
        
        s = unicode(sample).splitlines()
        self.assertEquals(s[0], u"first_source")
        self.assertEquals(s[1], u"second_source")
        self.assertEquals(s[2], u"expected: result")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
'''
Created on 6 lut 2015

@author: m.midor
'''
import unittest
from src.addressextractor.evaluator.test_samples import TestSamples


class FileReaderStub():
    @staticmethod
    def read_lines(filename):
        return ["# comment", "source=first_source", "source=second_source", "expected=result"]
    
class TestSamplesTest(unittest.TestCase):


    def test_from_file(self):
        samples = TestSamples.from_file("fake_file.txt", FileReaderStub)      
        self.assertEqual(len(samples), 1, "Should have read 1 test sample")
        
        sample = samples[0]
        self.assertEqual(len(sample.sources), 2, "Test sample should have list of 2 sources")
        self.assertEqual(sample.sources[0], "first_source")
        self.assertEqual(sample.sources[1], "second_source")
        self.assertEqual(sample.expected_result, "result")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
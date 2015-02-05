# -*- coding: utf-8 -*-

'''
Created on 5 lut 2015

@author: m.midor
'''
import unittest
from src.addressextractor.rankbased.dictionary import Dictionary
from src.addressextractor.rankbased.rank_based_extractor import RankBasedExtractor


class RankBasedExtractorTest(unittest.TestCase):


    def test_extract_street(self):
        """ Test extracts street name along with number """
        streets = Dictionary(["Wielicka"])
        extractor = RankBasedExtractor(streets)
        sources = ["Kraków, Podgórze, Wielicka 30"]
        result = extractor.extract(sources)
        expected = "Wielicka 30"
        
        self.assertEquals(result, expected, "Address extraction for '{0}' should have returned '{1}' but returned '{2}'".format(sources[0], expected, result))


    def test_extract_street_before_district(self):
        """ Test extractors uses the dictionaries in proper order """
        
        streets = Dictionary(["Wielicka"])
        districts = Dictionary(["Podgórze"])
        extractor = RankBasedExtractor(streets, districts)
        sources = ["Kraków, Podgórze, Wielicka 30"]
        result = extractor.extract(sources)
        expected = "Wielicka 30"
        
        self.assertEquals(result, expected, "Address extraction for '{0}' should have returned '{1}' but returned '{2}'".format(sources[0], expected, result))
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
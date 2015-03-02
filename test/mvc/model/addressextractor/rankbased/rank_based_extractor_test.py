# -*- coding: utf-8 -*-

'''
Created on 5 lut 2015

@author: m.midor
'''
import unittest
from src.mvc.model.addressextractor.rankbased.dictionary import Dictionary
from src.mvc.model.addressextractor.rankbased.rank_based_extractor import RankBasedExtractor
from src.mvc.model.addressextractor.rankbased.dictionary_entry import DictionaryEntry


class RankBasedExtractorTest(unittest.TestCase):


    def test_extract_street(self):
        """ Test extracts street name along with number """
        wielicka = DictionaryEntry(u"Wielicka", u"Wielicka", Dictionary.STREET)
        d = Dictionary([wielicka])
        extractor = RankBasedExtractor(d)
        sources = [u"Kraków, Podgórze, Wielicka 30"]
        result = extractor.extract(sources)
        expected = u"ul. Wielicka 30"
        
        self.assertEquals(result, expected, u"Address extraction for '{0}' should have returned '{1}' but returned '{2}'".format(sources[0], expected, result))


    def test_extract_street_before_district(self):
        """ Test extractors uses the dictionaries in proper order """
        
        d = Dictionary([DictionaryEntry(u"Wielicka", u"Wielicka", Dictionary.STREET), 
                        DictionaryEntry(u"Podgórze", u"Podgórze", Dictionary.DISTRICT)])
        extractor = RankBasedExtractor(d)
        sources = [u"Kraków, Podgórze, Wielicka 30"]
        result = extractor.extract(sources)
        expected = u"ul. Wielicka 30"
        
        self.assertEquals(result, expected, u"Address extraction for '{0}' should have returned '{1}' but returned '{2}'".format(sources[0], expected, result))
        
   
    def test_nowahuta_case(self):
        """ Test extractors uses the dictionaries in proper order """
        
        d = Dictionary([DictionaryEntry(u"Nowa", u"Nowa", Dictionary.STREET), 
                        DictionaryEntry(u"Nowa Huta", u"Nowa Huta", Dictionary.DISTRICT)])
        d.sort_longest_first()
        
        extractor = RankBasedExtractor(d)
        sources = [u"Kraków, Podgórze, Nowa Huta"]
        result = extractor.extract(sources)
        expected = u"Nowa Huta"
        
        self.assertEquals(result, expected, u"Address extraction for '{0}' should have returned '{1}' but returned '{2}'".format(sources[0], expected, result))
        
             
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
# -*- coding: utf-8 -*-

'''
Created on 5 lut 2015

@author: m.midor
'''
import unittest
from src.mvc.model.addressextractor.rankbased.dictionary import Dictionary
from src.mvc.model.addressextractor.rankbased.surnamenator import Surnamenator
from src.mvc.model.addressextractor.rankbased.dictionary_entry import DictionaryEntry


class SurnamenatorTest(unittest.TestCase):

    def __dictionary_has_entry(self, dictionary, entry_name):
        for entry in dictionary:
            if entry.name == entry_name:
                return True
            
        return False

    def test_surnamenate_dictionary(self):
        d = Dictionary([DictionaryEntry("Balona", "Balona", 0), 
                        DictionaryEntry("Andrzeja Damiana Drzazgi", "Andrzeja Damiana Drzazgi", 0), 
                        DictionaryEntry("Michała Sochy", "Michała Sochy", 0), 
                        DictionaryEntry("Pawła Wesołego-Miłosia", "Pawła Wesołego-Miłosia", 0)])
        
        Surnamenator.surnamenate_dictionary(d)
        
        self.assertTrue(self.__dictionary_has_entry(d, "balona"), "Surnamesation for 'Balona' failed")
        self.assertTrue(self.__dictionary_has_entry(d, "drzazgi"), "Surnamesation for 'Andrzeja Damiana Drzazgi' failed")
        self.assertTrue(self.__dictionary_has_entry(d, "sochy"), "Surnamesation for 'Michała Sochy' failed")
        self.assertTrue(self.__dictionary_has_entry(d, "miłosia"), "Surnamesation for 'Pawła Wesołego-Miłosia' failed")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
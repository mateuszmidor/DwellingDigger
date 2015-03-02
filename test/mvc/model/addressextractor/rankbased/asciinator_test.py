# -*- coding: utf-8 -*-

'''
Created on 5 lut 2015

@author: m.midor
'''
import unittest
from src.mvc.model.addressextractor.rankbased.dictionary import Dictionary
from src.mvc.model.addressextractor.rankbased.asciinator import Asciinator
from src.mvc.model.addressextractor.rankbased.dictionary_entry import DictionaryEntry


class AsciinatorTest(unittest.TestCase):


    def __dictionary_has_entry(self, dictionary, name, original_form, address_type):
        for e in dictionary:
            if e.name == name and e.original_form == original_form and e.address_type == address_type:
                return True
            
        return False
    
    
    def test_asciinate_dictionary(self):
        STREET = Dictionary.STREET
        entries = [DictionaryEntry(u"górska", u"górska", STREET), 
                   DictionaryEntry(u"czyżyny", u"czyżyny", STREET), 
                   DictionaryEntry(u"nowosądecka", u"nowosądecka", STREET), 
                   DictionaryEntry(u"prądnik", u"prądnik", STREET)]
        d = Dictionary(entries)
        Asciinator.asciinate_dictionary(d)
        
        self.assertTrue(self.__dictionary_has_entry(d, u"gorska", u"górska", STREET), 
                        "Asciination for 'górska' failed")
        
        self.assertTrue(self.__dictionary_has_entry(d, u"czyzyny", u"czyżyny", STREET), 
                        "Asciination for 'czyżyny' failed")
        
        self.assertTrue(self.__dictionary_has_entry(d, u"nowosadecka", u"nowosądecka", STREET),
                        "Asciination for 'nowosądecka' failed")
        
        self.assertTrue(self.__dictionary_has_entry(d, u"pradnik", u"prądnik", STREET),
                        "Asciination for 'prądnik' failed")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

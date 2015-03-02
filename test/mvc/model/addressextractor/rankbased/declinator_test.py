# -*- coding: utf-8 -*-

'''
Created on 5 lut 2015

@author: m.midor
'''
import unittest
from src.mvc.model.addressextractor.rankbased.dictionary import Dictionary
from src.mvc.model.addressextractor.rankbased.declinator import Declinator
from src.mvc.model.addressextractor.rankbased.dictionary_entry import DictionaryEntry


class DeclinatorTest(unittest.TestCase):


    def __dictionary_has_entry(self, dictionary, name, original_form, address_type):
        for e in dictionary:
            if e.name == name and e.original_form == original_form and e.address_type == address_type:
                return True
            
        return False


    def test_declinate_dictionary(self):
        STREET = Dictionary.STREET
        entries = [DictionaryEntry("krakowska", "krakowska", STREET),
                   DictionaryEntry("tyniecka", "tyniecka", STREET),
                   DictionaryEntry("czyżyny", "czyżyny", STREET),
                   DictionaryEntry("sloneczne", "sloneczne", STREET),
                   DictionaryEntry("andersa", "andersa", STREET)]
        
        d = Dictionary(entries)
        Declinator.declinate_dictionary(d)
    
        self.assertTrue(self.__dictionary_has_entry(d, "krakowskiej", "krakowska", STREET), 
                        "Declination for 'krakowska' not found in dictionary")
        
        self.assertTrue(self.__dictionary_has_entry(d, "tynieckiej", "tyniecka", STREET), 
                        "Declination for 'tyniecka' not found in dictionary")
        
        self.assertTrue(self.__dictionary_has_entry(d, "czyżynach", "czyżyny", STREET),
                        "Declination for 'czyżyny' not found in dictionary")
        
        self.assertTrue(self.__dictionary_has_entry(d, "slonecznym", "sloneczne", STREET),
                        "Declination for 'sloneczne' not found in dictionary")
        
        self.assertTrue(self.__dictionary_has_entry(d, "andersa", "andersa", STREET), 
                        "Entry 'andersa' lost from dictionary during declination")
    
        self.assertEqual(len(d), 9, "After declination, dictionary should have 9 elements, not %d" % len(d))
    
    
    def test_undeclinate(self):
        self.assertEqual(Declinator.undeclinate("krakowskiej"), "krakowska", "Undeclination for 'skiej' failed")
        self.assertEqual(Declinator.undeclinate("tynieckiej"), "tyniecka", "Undeclination for 'ckiej' failed")
        self.assertEqual(Declinator.undeclinate("czyżynach"), "czyżyny", "Undeclination for 'nach' failed")
        self.assertEqual(Declinator.undeclinate("slonecznym"), "sloneczne", "Undeclination for 'cznym' failed")


    def test_undeclinate_with_number(self):
        self.assertEqual(Declinator.undeclinate("krakowskiej 12"), "krakowska 12", "Undeclination for 'skiej' failed")
        self.assertEqual(Declinator.undeclinate("tynieckiej 9"), "tyniecka 9", "Undeclination for 'ckiej' failed")
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
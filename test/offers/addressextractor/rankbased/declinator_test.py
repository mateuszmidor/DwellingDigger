# -*- coding: utf-8 -*-

'''
Created on 5 lut 2015

@author: m.midor
'''
import unittest
from src.offers.addressextractor.rankbased.dictionary import Dictionary
from src.offers.addressextractor.rankbased.declinator import Declinator


class DeclinatorTest(unittest.TestCase):


    def test_declinate_dictionary(self):
        d = Dictionary(["krakowska", "tyniecka", "czyżyny", "sloneczne", "andersa"])
        Declinator.declinate_dictionary(d)
    
        self.assertTrue("krakowskiej" in d, "Declination for 'krakowska' not found in dictionary")
        self.assertTrue("tynieckiej" in d, "Declination for 'tyniecka' not found in dictionary")
        self.assertTrue("czyżynach" in d, "Declination for 'czyżyny' not found in dictionary")
        self.assertTrue("slonecznym" in d, "Declination for 'sloneczne' not found in dictionary")
        self.assertTrue("andersa" in d, "Entry 'andersa' lost from dictionary during declination")
    
    
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
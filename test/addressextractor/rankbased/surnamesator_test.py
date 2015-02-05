# -*- coding: utf-8 -*-

'''
Created on 5 lut 2015

@author: m.midor
'''
import unittest
from src.addressextractor.rankbased.dictionary import Dictionary
from src.addressextractor.rankbased.surnamesator import Surnamesator


class SurnamesatorTest(unittest.TestCase):


    def test_surnamesate_dictionary(self):
        d = Dictionary(["Balona", "Andrzeja Damiana Drzazgi", "Michała Sochy", "Pawła Wesołego-Miłosia"])
        Surnamesator.surnamesate_dictionary(d)
        
        self.assertTrue("balona" in d, "Surnamesation for 'Balona' failed")
        self.assertTrue("drzazgi" in d, "Surnamesation for 'Andrzeja Damiana Drzazgi' failed")
        self.assertTrue("sochy" in d, "Surnamesation for 'Michała Sochy' failed")
        self.assertTrue("miłosia" in d, "Surnamesation for 'Pawła Wesołego-Miłosia' failed")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
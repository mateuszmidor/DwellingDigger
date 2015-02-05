# -*- coding: utf-8 -*-

'''
Created on 5 lut 2015

@author: m.midor
'''
import unittest
from src.addressextractor.rankbased.asciinator import Asciinator
from src.addressextractor.rankbased.dictionary import Dictionary


class AsciinatorTest(unittest.TestCase):


    def test_asciinate_dictionary(self):
        d = Dictionary([u"górska", u"czyżyny", u"nowosądecka", u"prądnik"])
        Asciinator.asciinate_dictionary(d)
        
        self.assertTrue("gorska" in d, "Asciisation for 'górska' failed")
        self.assertTrue("czyzyny" in d, "Asciisation for 'czyżyny' failed")
        self.assertTrue("nowosadecka" in d, "Asciisation for 'nowosądecka' failed")
        self.assertTrue("pradnik" in d, "Asciisation for 'prądnik' failed")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

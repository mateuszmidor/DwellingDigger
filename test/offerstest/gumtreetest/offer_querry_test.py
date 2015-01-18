'''
Created on 18-01-2015

@author: mateusz
'''
import unittest
from offers.gumtree.offer_querry import OfferQuerry


class OfferQuerryTest(unittest.TestCase):


    def testRaisesOnEmptyCity(self):
        try:
            OfferQuerry.compose(city="")
            self.fail("Empty 'city' param should cause ValueError exception")
        except ValueError:
            # valid case
            pass
        except:
            self.fail("Empty 'city' param should cause ValueError exception but caused some other exception")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
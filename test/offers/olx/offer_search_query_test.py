'''
Created on 22-01-2015

@author: mateusz
'''
import unittest
from src.offers.olx.offer_search_query import OfferSearchQuery


class OfferSearchQueryTest(unittest.TestCase):

    def test_raises_on_empty_city(self):
        try:
            query = OfferSearchQuery.compose(city="")  # @UnusedVariable
            self.fail("Empty 'city' param should cause ValueError exception")
        except ValueError:
            # valid case
            pass
        except:
            self.fail("Empty 'city' param should cause ValueError exception but caused some other exception")
           

    def test_all_parameters_supplied(self):
        EXPECTED_QUERY_STRING = 'http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-kurdwan%C3%B3w/?search%5Bfilter_float_price%3Afrom%5D=800&search%5Bfilter_float_price%3Ato%5D=1600&search%5Bfilter_enum_rooms%5D%5B0%5D=two&search%5Bfilter_float_m%3Afrom%5D=40&search%5Bfilter_float_m%3Ato%5D=70'
        query = OfferSearchQuery.compose(city="krakow",
                                         whereabouts="kurdwanów",
                                         num_rooms="2",
                                         min_price="800",
                                         max_price="1600",
                                         min_area="40",
                                         max_area="70")
        self.assertEquals(EXPECTED_QUERY_STRING, query.as_url_string())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
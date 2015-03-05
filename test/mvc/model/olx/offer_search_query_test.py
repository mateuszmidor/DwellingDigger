# -*- coding: UTF-8 -*-

'''
Created on 22-01-2015

@author: mateusz
'''
import unittest
from src.mvc.model.olx.offer_search_query import OfferSearchQuery
from mock import Mock


class OfferSearchQueryTest(unittest.TestCase):

    def test_raises_on_empty_city(self):
        try:
            query = OfferSearchQuery.from_key_values(city="")  # @UnusedVariable
            self.fail("Empty 'city' param should cause ValueError exception")
        except ValueError:
            # valid case
            pass
           
           
    def test_city_supplied(self):
        EXPECTED_QUERY_STRING = 'http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow?'
        query = OfferSearchQuery.from_key_values(city="krakow")
        self.assertEquals(EXPECTED_QUERY_STRING, query.as_url_string())
        
        
    def test_city_whereabouts_supplied(self):
        EXPECTED_QUERY_STRING = 'http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-kurdwan%C3%B3w?'
        query = OfferSearchQuery.from_key_values(city="krakow", whereabouts="kurdwanów")
        self.assertEquals(EXPECTED_QUERY_STRING, query.as_url_string())
        
        
    def test_all_parameters_supplied(self):
        EXPECTED_QUERY_STRING = 'http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-kurdwan%C3%B3w?search%5Bfilter_float_price%3Afrom%5D=800&search%5Bfilter_float_price%3Ato%5D=1600&search%5Bfilter_enum_rooms%5D%5B0%5D=two&search%5Bfilter_float_m%3Afrom%5D=40&search%5Bfilter_float_m%3Ato%5D=70'
        query = OfferSearchQuery.from_key_values(city="krakow",
                                                 whereabouts="kurdwanów",
                                                 num_rooms="2",
                                                 min_price="800",
                                                 max_price="1600",
                                                 min_area="40",
                                                 max_area="70")
        self.assertEquals(EXPECTED_QUERY_STRING, query.as_url_string())


    def test_from_offer_params(self):
        EXPECTED_QUERY_STRING = 'http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-kurdwan%C3%B3w?search%5Bfilter_float_price%3Afrom%5D=800&search%5Bfilter_float_price%3Ato%5D=1600&search%5Bfilter_enum_rooms%5D%5B0%5D=two&search%5Bfilter_float_m%3Afrom%5D=40&search%5Bfilter_float_m%3Ato%5D=70'
        
        params = Mock()
        params.get_city = Mock(return_value = "krakow")
        params.get_whereabouts = Mock(return_value = "kurdwanów")
        params.get_num_rooms = Mock(return_value = 2)
        params.get_min_price = Mock(return_value = 800)
        params.get_max_price = Mock(return_value = 1600)
        params.get_min_area = Mock(return_value = 40)
        params.get_max_area = Mock(return_value = 70)
        
        query = OfferSearchQuery.from_offer_params(params)
        self.assertEquals(EXPECTED_QUERY_STRING, query.as_url_string()) 
        
           
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
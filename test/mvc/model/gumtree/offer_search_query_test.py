'''
Created on 18-01-2015

@author: mateusz
'''
import unittest
from src.mvc.model.gumtree.offer_search_query import OfferSearchQuery

class OfferParamsStub():
    """ 
    This guy is used to test OfferSearchQuery.from_offer_params 
    Could be nicely replaced with Mock but using __getattr__ is more fun :)
    """
    
    def __getattr__(self, name):
        METHOD_RESULT = {"get_city"         : "Krakow",
                        "get_whereabouts"   : "Nowa Huta",
                        "get_num_rooms"     : 1,
                        "get_min_price"     : 500,
                        "get_max_price"     : 1000,
                        "get_min_area"      : 30,
                        "get_max_area"      : 70}
        
        def get():
            """ Closure? """
            return METHOD_RESULT[name]
        
        return get
    
    
class OfferSearchQuerryTest(unittest.TestCase):

    def test_raises_on_empty_city(self):
        try:
            query = OfferSearchQuery.from_key_values(city="")  # @UnusedVariable
            self.fail("Empty 'city' param should cause ValueError exception")
        except ValueError:
            # valid case
            pass
        except:
            self.fail("Empty 'city' param should cause ValueError exception but caused some other exception")
           
            
    def test_from_key_values(self):
        EXPECTED_QUERY_STRING = 'http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/Krakow/Nowa%20Huta/c9008l3200208?A_AreaInMeters_max=70&A_AreaInMeters_min=30&A_ForRentBy=ownr&A_NumberRooms=10&AdType=2&isSearchForm=true&maxPrice=1000&maxPriceBackend=200000&minPrice=500&minPriceBackend=100000'
        query = OfferSearchQuery.from_key_values(city="Krakow",
                                                 whereabouts="Nowa Huta",
                                                 num_rooms="1",
                                                 min_price="500",
                                                 max_price="1000",
                                                 min_area="30",
                                                 max_area="70")
        self.assertEquals(EXPECTED_QUERY_STRING, query.as_url_string())
        
        
    def test_from_offer_params(self):
        EXPECTED_QUERY_STRING = 'http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/Krakow/Nowa%20Huta/c9008l3200208?A_AreaInMeters_max=70&A_AreaInMeters_min=30&A_ForRentBy=ownr&A_NumberRooms=10&AdType=2&isSearchForm=true&maxPrice=1000&maxPriceBackend=200000&minPrice=500&minPriceBackend=100000'
        params = OfferParamsStub()
        query = OfferSearchQuery.from_offer_params(params)
        self.assertEquals(EXPECTED_QUERY_STRING, query.as_url_string())
        
                
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

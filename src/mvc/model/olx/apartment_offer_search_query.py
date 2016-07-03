'''
Created on Jun 29, 2016

@author: mateusz
'''

from src.mvc.model.olx.offer_search_query import OfferSearchQuery
class ApartmentOfferSearchQuery(OfferSearchQuery):
    '''
    Build an OLX search query for apartments
    '''
#     OLX offer query url example:
#     http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-kurdwan%C3%B3w/?
#     search%5Bfilter_float_price%3Afrom%5D=800&
#     search%5Bfilter_float_price%3Ato%5D=1600&
#     search%5Bfilter_enum_rooms%5D%5B0%5D=two&
#     search%5Bfilter_float_m%3Afrom%5D=40&
#     search%5Bfilter_float_m%3Ato%5D=70
  
    
    def __init__(self, *args):
        self.OLX_QUERY_BASE_URL = u'http://olx.pl/nieruchomosci/mieszkania/wynajem'
        super(ApartmentOfferSearchQuery, self).__init__(*args)        
# -*- coding: UTF-8 -*-

'''
Created on 29-06-2016

@author: mateusz
'''
from src.mvc.model.olx.offer_search_query import OfferSearchQuery
class SingleroomOfferSearchQuery(OfferSearchQuery):
    '''
    Build an OLX search query for single rooms
    '''
#     OLX offer query url example:
#     http://olx.pl/nieruchomosci/stancje-pokoje/krakow/q-ruczaj/?
#     search%5Bfilter_float_price%3Afrom%5D=500&
#     search%5Bfilter_float_price%3Ato%5D=1000

  
    def __init__(self, city, whereabouts, num_rooms, min_price, max_price, min_area, max_area):
        self.OLX_QUERY_BASE_URL = u'http://olx.pl/nieruchomosci/stancje-pokoje'
        num_rooms = u"" # no num_rooms filter here
        super(SingleroomOfferSearchQuery, self).__init__(city, 
                                                         whereabouts, 
                                                         num_rooms, 
                                                         min_price, 
                                                         max_price, 
                                                         min_area, 
                                                         max_area)    
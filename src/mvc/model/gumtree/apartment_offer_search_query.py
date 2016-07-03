'''
Created on Jun 29, 2016

@author: mateusz
'''

from src.mvc.model.gumtree.offer_search_query import OfferSearchQuery
class ApartmentOfferSearchQuery(OfferSearchQuery):
    '''
    Build a Gumtre search query for apartments
    '''
    
    def __init__(self, *args):
        self.TEMPLATE = u'http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/{_city}/{_whereabouts}v1c9008l3200208{_has_whereabouts_mark}p{_page}?nr={_num_rooms}&pr={_min_price},{_max_price}'
        super(ApartmentOfferSearchQuery, self).__init__(*args)  
'''
Created on Jun 29, 2016

@author: mateusz
'''

from src.mvc.model.gumtree.offer_search_query import OfferSearchQuery
class SingleroomOfferSearchQuery(OfferSearchQuery):
    '''
    Build a Gumtre search query for single rooms
    '''
    
    def __init__(self, city, whereabouts, num_rooms, min_price, max_price, min_area, max_area):
        self.TEMPLATE = u'http://www.gumtree.pl/s-pokoje-do-wynajecia/{_city}/{_whereabouts}v1c9000l3200208{_has_whereabouts_mark}p{_page}?pr={_min_price},{_max_price}'
        num_rooms = u"" # no num_rooms filter here
        super(SingleroomOfferSearchQuery, self).__init__(city, 
                                                         whereabouts, 
                                                         num_rooms, 
                                                         min_price, 
                                                         max_price, 
                                                         min_area, 
                                                         max_area)  
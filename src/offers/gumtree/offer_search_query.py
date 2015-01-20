'''
Created on 18-01-2015

@author: mateusz
'''
import urllib

class OfferSearchQuery(object):
    """
    Offer search query. 
    Search criteria: desired city, whereabouts, num rooms, min and max price, min and max square meters.
    Can be turned into url and used to query Gumtree for offers matching the criteria.
    """

    """Request url template for querying Gumtree for offers"""
    __TEMPLATE = 'http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/{_city}/{_whereabouts}c9008l3200208?A_AreaInMeters_max={_max_area}&A_AreaInMeters_min={_min_area}&A_ForRentBy=ownr&A_NumberRooms={_num_rooms}&AdType=2&isSearchForm=true&maxPrice={_max_price}&maxPriceBackend=200000&minPrice={_min_price}&minPriceBackend=100000'
    
    @classmethod
    def compose(cls, city="", whereabouts="", num_rooms="", min_price="", max_price="", min_area="", max_area=""):
        return cls(city, whereabouts, num_rooms, min_price, max_price, min_area, max_area)
    
    def __init__(self, city, whereabouts, num_rooms, min_price, max_price, min_area, max_area):
        # city is obligatory
        if (not city):
            raise ValueError("City is obligatory to compose a valid offer search query")
        
        self.city = city
        self.whereabouts = whereabouts # eg. "Kazimierz"
        self.num_rooms = num_rooms
        self.min_price = min_price
        self.max_price = max_price
        self.min_area = min_area # square meters
        self.max_area = max_area
        
    def __str__(self):
        return self.as_url_string()
    
    def as_url_string(self):
        whereabouts = self.whereabouts
        if (whereabouts != ""):
            whereabouts = urllib.quote(whereabouts)  # escape special characters like spaces etc
            whereabouts += "/"  # whereabouts is http request address section; so must be followed by "/"
            
        # gumtree encodes one room as '10'. stupid, ha?
        numRooms = self.num_rooms
        if (numRooms == "1"):
            numRooms = "10" 
        
        query = OfferSearchQuery.__TEMPLATE.format(_city=self.city, _whereabouts=whereabouts, _num_rooms=numRooms,
                                                _min_price=self.min_price, _max_price=self.max_price, _min_area=self.min_area,
                                                _max_area=self.max_area)
        
        return query
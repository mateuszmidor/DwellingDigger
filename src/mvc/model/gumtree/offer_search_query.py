'''
Created on 18-01-2015

@author: mateusz
'''
import urllib

class OfferSearchQuery(object):
    """
    Offer search query. 
    Search criteria: desired __city, __whereabouts, num rooms, min and max price, min and max square meters.
    Can be turned into url and used to query Gumtree for offers matching the criteria.
    """

    """Request url template for querying Gumtree for offers"""
    __TEMPLATE = 'http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/{_city}/{_whereabouts}c9008l3200208?A_AreaInMeters_max={_max_area}&A_AreaInMeters_min={_min_area}&A_ForRentBy=ownr&A_NumberRooms={_num_rooms}&AdType=2&isSearchForm=true&maxPrice={_max_price}&maxPriceBackend=200000&minPrice={_min_price}&minPriceBackend=100000'
    
    
    @classmethod
    def from_key_values(cls, city="", whereabouts="", num_rooms="", min_price="", max_price="", min_area="", max_area=""):
        """ Use this method to build OfferSearchQuery from key-value pairs """
        return cls(city, whereabouts, num_rooms, min_price, max_price, min_area, max_area)
    
    
    @classmethod
    def from_offer_params(cls, params):
        """ Use this method to build OfferSearchQuery from OfferParams """
        def str_or_empty(v):
            return str(v) if v else ""
        
        city = params.get_city()
        whereabouts = str_or_empty(params.get_whereabouts())
        num_rooms = str_or_empty(params.get_num_rooms())
        min_price = str_or_empty(params.get_min_price())
        max_price = str_or_empty(params.get_max_price())
        min_area = str_or_empty(params.get_min_area())
        max_area = str_or_empty(params.get_max_area())
    
        return cls(city, whereabouts, num_rooms, min_price, max_price, min_area, max_area)
    
    
    def __init__(self, city, whereabouts, num_rooms, min_price, max_price, min_area, max_area):
        # __city is obligatory
        if not city:
            raise ValueError("City is obligatory to from_key_values a valid offer search query")
        
        self.__city = city
        self.__whereabouts = whereabouts # eg. "Kazimierz"
        self.__num_rooms = num_rooms
        self.__min_price = min_price
        self.__max_price = max_price
        self.__min_area = min_area # square meters
        self.__max_area = max_area
        
        
    def __str__(self):
        return self.as_url_string()
    
    
    def as_url_string(self):
        whereabouts = self.__whereabouts
        if whereabouts != "":
            whereabouts = urllib.quote(whereabouts)  # escape special characters like spaces etc
            whereabouts += "/"  # __whereabouts is http request address section; so must be followed by "/"
            
        city = urllib.quote(self.__city) # escape special characters like spaces etc
        
        # gumtree encodes one room as '10'. stupid, ha?
        num_rooms = self.__num_rooms
        if num_rooms == "1":
            num_rooms = "10" 
        
        query = OfferSearchQuery.__TEMPLATE.format(_city=city, _whereabouts=whereabouts, _num_rooms=num_rooms,
                                                _min_price=self.__min_price, _max_price=self.__max_price, _min_area=self.__min_area,
                                                _max_area=self.__max_area)
        
        return query
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
    __TEMPLATE = u'http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/{_city}/{_whereabouts}c9008l3200208?A_AreaInMeters_max={_max_area}&A_AreaInMeters_min={_min_area}&A_ForRentBy=ownr&A_NumberRooms={_num_rooms}&AdType=2&isSearchForm=true&maxPrice={_max_price}&maxPriceBackend=200000&minPrice={_min_price}&minPriceBackend=100000'
    
    
    @classmethod
    def from_key_values(cls, city=u"", whereabouts=u"", num_rooms=u"", min_price=u"", max_price=u"", min_area=u"", max_area=u""):
        """ Use this method to build OfferSearchQuery from key-value pairs """
        return cls(city, whereabouts, num_rooms, min_price, max_price, min_area, max_area)
    
    
    @classmethod
    def from_offer_params(cls, params):
        """ Use this method to build OfferSearchQuery from OfferParams """
        def unicode_or_empty(v):
            return unicode(v) if v else u""
        
        city = unicode_or_empty(params.get_city())
        whereabouts = unicode_or_empty(params.get_whereabouts())
        num_rooms = unicode_or_empty(params.get_num_rooms())
        min_price = unicode_or_empty(params.get_min_price())
        max_price = unicode_or_empty(params.get_max_price())
        min_area = unicode_or_empty(params.get_min_area())
        max_area = unicode_or_empty(params.get_max_area())
    
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
        if whereabouts:
            whereabouts = whereabouts.encode('UTF8') # urllib.quote doesnt accept unicode so - encode
            whereabouts = urllib.quote(whereabouts)  # escape special characters like spaces etc
            whereabouts += u"/"  # __whereabouts is http request address section; so must be followed by "/"
            
        city = urllib.quote(self.__city) # escape special characters like spaces etc
        
        # gumtree encodes one room as '10'. stupid, ha?
        num_rooms = self.__num_rooms
        if num_rooms == u"1":
            num_rooms = u"10" 
        
        query = OfferSearchQuery.__TEMPLATE.format(_city=city, _whereabouts=whereabouts, _num_rooms=num_rooms,
                                                _min_price=self.__min_price, _max_price=self.__max_price, _min_area=self.__min_area,
                                                _max_area=self.__max_area)
        
        return query.encode('UTF8')
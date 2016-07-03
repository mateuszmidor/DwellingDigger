'''
Created on 18-01-2015

@author: mateusz
'''
import urllib

# note: the min area/max area constraints are no longer supported by gumtree api
class OfferSearchQuery(object):
    """
    Offer search query. 
    Search criteria: desired __city, __whereabouts, num rooms, min and max price, min and max square meters.
    Can be turned into url and used to query Gumtree for offers matching the criteria.
    """


    @classmethod
    def from_key_values(cls, city=u"", 
                        whereabouts=u"", 
                        num_rooms=u"", 
                        min_price=u"", 
                        max_price=u"", 
                        min_area=u"", 
                        max_area=u""):
        """ Use this method to build OfferSearchQuery from key-value pairs """
        return cls(city, whereabouts, num_rooms, min_price, max_price, min_area, max_area)
    
    
    @classmethod
    def from_offer_params(cls, params):
        """ Use this method to build OfferSearchQuery from OfferParams """
        def unicode_or_empty(string):
            return unicode(string) if string else u""
        
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
        
        # wherebous can be eg. "Kazimierz"
        self.__whereabouts = whereabouts 
        self.__num_rooms = num_rooms
        
        self.__min_price = min_price
        self.__max_price = max_price
        
        # area unit is square meters
        self.__min_area = min_area 
        self.__max_area = max_area
        
        
    def __str__(self):
        return self.as_url_string()
    
    
    def as_url_string(self):
        whereabouts = self.__whereabouts
        
        # no whereabouts by default
        whereabouts_mark = u""
        if whereabouts:
            # urllib.quote doesnt accept unicode so - encode
            whereabouts = whereabouts.encode('UTF8') 
            
            # escape special characters like spaces etc
            whereabouts = urllib.quote(whereabouts) 
            
            # __whereabouts is http request address section; so must be followed by "/"
            whereabouts += u"/"  
            
            # set has whereabouts
            whereabouts_mark = u"q0"
            
        # escape special characters like spaces etc
        city = urllib.quote(self.__city) 
        
        # gumtree encodes one room as '10'. stupid, ha?
        num_rooms = self.__num_rooms
        if num_rooms == u"1":
            num_rooms = u"10" 
        
        # TEMPLATE to be provided by descendant class
        query = self.TEMPLATE.format(_city=city, 
                                       _whereabouts=whereabouts, 
                                       _num_rooms=num_rooms,
                                       _min_price=self.__min_price, 
                                       _max_price=self.__max_price, 
                                       _min_area=self.__min_area,
                                       _max_area=self.__max_area,
                                       _has_whereabouts_mark=whereabouts_mark,
                                       _page=u"{_page}") # dont touch _page placeholder
        
        return query.encode('UTF8')
    
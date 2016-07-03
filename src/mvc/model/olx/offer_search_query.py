# -*- coding: UTF-8 -*-

'''
Created on 22-01-2015

@author: mateusz
'''
import urllib
import unicodedata
from _collections import defaultdict

class OfferSearchQuery(object):
    """
    Offer search query. 
    Search criteria: desired city, whereabouts, num rooms, min and max price, min and max square meters.
    Can be turned into url and used to query OLX for offers matching the criteria.
    """
    
 



    @classmethod
    def from_key_values(cls, 
                        city=u"", 
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
            """ Convert object to unicode string or empty string if None """
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
        
        # Make sure city and whereabouts dont contain national characters as OLX doesnt support them
        self.__city = self.__asciinate(city)
        
        # wherebouts is eg. "Kazimierz"
        self.__whereabouts = self.__asciinate(whereabouts) 
        self.__num_rooms = num_rooms
        
        # price is string 
        self.__min_price = min_price
        self.__max_price = max_price
        
        # area unit is square meters
        self.__min_area = min_area
        self.__max_area = max_area
        
    
    @staticmethod
    def __asciinate(address):
        almost_ascii = u"".join(c for c in unicodedata.normalize('NFD', address) if unicodedata.category(c) != 'Mn')
        # ł, Ł need special handling
        almost_ascii = almost_ascii.replace(u"ł", u"l")
        ascii = almost_ascii.replace(u"Ł", u"L")
        return ascii
                
                
    def __str__(self):
        return self.as_url_string()
    
    
    @staticmethod
    def __add_city(url, city):
        """
        Adds CITY section to base url:
        http://olx.pl/nieruchomosci/mieszkania/wynajem/CITY
        """
        
        # escape special characters in city name, like spaces etc.
        return url + u"/" + urllib.quote(city) 
    
    
    @staticmethod
    def __add_whereabouts(url, whereabouts):
        """
        Adds optional WHEREABOUTS section to url:
        http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-WHEREABOUTS/
        """
        
        # whereabouts is not a must
        if whereabouts == u"": 
            return url 
        
        # escape special characters in wherebouts, like spaces etc
        whereabouts = urllib.quote(whereabouts)  
        return url + u"/q-" + whereabouts 
        
        
    @staticmethod
    def __add_arg(args, template, new_arg):
        """ Method for building http request argument list """
        
        # Nothing to add
        if new_arg == u"":
            return args
        
        # If we already have some arguments - add ampersand separator
        if args != u"": 
            args += u"&"
        
        # Add new argument to argument list and return
        return args + template.format(new_arg)
    
    
    def __add_num_rooms(self, args, num_rooms):
        if not num_rooms:
            return args
        
        template = u"search%5Bfilter_enum_rooms%5D%5B0%5D={0}"
        
        # "four" in OLX exactly means "four or more" , so lets fall back to "four" if no other number matches
        room_numbers = defaultdict(lambda s : u"four")
        room_numbers[u""]   = u""
        room_numbers[u"1"]  = u"one"
        room_numbers[u"2"]  = u"two"
        room_numbers[u"3"]  = u"three"
        
        num_rooms_str = room_numbers[num_rooms]
            
        return self.__add_arg(args, template, num_rooms_str)
    
    
    def __add_min_price(self, args, min_price):
        template = u"search%5Bfilter_float_price%3Afrom%5D={0}"
        return self.__add_arg(args, template, min_price)
    
    
    def __add_max_price(self, args, max_price):
        template = u"search%5Bfilter_float_price%3Ato%5D={0}"
        return self.__add_arg(args, template, max_price)
    
    
    def __add_min_area(self, args, min_area):
        template = u"search%5Bfilter_float_m%3Afrom%5D={0}"
        return self.__add_arg(args, template, min_area)    
    
    
    def __add_max_area(self, args, max_area):
        template = u"search%5Bfilter_float_m%3Ato%5D={0}"
        return self.__add_arg(args, template, max_area)    
    
    def __add_distance(self, args, dist):
        template = u"search[dist]={0}"
        return self.__add_arg(args, template, dist) 
    
    def as_url_string(self):
        
        # Build the base url
        url = self.OLX_QUERY_BASE_URL # OLX_QUERY_BASE_URL to be provided by descendant class
        url = self.__add_city(url, self.__city)
        url = self.__add_whereabouts(url, self.__whereabouts)
            
        # Build the argument list
        args = ""
        args = self.__add_distance(args, "5") # 5km
        args = self.__add_min_price(args, self.__min_price)
        args = self.__add_max_price(args, self.__max_price)
        args = self.__add_num_rooms(args, self.__num_rooms)
        args = self.__add_min_area(args, self.__min_area)
        args = self.__add_max_area(args, self.__max_area)
        
        # Build the full url from base url and argument list
        query = url + u"?" + args
        return query.encode('UTF8')
        
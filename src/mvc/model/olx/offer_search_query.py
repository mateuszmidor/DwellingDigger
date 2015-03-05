# -*- coding: UTF-8 -*-

'''
Created on 22-01-2015

@author: mateusz
'''
import urllib

class OfferSearchQuery(object):
    """
    Offer search query. 
    Search criteria: desired city, whereabouts, num rooms, min and max price, min and max square meters.
    Can be turned into url and used to query OLX for offers matching the criteria.
    """
    
    "OLX offer query url example:"
    'http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-kurdwan%C3%B3w/?search%5Bfilter_float_price%3Afrom%5D=800&search%5Bfilter_float_price%3Ato%5D=1600&search%5Bfilter_enum_rooms%5D%5B0%5D=two&search%5Bfilter_float_m%3Afrom%5D=40&search%5Bfilter_float_m%3Ato%5D=70'
    __OLX_QUERY_BASE_URL = 'http://olx.pl/nieruchomosci/mieszkania/wynajem'


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
    
    def __add_city(self, url, city):
        """
        Adds CITY section to base url:
        http://olx.pl/nieruchomosci/mieszkania/wynajem/CITY
        """
        
        return url + "/" + urllib.quote(city) # escape special characters like spaces etc.
    
    def __add_whereabouts(self, url, whereabouts):
        """
        Adds optional WHEREABOUTS section to url:
        http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-WHEREABOUTS/
        """
        
        if whereabouts == "": 
            return url # __whereabouts is not a must
        
        whereabouts = urllib.quote(whereabouts)  # escape special characters like spaces etc
        return url + "/q-" + whereabouts 
        
    def __add_arg(self, args, template, new_arg):
        """ Method for building http request argument list """
        
        # Nothing to add
        if new_arg == "":
            return args
        
        # If we already have some arguments - add ampersand separator
        if args != "": 
            args += "&"
        
        # Add new argument to argument list and return
        return args + template.format(new_arg)
    
    def __add_num_rooms(self, args, num_rooms):
        TEMPLATE = "search%5Bfilter_enum_rooms%5D%5B0%5D={0}"
        ROOM_NUMBERS = {""  : "",
                        "1" : "one",
                        "2" : "two",
                        "3" : "three",
                        "4" : "four"}
        num_rooms_str = ROOM_NUMBERS[num_rooms]
        return self.__add_arg(args, TEMPLATE, num_rooms_str)
    
    def __add_min_price(self, args, min_price):
        TEMPLATE = "search%5Bfilter_float_price%3Afrom%5D={0}"
        return self.__add_arg(args, TEMPLATE, min_price)
    
    def __add_max_price(self, args, max_price):
        TEMPLATE = "search%5Bfilter_float_price%3Ato%5D={0}"
        return self.__add_arg(args, TEMPLATE, max_price)
    
    def __add_min_area(self, args, min_area):
        TEMPLATE = "search%5Bfilter_float_m%3Afrom%5D={0}"
        return self.__add_arg(args, TEMPLATE, min_area)    
    
    def __add_max_area(self, args, max_area):
        TEMPLATE = "search%5Bfilter_float_m%3Ato%5D={0}"
        return self.__add_arg(args, TEMPLATE, max_area)    
    
    def as_url_string(self):
        
        # Build the base url
        url = OfferSearchQuery.__OLX_QUERY_BASE_URL
        url = self.__add_city(url, self.__city)
        url = self.__add_whereabouts(url, self.__whereabouts)
            
        # Build the argument list
        args = ""
        args = self.__add_min_price(args, self.__min_price)
        args = self.__add_max_price(args, self.__max_price)
        args = self.__add_num_rooms(args, self.__num_rooms)
        args = self.__add_min_area(args, self.__min_area)
        args = self.__add_max_area(args, self.__max_area)
        
        # Build the full url from base url and argument list
        full_url = url + "?" + args
        
        return full_url
        
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
    __OLX_QUERY_BASE_URL = 'http://olx.pl/nieruchomosci/mieszkania/wynajem/'

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
    
    def __add_city(self, url, city):
        return url + city + "/"
    
    def __add_whereabouts(self, url, whereabouts):
        if (whereabouts == ""): return url # whereabouts is not a must
        whereabouts = urllib.quote(whereabouts)  # escape special characters like spaces etc
        return url + "q-" + whereabouts + "/" # eg. http://olx.pl/nieruchomosci/mieszkania/wynajem/krakow/q-kurdwanów/
        
    def __add_arg(self, args, template, new_arg):
        """ Method for building http request argument list """
        
        # Nothing to add
        if (new_arg == ""):
            return args
        
        # If we already have some arguments - add ampersand separator
        if (args != ""): 
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
        url = self.__add_city(url, self.city)
        url = self.__add_whereabouts(url, self.whereabouts)
            
        # Build the argument list
        args = ""
        args = self.__add_min_price(args, self.min_price)
        args = self.__add_max_price(args, self.max_price)
        args = self.__add_num_rooms(args, self.num_rooms)
        args = self.__add_min_area(args, self.min_area)
        args = self.__add_max_area(args, self.max_area)
        
        # Build the full url from base url and argument list
        full_url = url
        if (args != ""): 
            full_url += "?" + args
        
        return full_url
        
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

    """Request url template for querying OLX for offers"""
    __TEMPLATE = 'http://olx.pl/nieruchomosci/mieszkania/wynajem/{_city}/{_whereabouts}?search%5Bfilter_float_price%3Afrom%5D={_min_price}&search%5Bfilter_float_price%3Ato%5D={_max_price}&search%5Bfilter_enum_rooms%5D%5B0%5D={_num_rooms}&search%5Bfilter_float_m%3Afrom%5D={_min_area}&search%5Bfilter_float_m%3Ato%5D={_max_area}'
    
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
        
    def __add_num_rooms(self, args, num_rooms):
        if (num_rooms == ""): return args 
        if (args != ""): args += "&"
        # encode room number
        ROOM_NUMBERS = {"1" : "one",
                        "2" : "two",
                        "3" : "three",
                        "4" : "four"}
        num_rooms_string = ROOM_NUMBERS[num_rooms]
        return args + "search[filter_enum_rooms][0]={0}".format(num_rooms_string)
    
    def __add_min_price(self, args, min_price):
        if (min_price == ""): return args
        if (args != ""): args += "&"
        return args + "search[filter_float_price%3Afrom]={0}".format(min_price)
    
    def __add_max_price(self, args, max_price):
        if (max_price == ""): return args
        if (args != ""): args += "&"
        return args + "search[filter_float_price%3Ato]={0}".format(max_price)
    
    def __add_min_area(self, args, min_area):
        if (min_area == ""): return args
        if (args != ""): args += "&"
        return args + "search[filter_float_m%3Afrom]={0}".format(min_area)
    
    def __add_max_area(self, args, max_area):
        if (max_area == ""): return args
        if (args != ""): args += "&"
        return args + "search[filter_float_m%3Ato]={0}".format(max_area)
    
    
    def as_url_string(self):
        url = OfferSearchQuery.__OLX_QUERY_BASE_URL
        url = self.__add_city(url, self.city)
        url = self.__add_whereabouts(url, self.whereabouts)
            
        args = ""
        args = self.__add_num_rooms(args, self.num_rooms)
        args = self.__add_min_price(args, self.min_price)
        args = self.__add_max_price(args, self.max_price)
        args = self.__add_min_area(args, self.min_area)
        args = self.__add_max_area(args, self.max_area)
        
        
        full_url = url
        if (args != ""): full_url += "?" + args
        
        return full_url
        
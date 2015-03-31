'''
Created on 05-03-2015

@author: mateusz
'''

class OfferParams(object):
    '''
    This class represents params criteria provided by user to look for offers
    '''
        
        
    @staticmethod
    def from_key_values(city=None,
                        whereabouts=None, 
                        num_rooms=None, 
                        min_price=None, 
                        max_price=None, 
                        min_area=None, 
                        max_area=None):
        """ Use this method to build OfferParams from key-value pairs """
        
        return OfferParams(city, whereabouts, num_rooms, min_price, max_price, min_area, max_area)
    
    
    @staticmethod
    def from_cgi_fieldstorage(cgi_field_storage, default_city=""):
        """ Use this method to build OfferParams from cgi.FieldStorage """
        
        s = cgi_field_storage
        return OfferParams(s.getvalue("city", default_city),
                           s.getvalue("whereabouts", None),
                           s.getvalue("num_rooms", None),
                           s.getvalue("min_price", None),
                           s.getvalue("max_price", None),
                           s.getvalue("min_area", None),
                           s.getvalue("max_area", None))


    def __init__(self,
                 city,
                 whereabouts, 
                 num_rooms, 
                 min_price, 
                 max_price, 
                 min_area, 
                 max_area):
        
        if not city:
            raise ValueError("City is obligatory")
        
        if self.__invalid_range(min_price, max_price):
            raise ValueError("max_price < min_price")

        if self.__invalid_range(min_area, max_area):
            raise ValueError("max_area < min_area")
        
        self.__city = city
        self.__whereabouts = whereabouts
        self.__num_rooms = num_rooms
        self.__min_price = min_price
        self.__max_price = max_price
        self.__min_area = min_area
        self.__max_area = max_area
        
    
    def __invalid_range(self, minimum, maximum):
        if not minimum:
            return False
        
        if not maximum:
            return False
        
        if maximum < minimum:
            return True
        
        
    def get_city(self):
        return self.__city
    
    
    def get_whereabouts(self):
        return self.__whereabouts
    

    def get_num_rooms(self):
        return self.__num_rooms
    
    
    def get_min_price(self):
        return self.__min_price
    
    
    def get_max_price(self):
        return self.__max_price
    
    
    def get_min_area(self):
        return self.__min_area
    
    
    def get_max_area(self):
        return self.__max_area 
    
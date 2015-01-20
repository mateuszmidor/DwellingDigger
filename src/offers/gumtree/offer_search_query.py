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
    __TEMPLATE = 'http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/{_city}/{_whereabouts}c9008l3200208?A_AreaInMeters_max={_maxArea}&A_AreaInMeters_min={_minArea}&A_ForRentBy=ownr&A_NumberRooms={_numRooms}&AdType=2&isSearchForm=true&maxPrice={_maxPrice}&maxPriceBackend=200000&minPrice={_minPrice}&minPriceBackend=100000'
    
    @staticmethod
    def compose(city="", whereabouts="", numRooms="", minPrice="", maxPrice="", minArea="", maxArea=""):
        return OfferSearchQuery(city, whereabouts, numRooms, minPrice, maxPrice, minArea, maxArea)
    
    def __init__(self, city, whereabouts, numRooms, minPrice, maxPrice, minArea, maxArea):
        # city is obligatory
        if (not city):
            raise ValueError("City is obligatory to compose a valid offer search query")
        
        self.city = city
        self.whereabouts = whereabouts # eg. "Kazimierz"
        self.numRooms = numRooms
        self.minPrice = minPrice
        self.maxPrice = maxPrice
        self.minArea = minArea # square meters
        self.maxArea = maxArea
        
    def __str__(self):
        return self.as_url_string()
    
    def as_url_string(self):
        whereabouts = self.whereabouts
        if (whereabouts != ""):
            whereabouts = urllib.quote(whereabouts)  # escape special characters like spaces etc
            whereabouts += "/"  # whereabouts is http request address section; so must be followed by "/"
            
        # gumtree encodes one room as '10'. stupid, ha?
        numRooms = self.numRooms
        if (numRooms == "1"):
            numRooms = "10" 
        
        query = OfferSearchQuery.__TEMPLATE.format(_city=self.city, _whereabouts=whereabouts, _numRooms=numRooms,
                                                _minPrice=self.minPrice, _maxPrice=self.maxPrice, _minArea=self.minArea,
                                                _maxArea=self.maxArea)
        
        return query
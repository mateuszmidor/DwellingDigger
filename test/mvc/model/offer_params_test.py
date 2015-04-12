'''
Created on 05-03-2015

@author: mateusz
'''
import unittest
from src.mvc.model.offer_params import OfferParams

class CgiFieldstorageStub:
    """ This guy is used to test OfferParams.from_cgi_fieldstorage """
    
    @staticmethod
    def getvalue(name, defvalue):
        FIELDS = {"city"        : "Krakow",
                  "whereabouts" : "Krowodrza", 
                  "num_rooms"   : 4, 
                  "min_price"   : 950, 
                  "max_price"   : 1450, 
                  "min_area"    : 45, 
                  "max_area"    : 75}
        
        return FIELDS[name] if name in FIELDS else defvalue
    
    
class OfferParamsTest(unittest.TestCase):

    def test_raises_on_empty_city1(self):
        """ Tests empty city as empty string """
        try:
            params = OfferParams.from_key_values(city="")  # @UnusedVariable
            self.fail("Empty 'city' param should cause ValueError exception")
        except ValueError:
            # valid case
            pass


    def test_raises_on_empty_city2(self):
        """ Tests empty city as None """
        try:
            params = OfferParams.from_key_values(city=None)  # @UnusedVariable
            self.fail("Empty 'city' param should cause ValueError exception")
        except ValueError:
            # valid case
            pass
      
      
    def test_raises_on_price_error(self):
        """ Test if raises exception when min_price > max_price """
        try:
            params = OfferParams.from_key_values(city="Krakow", min_price = 1000, max_price = 950)  # @UnusedVariable
            self.fail("min_price = 1000 and max_price = 950 should cause ValueError exception")
        except ValueError:
            # valid case
            pass
        
        
    def test_raises_on_area_error(self):
        """ Test if raises exception when min_area > max_area """
        try:
            params = OfferParams.from_key_values(city="Krakow", min_area = 75, max_area = 45)  # @UnusedVariable
            self.fail("min_area = 75 and max_area = 45 should cause ValueError exception")
        except ValueError:
            # valid case
            pass
        
        
    def test_from_key_values(self):
        params = OfferParams.from_key_values(city=u"Krakow",
                                             whereabouts=u"Krowodrza", 
                                             num_rooms=4, 
                                             min_price=950, 
                                             max_price=1450, 
                                             min_area=45, 
                                             max_area=75)
        
        self.assertTrue(isinstance(params.get_city(), unicode), 
                        "'city' should be stored as unicode")
        
        self.assertEqual(params.get_city(), u"Krakow", 
                         "city should be Krakow but is %s" % params.get_city())
                            
        self.assertTrue(isinstance(params.get_whereabouts(), unicode), 
                        "'whereabouts' should be stored as unicode")
                            
        self.assertEqual(params.get_whereabouts(), u"Krowodrza", 
                         "whereabouts should be Krowodrza but is %s" % params.get_whereabouts())
        
        self.assertEqual(params.get_num_rooms(), 4, 
                         "num_rooms should be 4 but is %d" % params.get_num_rooms())
        
        self.assertEqual(params.get_min_price(), 950, 
                         "min_price should be 950 but is %d" % params.get_min_price())   
             
        self.assertEqual(params.get_max_price(), 1450, 
                         "max_price should be 1450 but is %d" % params.get_max_price()) 
              
        self.assertEqual(params.get_min_area(), 45, 
                         "min_area should be 45 but is %d" % params.get_min_area()) 
               
        self.assertEqual(params.get_max_area(), 75, 
                         "max_area should be 75 but is %d" % params.get_max_area())        
                   
  
    def test_from_cgi_fieldstorage(self):
        params = OfferParams.from_cgi_fieldstorage(CgiFieldstorageStub)
        
        self.assertTrue(isinstance(params.get_city(), unicode), 
                        "'city' should be stored as unicode")
        
        self.assertEqual(params.get_city(), u"Krakow", 
                         "city should be Krakow but is %s" % params.get_city())
                            
        self.assertTrue(isinstance(params.get_whereabouts(), unicode), 
                        "'whereabouts' should be stored as unicode")
                                    
        self.assertEqual(params.get_whereabouts(), u"Krowodrza", 
                         "whereabouts should be Krowodrza but is %s" % params.get_whereabouts())
        
        self.assertEqual(params.get_num_rooms(), 4, 
                         "num_rooms should be 4 but is %d" % params.get_num_rooms())
        
        self.assertEqual(params.get_min_price(), 950, 
                         "min_price should be 950 but is %d" % params.get_min_price())   
             
        self.assertEqual(params.get_max_price(), 1450, 
                         "max_price should be 1450 but is %d" % params.get_max_price()) 
              
        self.assertEqual(params.get_min_area(), 45, 
                         "min_area should be 45 but is %d" % params.get_min_area()) 
               
        self.assertEqual(params.get_max_area(), 75, 
                         "max_area should be 75 but is %d" % params.get_max_area())                    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
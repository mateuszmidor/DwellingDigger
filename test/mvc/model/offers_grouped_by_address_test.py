'''
Created on 28 kwi 2015

@author: m.midor
'''
import unittest
from datetime import datetime
from src.mvc.model.offers_grouped_by_address import OffersGroupedByAddress


class OffersGroupedByAddressTest(unittest.TestCase):
    OFFER1 = {"address" :   "Wielicka, Krakow, Polska",
              "address_section" :   "Wielicka",
              "title"   :   "OFFER1",
              "date"    :   datetime(2000, 1, 1),
              "price"   :   "1000 ZL",
              "url"     :   "www.OFFER1.pl",
              "image_url"   :   "www.OFFER1_img.pl",
              "summary" :   "Tanie mieszkanie na wielickiej",
              "latlong" :   [1, 1],
              "area"    :   30,
              "num_rooms"   : 2}
    
    OFFER2 = {"address" :   "Kurdwanow, Krakow, Polska",
              "address_section" :   "osiedle Kurdwanow",
              "title"   :   "OFFER2",
              "date"    :   datetime(2000, 1, 2),
              "price"   :   "2000 ZL",
              "url"     :   "www.OFFER2.pl",
              "image_url" :   "www.OFFER2_img.pl",
              "summary" :   "Niezbyt tanie mieszkanie, kurdwanow",
              "latlong" :   [2, 2],
              "area"    :   50,
              "num_rooms"   : 3}        

    OFFER3 = {"address" :   "Wielicka, Krakow, Polska",
              "address_section" :   "ul wielicka",
              "title"   :   "OFFER3",
              "date"    :   datetime(2000, 1, 3),
              "price"   :   "3000 ZL",
              "url"     :   "www.OFFER3.pl",
              "image_url" :   "www.OFFER3_img.pl",
              "summary" :   "Absolutnie nietanie mieszkanie, kurdwanow",
              "latlong":   [1, 1],
              "area"    : 70,
              "num_rooms"   : 4}  

    

    def get_group_by_address(self, groups, address):
        ''' Helper function to retrieve group af offers that has given address assigned '''
        return next((g for g in groups if g["address"] == address), None)

  
    def get_offer_by_url(self, offers, url):
        ''' Helper function to retrieve group af offers that has given address assigned '''
        return next((o for o in offers if o["url"] == url), None)
        

    def test_get_groups(self):
        ''' 
        Check if the method returns offers properly grouped by address.
        There should be two groups returned:
        -group for Wielicka, Krakow, Polska. containing 2 offers
        -group for Kurdwanow, Krakow, Polska. containing 1 offer
        '''
        
        # get the offer groups
        groups = OffersGroupedByAddress.as_list([OffersGroupedByAddressTest.OFFER1, 
                                                 OffersGroupedByAddressTest.OFFER2, 
                                                 OffersGroupedByAddressTest.OFFER3])
                                                     
        # we have 3 offers, 2 share same address so - 2 groups should be returned
        self.assertEqual(2, len(groups), 
                         "There should be 2 offer groups returned but was %d" % len(groups))
        
        
        ################################################## 
        #                                                                 
        # investigate the "Wielicka, Krakow, Polska" group
        #
        ##################################################
        # get the group at "Wielicka, Krakow, Polska"
        group1 = self.get_group_by_address(groups, "Wielicka, Krakow, Polska")
        self.assertTrue(group1 != None, 
                        "'Wielicka, Krakow, Polska' should be in the returned groups")
                             
        # check longitude                      
        self.assertEqual(1, group1["longitude"], 
                         "longitude for 'Wielicka, Krakow, Polska' should be '1' but was '%d'" % group1["longitude"]) 
        
        # check latitude                      
        self.assertEqual(1, group1["latitude"], 
                         "latitude for 'Wielicka, Krakow, Polska' should be '1' but was '%d'" % group1["latitude"]) 
        
        # check there are two offers in this group as two offers share "Wielicka, Krakow, Polska" address
        self.assertEqual(2, len(group1["offers"]),
                                "There should be 2 offers in 'Wielicka, Krakow, Polska' group, but there is %d" % len(group1["offers"]))
        ################################################## 
        #                                                                 
        # investigate OFFER1 within the group
        #
        ################################################## 
        offer1 = self.get_offer_by_url(group1["offers"], "www.OFFER1.pl") 
        self.assertTrue(offer1 != None, 
                        "offer 'www.OFFER1.pl' should be present in 'Wielicka, Krakow, Polska' group")
        
        # check image url
        self.assertEqual("www.OFFER1_img.pl", offer1["image_url"], 
                         "image_url should be 'www.OFFER1_img.pl' for 'www.OFFER1.pl' offer but was '%s'" % offer1["image_url"])
                
        # check address section string (the address that was found on the offer web page in designated field)
        self.assertEqual("Wielicka", offer1["address_section"], 
                         "address_section should be 'Wielicka' for 'www.OFFER1.pl' offer")
        
        # check the offer title
        self.assertEqual("OFFER1", offer1["title"], 
                         "title should be 'OFFER1' for 'www.OFFER1.pl' offer")        
        
        # check the offer date
        self.assertEqual(datetime(2000, 1, 1), offer1["date"], 
                         "date should be 2000/1/1 for 'www.OFFER1.pl' offer") 
        
        # check the offer price
        self.assertEqual("1000 ZL", offer1["price"], 
                         "price should be '1000 ZL' for 'www.OFFER1.pl' offer")           
   
        # check the offer summary
        self.assertEqual("Tanie mieszkanie na wielickiej", offer1["summary"], 
                         "summary should be 'Tanie mieszkanie na wielickiej' for 'www.OFFER1.pl' offer") 
           
        # check num rooms
        self.assertEqual(2, offer1["num_rooms"], 
                         "num_rooms should be 2 for 'www.OFFER1.pl' offer")    
                   
        # check square meters
        self.assertEqual(30, offer1["area"], 
                         "area should be 30 for 'www.OFFER1.pl' offer")                    
        ################################################## 
        #                                                                 
        # investigate OFFER3 within the group
        #
        ##################################################   
        offer3 = self.get_offer_by_url(group1["offers"], "www.OFFER3.pl") 
        self.assertTrue(offer3 != None, 
                        "offer 'www.OFFER3.pl' should be present in 'Wielicka, Krakow, Polska' group")
        
        # check image url
        self.assertEqual("www.OFFER3_img.pl", offer3["image_url"], 
                         "image_url should be 'www.OFFER3_img.pl' for 'www.OFFER3.pl' offer but was '%s'" % offer3["image_url"])
                
        # check address section string (the address that was found on the offer web page in designated field)
        self.assertEqual("ul wielicka", offer3["address_section"], 
                         "address_section should be 'ul wielicka' for 'www.OFFER3.pl' offer")    
        
        # check the offer title
        self.assertEqual("OFFER3", offer3["title"], 
                         "title should be 'OFFER3' for 'www.OFFER3.pl' offer")    
        
        # check the offer date
        self.assertEqual(datetime(2000, 1, 3), offer3["date"], 
                         "date should be 2000/1/3 for 'www.OFFER3.pl' offer")   
        
        # check the offer price
        self.assertEqual("3000 ZL", offer3["price"], 
                         "price should be '3000 ZL' for 'www.OFFER3.pl' offer")     
        
        # check the offer summary
        self.assertEqual("Absolutnie nietanie mieszkanie, kurdwanow", offer3["summary"], 
                         "summary should be 'Absolutnie nietanie mieszkanie, kurdwanow' for 'www.OFFER3.pl' offer")                             
                      
        # check num rooms
        self.assertEqual(4, offer3["num_rooms"], 
                         "num_rooms should be 4 for 'www.OFFER3.pl' offer")    
                   
        # check square meters
        self.assertEqual(70, offer3["area"], 
                         "area should be 70 for 'www.OFFER3.pl' offer")                        
           
        ################################################## 
        #                                                                 
        # investigate the "Kurdwanow, Krakow, Polska" group
        #
        ##################################################
        # get the group at "Kurdwanow, Krakow, Polska"
        group2 = self.get_group_by_address(groups, "Kurdwanow, Krakow, Polska")
        self.assertTrue(group2 != None, 
                        "'Kurdwanow, Krakow, Polska' should be in the returned groups")                      


        # check longitude                      
        self.assertEqual(2, group2["longitude"], 
                         "longitude for 'Kurdwanow, Krakow, Polska' should be '1' but was '%d'" % group2["longitude"]) 
        
        # check latitude                      
        self.assertEqual(2, group2["latitude"], 
                         "latitude for 'Kurdwanow, Krakow, Polska' should be '2' but was '%d'" % group2["latitude"]) 
        
        # check there is one offer in this group as only one offer is at "Kurdwanow, Krakow, Polska" address
        self.assertEqual(1, len(group2["offers"]),
                                "There should be 1 offer in 'Kurdwanow, Krakow, Polska' group, but there is %d" % len(group2["offers"]))                                   
                                  
               
        ################################################## 
        #                                                                 
        # investigate OFFER2 within the group
        #
        ##################################################   
        offer2 = self.get_offer_by_url(group2["offers"], "www.OFFER2.pl") 
        self.assertTrue(offer2 != None, 
                        "offer 'www.OFFER2.pl' should be present in 'Kurdwanow, Krakow, Polsk' group")
        
        # check image url
        self.assertEqual("www.OFFER2_img.pl", offer2["image_url"], 
                         "image_url should be 'www.OFFER2_img.pl' for 'www.OFFER2.pl' offer but was '%s'" % offer2["image_url"])
                
        # check address section string (the address that was found on the offer web page in designated field)
        self.assertEqual("osiedle Kurdwanow", offer2["address_section"], 
                         "address_section should be 'osiedle Kurdwanow' for 'www.OFFER2.pl' offer")    
        
        # check the offer title
        self.assertEqual("OFFER2", offer2["title"], 
                         "title should be 'OFFER2' for 'www.OFFER2.pl' offer")    
        
        # check the offer date
        self.assertEqual(datetime(2000, 1, 2), offer2["date"], 
                         "date should be 2000/1/2 for 'www.OFFER2.pl' offer")   
        
        # check the offer price
        self.assertEqual("2000 ZL", offer2["price"], 
                         "price should be '2000 ZL' for 'www.OFFER2.pl' offer")     
        
        # check the offer summary
        self.assertEqual("Niezbyt tanie mieszkanie, kurdwanow", offer2["summary"], 
                         "summary should be 'Niezbyt tanie mieszkanie, kurdwanow' for 'www.OFFER2.pl' offer")  
                       
        # check num rooms
        self.assertEqual(3, offer2["num_rooms"], 
                         "num_rooms should be 3 for 'www.OFFER2.pl' offer")    
                   
        # check square meters
        self.assertEqual(50, offer2["area"], 
                         "area should be 50 for 'www.OFFER2.pl' offer")   
        
                               
    def test_get_json_string(self):
        ''' 
        Only roughly check that returned string contains expected offers; 
        we are not up to check json implementation for python here.
        '''
        json = OffersGroupedByAddress.as_json([OffersGroupedByAddressTest.OFFER1, 
                                                   OffersGroupedByAddressTest.OFFER2, 
                                                   OffersGroupedByAddressTest.OFFER3])
        self.assertTrue("www.OFFER1.pl" in json, 
                        "'www.OFFER1.pl' should be in json string: '%s'" % json)                                           
        
        self.assertTrue("www.OFFER2.pl" in json, 
                        "'www.OFFER2.pl' should be in json string: '%s'" % json) 
        
        self.assertTrue("www.OFFER3.pl" in json, 
                        "'www.OFFER3.pl' should be in json string: '%s'" % json) 
                        
                        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
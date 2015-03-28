'''
Created on 13 lut 2015

@author: m.midor
'''
import unittest
from mock import Mock, patch
from src.mvc.model.offers import Offers
from src.ioc.dependency_injector import DependencyInjector

    
class OffersTest(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(OffersTest, self).__init__(*args, **kwargs)
        config_mock = Mock()
        DependencyInjector.manual_inject("config", config_mock, Offers)
    
    
    @patch('src.mvc.model.offers.AddressExtractor')
    @patch('src.mvc.model.offers.CachingGeocoder')
    @patch('src.mvc.model.offers.WebDocumentFetcher')
    @patch('src.mvc.model.offers.Gumtree')
    @patch('src.mvc.model.offers.GumtreeOfferExtractor')
    @patch('src.mvc.model.offers.Olx')
    @patch('src.mvc.model.offers.OlxOfferExtractor')
    def test_get_from_all_sources(self, olx_offer_extractor, olx,
                                  gumtree_offer_extractor, gumtree,
                                  web_doc_fetcher, geocoder_class, address_extractor):
        """
        Needed stubs:
            extractor - on extract() returns "Wielicka"
            address_extractor - on for_city() returns extractor
            geocoder_class - on geocode() returns [1.1, 2.2]
            web_doc_fetcher - on fetch() returns u"WebDocHtmlContent"
            gumtree - on get_urls() returns ["gumtree1url", "gumtree2url"]
            olx - on get_urls() return ["olx1url", "olx2url"]
            gumtree_offer_extractor - on extract() returns a dictionary with offer details
            olx_offer_extractor - on extract() returns a dictionary with offer details
        """
        # 1. Prepare the stubs
        # this is actual extractor 
        extractor = Mock()
        extractor.extract = Mock(return_value = "Wielicka")
        
        # this is extractor factory
        address_extractor.for_city = Mock(return_value = extractor)
        
        geocoder_instance = Mock()
        geocoder_instance.geocode = Mock(return_value = [1.1, 2.2])
        geocoder_class.return_value = geocoder_instance
        
        web_doc_fetcher.fetch = Mock(return_value = u"WebDocHtmlContent")
        
        gumtree.get_urls = Mock(return_value = ["gumtree1url", "gumtree2url"])
        
        olx.get_urls = Mock(return_value = ["olx1url", "olx2url"])
        
        gumtree_offer_extractor.extract = Mock(return_value = {"title" : "gumtreeoffer",
                                                               "summary" : "some description",
                                                               "address_section" : "address"})
        
        olx_offer_extractor.extract = Mock(return_value = {"title" : "olxoffer",
                                                           "summary" : "some description",
                                                           "address_section" : "address"}) 
           
         
        params = Mock()
        params.get_city = Mock(return_value = "Krakow")  
        # 2. Run the function    
              
        offers = Offers.get_from_all_sources(offer_params = params)
        
        
        # 3. Verify the returned offers
        offers = list(offers)
        self.assertEquals(len(offers), 4, "get_from_all_sources should have returned 4 offers, not %d" % len(offers))
        
        for offer in offers:
            self.assertTrue("url" in offer, "No 'url' entry in offer %s" % str(offer))
            self.assertTrue(offer["url"] in ["gumtree1url", "gumtree2url", "olx1url", "olx2url"],
                            "Invalid url in offer %s" % str(offer))
            
            self.assertTrue("address" in offer)
            self.assertEquals(offer["address"], 
                              "Wielicka, Krakow, Polska", 
                              "Offer address should be Wielicka, Krakow, Polska: %s" % str(offer))
            
            self.assertTrue("longlatt" in offer)
            self.assertEquals(offer["longlatt"], [1.1, 2.2], "longlatt of offer should be [1.1, 2.2]: %s" % str(offer))
            
 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
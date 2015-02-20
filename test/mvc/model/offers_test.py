'''
Created on 13 lut 2015

@author: m.midor
'''
import unittest
from mock import Mock
from src.mvc.model.offers import Offers

class WebDocumentFetcherStub():
    """This guy is used in offers.get_from_all_sources to return predefined html content"""

    @staticmethod
    def fetch(url):
        """Returns fixed HTML string representing gumtree offer search result"""
        return next(WebDocumentFetcherStub.__get_next_page)
    
class OffersTest(unittest.TestCase):
    
    def setUp(self):
        # this is actual extractor 
        self.ExtractorStub = Mock()
        self.ExtractorStub.extract = Mock(return_value = "Wielicka")
        
        # this is extractor factory
        self.AddressExtractorStub = Mock()
        self.AddressExtractorStub.for_city = Mock(return_value = self.ExtractorStub)
        
        self.GeocoderStub = Mock()
        self.GeocoderStub.geocode = Mock(return_value = [1.1, 2.2])
        
        self.WebDocumentFetcherStub = Mock()
        self.WebDocumentFetcherStub.fetch = Mock(return_value = u"WebDocHtmlContent")
        
        self.GumtreeStub = Mock()
        self.GumtreeStub.get_urls = Mock(return_value = ["gumtree1url", "gumtree2url"])
        
        self.OlxStub = Mock()
        self.OlxStub.get_urls = Mock(return_value = ["olx1url", "olx2url"])
        
        self.GumtreeOfferExtractorStub = Mock()
        self.GumtreeOfferExtractorStub.extract = Mock(return_value = {"title" : "gumtreeoffer",
                                                                      "summary" : "some description",
                                                                      "address_section" : "address"})
        
        self.OlxOfferExtractorStub = Mock()
        self.OlxOfferExtractorStub.extract = Mock(return_value = {"title" : "olxoffer",
                                                                  "summary" : "some description",
                                                                  "address_section" : "address"})
        
    def test_get_from_all_sources(self):
        """
        Needed stubs:
            ExtractorStub - on extract() returns "Wielicka"
            AddressExtractorStub - on for_city() returns ExtractorStub
            GeocoderStub - on geocode() returns [1.1, 2.2]
            WebDocumentFetcherStub - on fetch() returns u"WebDocHtmlContent"
            GumtreeStub - on get_urls() returns ["gumtree1url", "gumtree2url"]
            OlxStub - on get_urls() return ["olx1url", "olx2url"]
            GumtreeOfferExtractorStub - on extract() returns a dictionary with required entries
            OlxOfferExtractorStub - on extract() returns a dictionary with required entries
        """

        offers = Offers(self.GeocoderStub, 
                        self.AddressExtractorStub, 
                        self.WebDocumentFetcherStub, 
                        self.OlxStub,
                        self.GumtreeStub,
                        self.OlxOfferExtractorStub,
                        self.GumtreeOfferExtractorStub).get_from_all_sources(city="Krakow")
                        
        offers = list(offers)
        self.assertEquals(len(offers), 4, "get_from_all_sources should have returned 4 offers")
        
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
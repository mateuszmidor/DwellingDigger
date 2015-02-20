'''
Created on 12-02-2015

FACADE. All needed functionality from model package you can find here
@author: mateusz
'''
import Queue
import threading

from src.mvc.model.addressextractor.address_extractor import AddressExtractor
from src.mvc.model.gumtree.gumtree import Gumtree
from src.mvc.model.gumtree.offer_extractor import OfferExtractor as GumtreeOfferExtractor
from src.mvc.model.olx.offer_extractor import OfferExtractor as OlxOfferExtractor
from src.mvc.model.olx.olx import Olx
from src.outerspaceaccess.web_document_fetcher import WebDocumentFetcher
from src.outerspaceaccess.geocoder import Geocoder


class Offers(object):
    '''
    This class is facade for model package.
    '''
    
    def __init__(
                 self, 
                 geocoder = Geocoder,
                 address_extractor = AddressExtractor,
                 web_document_fetcher = WebDocumentFetcher,
                 olx = Olx,
                 gumtree = Gumtree,
                 olx_offer_extractor = OlxOfferExtractor,
                 gumtree_offer_extractor = GumtreeOfferExtractor
                 ):
        """ This constructor allows for full dependency injection thus enabling unit testing """
        
        self.geocoder = geocoder
        self.address_extractor = address_extractor
        self.web_document_fetcher = web_document_fetcher
        self.olx = olx
        self.gumtree = gumtree
        self.olx_offer_extractor = olx_offer_extractor
        self.gumtree_offer_extractor = gumtree_offer_extractor


    def __format_full_address(self, street_district, city, country):
        """ Compose address string from street, city and country. street is optional """
        
        if street_district:
            return u"{0}, {1}, {2}".format(street_district, city, country)
        else:
            return u"{0}, {1}".format(city, country)
        
        
    def __fetch(self, in_queue, out_queue, address_extractor):
        """
        This method takes offer url and offer extractor from in_queue,
        downloads offer page from url and extracts offer details, then
        extracts address from offer details, finds address geolocation,
        and puts offer details along with address and geolocation into out_queue
        offer_extractor individual for each url, since there can be urls
        to different www services on in_queue.
        """
        
        while True:
            url, offer_extrator = in_queue.get()
            offer_page = self.web_document_fetcher.fetch(url)
            offer = offer_extrator.extract(offer_page)
            
            street_or_district = address_extractor.extract([offer["address_section"], 
                                                            offer["title"], 
                                                            offer["summary"]]) 
             
            full_address = self.__format_full_address(street_or_district, 
                                                      address_extractor.city, 
                                                      address_extractor.country)
            offer["address"] = full_address
            
            longlatt = self.geocoder.geocode(full_address)
            offer["longlatt"] = longlatt
            
            offer["url"] = url 
            
            out_queue.put(offer) 
            in_queue.task_done()
            
    def get_from_all_sources(self, max_offer_count="5", max_parallel_count=5,
                            city="", whereabouts="", num_rooms="", min_price="", max_price="", 
                            min_area="", max_area=""):
        """ 
        Gets offers from Olx and Gumtree filtered with provided criteria.
        Returned offers contain already extracted and geocoded address 
        in "address" and "longlatt" fields, respectively. 
        
        """
        # prepare address extractor for given city
        address_extractor = self.address_extractor.for_city(city) 
        address_extractor.city = city
        address_extractor.country = "Polska"
        
        # get offer url generators
        gumtree_urls = self.gumtree.get_urls(max_offer_count, city, whereabouts, num_rooms, min_price, max_price, min_area, max_area, 
                                             self.web_document_fetcher)
        olx_urls = self.olx.get_urls(max_offer_count, city, whereabouts, num_rooms, min_price, max_price, min_area, max_area, 
                                     self.web_document_fetcher)

        # prepare task and result queue
        in_queue = Queue.Queue()
        out_queue = Queue.Queue()
        
        # prepare working threads
        for i in xrange(max_parallel_count): # @UnusedVariable
            t = threading.Thread(target=self.__fetch, 
                                 name="OfferFetchingThread", 
                                 args=(in_queue, out_queue, address_extractor))
            t.setDaemon(True)
            t.start()
        
        # put urls into input queue,
        # count urls; the max_offer_count is desired upper limit, no guarantee you will get that much
        url_count = 0
        for url in gumtree_urls:
            in_queue.put((url, self.gumtree_offer_extractor))
            url_count += 1
            
        for url in olx_urls:
            in_queue.put((url, self.olx_offer_extractor))
            url_count += 1       
            
        # yield offers from output queue
        for i in xrange(url_count): # @UnusedVariable
            yield out_queue.get()        
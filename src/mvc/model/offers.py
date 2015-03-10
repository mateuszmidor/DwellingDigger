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
from src.outerspaceaccess.cachinggeocoder import CachingGeocoder


class Offers(object):
    '''
    This class is facade for model package.
    '''

    @staticmethod
    def __format_full_address(street_district, city, country):
        """ Compose address string from street, city and country. street is optional """
        
        if street_district:
            return u"{0}, {1}, {2}".format(street_district, city, country)
        else:
            return u"{0}, {1}".format(city, country)
        
       
    @staticmethod 
    def __fetch(in_queue, out_queue, address_extractor, geocoder):
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
            offer_page = WebDocumentFetcher.fetch(url)
            offer = offer_extrator.extract(offer_page)
            
            street_or_district = address_extractor.extract([offer["address_section"], 
                                                            offer["title"], 
                                                            offer["summary"]]) 
             
            full_address = Offers.__format_full_address(street_or_district, 
                                                      address_extractor.city, 
                                                      address_extractor.country)
            offer["address"] = full_address
            
            longlatt = geocoder.geocode(full_address)
            offer["longlatt"] = longlatt
            
            offer["url"] = url 
            
            out_queue.put(offer) 
            in_queue.task_done()
            
            
    @staticmethod
    def get_from_all_sources(offer_params, max_offer_count=5, max_parallel_count=5):
        """ 
        Gets offers from Olx and Gumtree filtered with provided criteria.
        Returned offers contain already extracted and geocoded address 
        in "address" and "longlatt" fields, respectively. 
        
        """
        
        # prepare geocoder
        geocoder = CachingGeocoder("DwellingDigger/data/geocodingscache.txt")
        
        # prepare address extractor for given city
        city = offer_params.get_city()
        address_extractor = AddressExtractor.for_city(city) 
        address_extractor.city = city
        address_extractor.country = "Polska"
        
        # get offer url generators
        gumtree_urls = Gumtree.get_urls(offer_params, max_offer_count)
        olx_urls = Olx.get_urls(offer_params, max_offer_count)

        # prepare task and result queue
        in_queue = Queue.Queue()
        out_queue = Queue.Queue()
        
        # prepare working threads
        for i in xrange(max_parallel_count): # @UnusedVariable
            t = threading.Thread(target=Offers.__fetch, 
                                 name="OfferFetchingThread", 
                                 args=(in_queue, out_queue, address_extractor, geocoder))
            t.setDaemon(True)
            t.start()
        # put urls into input queue,
        # count urls; the max_offer_count is desired upper limit, no guarantee you will get that much
        url_count = 0
        for url in gumtree_urls:
            in_queue.put((url, GumtreeOfferExtractor))
            url_count += 1
            
        for url in olx_urls:
            in_queue.put((url, OlxOfferExtractor))
            url_count += 1       
            
        # yield offers from output queue
        for i in xrange(url_count): # @UnusedVariable
            yield out_queue.get()  
            
        # dump new geocodings into cache file
        geocoder.sync()      
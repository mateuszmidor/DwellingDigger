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
    FINISH = object()
    
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
        and puts offer details along with address and geolocation into out_queue.
        offer_extractor is individual for each url, since there can be urls
        to different www services using different formats on in_queue.
        """
        
        while True:
            try:
                work_data = in_queue.get()
                
                if work_data == Offers.FINISH:
                    in_queue.put(Offers.FINISH)
                    print ("Finishing fetcher thread")
                    break
                
                # unpack the work data
                url, offer_extrator = work_data
                
                # fetch the offer web page
                offer_page = WebDocumentFetcher.fetch(url)
                
                # parse the page and extract offer details
                offer = offer_extrator.extract(offer_page)
                
                # find address in the offer
                street_or_district = address_extractor.extract([offer["address_section"], 
                                                                offer["title"], 
                                                                offer["summary"]]) 
                 
                # form nice full address string containing street, city and country
                full_address = Offers.__format_full_address(street_or_district, 
                                                          address_extractor.city, 
                                                          address_extractor.country)
                
                # add the nice address to offer details
                offer["address"] = full_address
                
                # geocode the address and add it to offer details
                longlatt = geocoder.geocode(full_address)
                offer["longlatt"] = longlatt
                
                # add the offer page url to offer details
                offer["url"] = url 
                
                # output the offer
                out_queue.put(offer) 
            except:
                print ("Offer fetch exception")
                # on exception still output to indicate this work item has been processed
                out_queue.put(None)
            finally:
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
        
        # prepare task and result queue
        in_queue = Queue.Queue()
        out_queue = Queue.Queue()
        
        # prepare working threads
        for i in xrange(max_parallel_count): # @UnusedVariable
            t = threading.Thread(target=Offers.__fetch, 
                                 name="OfferFetchingThread", 
                                 args=(in_queue, out_queue, address_extractor, geocoder))
            t.start()
            
        # put urls into input queue,
        # count urls so we know how many results to expect;
        # the max_offer_count is desired upper limit, no guarantee you will get that much
        url_count = 0
        for url in Gumtree.get_urls(offer_params, max_offer_count):
            in_queue.put((url, GumtreeOfferExtractor))
            url_count += 1
            
        for url in Olx.get_urls(offer_params, max_offer_count):
            in_queue.put((url, OlxOfferExtractor))
            url_count += 1       
            
            
        # put the finish sentinel in the input queue so the working threads know when to exit
        in_queue.put(Offers.FINISH)
        
        # yield offers from output queue
        for i in xrange(url_count): # @UnusedVariable
            print("waiting for offer number: %d" % (i+1))
            offer = out_queue.get()
            if offer:
                yield offer  
            
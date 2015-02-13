'''
Created on 12-02-2015

@author: mateusz
'''
from src.outerspaceaccess.web_document_fetcher import WebDocumentFetcher
from src.offers.addressextractor.address_extractor import AddressExtractor
from src.outerspaceaccess.geocoder import Geocoder
from src.offers.gumtree.gumtree import Gumtree
from src.offers.olx.olx import Olx
from src.offers.gumtree.offer_extractor import OfferExtractor as GumtreeOfferExtractor
from src.offers.olx.offer_extractor import OfferExtractor as OlxOfferExtractor
import Queue
import threading

class Offers(object):
    '''
    classdocs
    '''

    @staticmethod 
    def __fetch(in_queue, out_queue, address_extractor, web_document_fetcher):
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
            offer_page = web_document_fetcher.fetch(url)
            offer = offer_extrator.extract(offer_page)
            
            address = address_extractor.extract([offer["address_section"], offer["title"], offer["summary"]])  
            full_address = u"{0}, {1}, {2}".format(address, address_extractor.city, address_extractor.country)
            offer["address"] = full_address
            
            longlatt = Geocoder.geocode(full_address)
            offer["longlatt"] = longlatt
            
            offer["url"] = url 
            
            out_queue.put(offer) 
            in_queue.task_done()
            
    @staticmethod
    def get_from_all_sources(max_offer_count="5", web_fetcher=WebDocumentFetcher, max_parallel_count=5,
                            city="", whereabouts="", num_rooms="", min_price="", max_price="", 
                            min_area="", max_area=""):
        
        # prepare address extractor for given city
        address_extractor = AddressExtractor.for_krakow() 
        address_extractor.city = city
        address_extractor.country = "Polska"
        # get offer url generators
        gumtree_urls = Gumtree.get_urls(max_offer_count, city, whereabouts, num_rooms, min_price, max_price, min_area, max_area, web_fetcher)
        olx_urls = Olx.get_urls(max_offer_count, city, whereabouts, num_rooms, min_price, max_price, min_area, max_area, web_fetcher)

        # prepare working queues
        in_queue = Queue.Queue()
        out_queue = Queue.Queue()
        
        # prepare working threads
        for i in xrange(max_parallel_count): # @UnusedVariable
            t = threading.Thread(target=Offers.__fetch, name="OfferFetchingThread", args=(in_queue, 
                                                                                          out_queue,
                                                                                          address_extractor,
                                                                                          web_fetcher))
            t.setDaemon(True)
            t.start()
        
        # put work into input queue,
        # count urls; the max_offer_count is upper limit, no guarantee you will get that much
        url_count = 0
        for url in gumtree_urls:
            in_queue.put((url, GumtreeOfferExtractor))
            url_count += 1
            
        for url in olx_urls:
            in_queue.put((url, OlxOfferExtractor))
            url_count += 1       
            
        # yield results from output queue
        for i in xrange(url_count): # @UnusedVariable
            yield out_queue.get()   
            
            
    @staticmethod
    def group_by_address(offers):
        pass
                    
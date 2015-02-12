'''
Created on 20-01-2015

@author: mateusz
FACADE. All needed functionality from gumtree package you can find here
'''
from src.outerspaceaccess.web_document_fetcher import WebDocumentFetcher
from src.offers.gumtree.offer_search_query import OfferSearchQuery
from src.offers.gumtree.offer_searcher import OfferSearcher
from src.offers.gumtree.offer_extractor import OfferExtractor
import threading
import Queue

class Gumtree(object):
    '''
    This class is facade for gumtree package.
    '''

    @staticmethod
    def get_urls(max_offer_count="5", city="", whereabouts="", num_rooms="", min_price="", max_price="", 
                 min_area="", max_area="", web_document_fetcher=WebDocumentFetcher):
        
        query = OfferSearchQuery.compose(city=city, whereabouts=whereabouts, num_rooms=num_rooms,
                                         min_price=min_price, max_price=max_price,
                                         min_area=min_area, max_area=max_area)
        
        return OfferSearcher.search(query, int(max_offer_count), web_document_fetcher)
               
    @staticmethod
    def get_offers(max_offer_count="5", city="", whereabouts="", num_rooms="", min_price="", max_price="", 
                   min_area="", max_area="", web_document_fetcher=WebDocumentFetcher):
        
        urls = Gumtree.get_urls(max_offer_count=max_offer_count, web_document_fetcher=web_document_fetcher,
                                city=city, whereabouts=whereabouts, num_rooms=num_rooms,
                                min_price=min_price, max_price=max_price,
                                min_area=min_area, max_area=max_area)
        for url in urls:
            offer_page = WebDocumentFetcher.fetch(url)
            offer = OfferExtractor.extract(offer_page)
            offer["url"] = url
            yield offer
       
       
    @staticmethod 
    def fetch(in_queue, out_queue):
        while True:
            url = in_queue.get()
            offer_page = WebDocumentFetcher.fetch(url)
            offer = OfferExtractor.extract(offer_page)  
            offer["url"] = url 
            out_queue.put(offer) 
            in_queue.task_done()
            
             
    @staticmethod
    def get_offers_parallel(max_offer_count="5", city="", whereabouts="", num_rooms="", min_price="", max_price="", 
                            min_area="", max_area="", max_parallel_count=5):
        
        query = OfferSearchQuery.compose(city=city, whereabouts=whereabouts, num_rooms=num_rooms,
                                         min_price=min_price, max_price=max_price,
                                         min_area=min_area, max_area=max_area)
        
        urls = OfferSearcher.search(query, int(max_offer_count), WebDocumentFetcher)
        
        # prepare working queues
        in_queue = Queue.Queue()
        out_queue = Queue.Queue()
        
        # prepare working threads
        for i in xrange(max_parallel_count): # @UnusedVariable
            t = threading.Thread(target = Gumtree.fetch, name="OfferFetchingThread", args=(in_queue, out_queue))
            t.setDaemon(True)
            t.start()
            
        # put work into input queue,
        # count urls; the max_offer_count is upper limit, no guarantee you will get that much
        found_url_count = 0
        for url in urls:
            in_queue.put(url)
            found_url_count += 1
            

        # yeald results from output queue
        for i in xrange(found_url_count): # @UnusedVariable
            yield out_queue.get()
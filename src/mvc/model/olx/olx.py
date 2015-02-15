'''
Created on 25-01-2015

@author: mateusz
FACADE. All needed functionality from olx package you can find here
'''
from src.mvc.model.olx.offer_search_query import OfferSearchQuery
from src.mvc.model.olx.offer_searcher import OfferSearcher
from src.mvc.model.olx.offer_extractor import OfferExtractor
from src.outerspaceaccess.web_document_fetcher import WebDocumentFetcher

class Olx(object):
    '''
    This class is facade for olx package.
    '''

    @staticmethod
    def get_urls(max_offer_count="5", city="", whereabouts="", num_rooms="", min_price="", max_price="", 
                 min_area="", max_area="", web_document_fetcher=WebDocumentFetcher):
        
        query = OfferSearchQuery.compose(city=city, whereabouts=whereabouts, num_rooms=num_rooms,
                                         min_price=min_price, max_price=max_price,
                                         min_area=min_area, max_area=max_area)
        
        return OfferSearcher.search(query, int(max_offer_count), web_document_fetcher)
    
    @staticmethod
    def get_offers(max_offer_count="5", web_document_fetcher=WebDocumentFetcher,
                   city="", whereabouts="", num_rooms="", min_price="", max_price="", 
                   min_area="", max_area=""):
        
        urls = Olx.get_urls(max_offer_count=max_offer_count, web_document_fetcher=web_document_fetcher,
                            city=city, whereabouts=whereabouts, num_rooms=num_rooms,
                            min_price=min_price, max_price=max_price,
                            min_area=min_area, max_area=max_area)
        for url in urls:
            offer_page = WebDocumentFetcher.fetch(url)
            try:
                offer = OfferExtractor.extract(offer_page)
                offer["url"] = url
                yield offer
            except:
                continue
            

        
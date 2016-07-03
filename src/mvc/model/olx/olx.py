'''
Created on 25-01-2015

@author: mateusz
FACADE. All needed functionality from olx package you can find here
'''
from src.mvc.model.olx.apartment_offer_search_query import ApartmentOfferSearchQuery
from src.mvc.model.olx.singleroom_offer_search_query import SingleroomOfferSearchQuery
from src.mvc.model.olx.offer_searcher import OfferSearcher
from src.mvc.model.olx.offer_extractor import OfferExtractor
from src.outerspaceaccess.web_document_fetcher import WebDocumentFetcher

class Olx(object):
    '''
    This class is facade for olx package.
    '''


    @staticmethod
    def get_urls(offer_params, max_offer_count=5, web_document_fetcher=WebDocumentFetcher):
        
        # want single room offers?
        if str(offer_params.get_num_rooms()) == "0":
            singleroom_query = SingleroomOfferSearchQuery.from_offer_params(offer_params)
            return OfferSearcher.search(singleroom_query, max_offer_count, web_document_fetcher)
            
        # want apartments
        apartment_query = ApartmentOfferSearchQuery.from_offer_params(offer_params)
        return OfferSearcher.search(apartment_query, max_offer_count, web_document_fetcher)
    
    
    @staticmethod
    def get_offers(offer_params, max_offer_count=5, web_document_fetcher=WebDocumentFetcher):
        
        urls = Olx.get_urls(offer_params=offer_params,
                            max_offer_count=max_offer_count, 
                            web_document_fetcher=web_document_fetcher)
        for url in urls:
            offer_page = web_document_fetcher.fetch(url)
            try:
                offer = OfferExtractor.extract(offer_page)
                offer["url"] = url
                yield offer
            except:
                continue
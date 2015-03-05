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
    def get_urls(offer_params, max_offer_count=5, web_document_fetcher=WebDocumentFetcher):
        
        query = OfferSearchQuery.from_offer_params(offer_params)
        return OfferSearcher.search(query, int(max_offer_count), web_document_fetcher)
    
    
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
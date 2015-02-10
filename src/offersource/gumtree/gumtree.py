'''
Created on 20-01-2015

@author: mateusz
FACADE. All needed functionality from gumtree package you can find here
'''
from src.offersource.gumtree.offer_search_query import OfferSearchQuery
from src.offersource.gumtree.offer_searcher import OfferSearcher
from src.offersource.gumtree.offer_extractor import OfferExtractor
from src.offersource.web_document_fetcher import WebDocumentFetcher

class Gumtree(object):
    '''
    This class is facade for gumtree package.
    '''

    @staticmethod
    def get_offers(max_offer_count="5", city="", whereabouts="", num_rooms="", min_price="", max_price="", 
                   min_area="", max_area=""):
        
        query = OfferSearchQuery.compose(city=city, whereabouts=whereabouts, num_rooms=num_rooms,
                                         min_price=min_price, max_price=max_price,
                                         min_area=min_area, max_area=max_area)
        
        urls = OfferSearcher.search(query, int(max_offer_count), WebDocumentFetcher)
        for url in urls:
            offer_page = WebDocumentFetcher.fetch(url)
            offer = OfferExtractor.extract(offer_page)
            offer["url"] = url
            yield offer
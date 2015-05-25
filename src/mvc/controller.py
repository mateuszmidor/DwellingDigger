# -*- coding: utf-8 -*-
'''
Created on 16-01-2015

@author: mateusz
'''
import cProfile
import pstats

from src.mvc.model.gumtree.offer_search_query import OfferSearchQuery as GumtreeOfferSearchQuery
from src.mvc.model.gumtree.offer_searcher import OfferSearcher as GumtreeOfferSearcher
from src.mvc.model.gumtree.gumtree import Gumtree

from src.mvc.model.olx.offer_searcher import OfferSearcher as OlxOfferSearcher
from src.mvc.model.olx.offer_search_query import OfferSearchQuery as OlxOfferSearchQuery
from src.mvc.model.olx.olx import Olx

from src.outerspaceaccess.web_document_fetcher import WebDocumentFetcher

from src.mvc.model.addressextractor.address_extractor import AddressExtractor
from src.mvc.model.addressextractor.evaluator.evaluator import Evaluator
from src.mvc.model.offer_params import OfferParams


class Controller:


    @staticmethod
    def demo_run():
        run_func = Controller.print_learning_samples
#         run_func = Controller.print_5_olx_offer_urls
#         run_func = Controller.print_5_olx_offer_details
#         run_func = Controller.print_5_gumtree_offer_urls
#         run_func = Controller.print_5_gumtree_offer_details
#         run_func = Controller.evaluate_address_extractor
        Controller.profile_func(run_func)
        
                
    @staticmethod
    def profile_func(run_func):
        cProfile.runctx("run_func()", 
                        globals={"global_variables":"none"}, 
                        locals={"run_func":run_func}, 
                        filename="diagnostics/DesktopMain_profile.txt")
        p = pstats.Stats("diagnostics/DesktopMain_profile.txt")
        p.strip_dirs().sort_stats('cumulative').print_stats(20)        
       
             
    @staticmethod
    def evaluate_address_extractor():
        """ Evaluate the extractor against krakow data """
        extractor = AddressExtractor.for_city("krakow")
        Evaluator.evaluate(extractor)
       
        
    @staticmethod
    def print_learning_samples():
        """ 
        Prints learning samples for AddressExtractor. It looks like this:
        # 1.
        source= [address section]
        source= [title]
        source= [summary]
        expected= [to be manually filled]
        ... repeat
        """   

        params = OfferParams.from_key_values(city="Kraków")
        offers = Olx.get_offers(offer_params=params, max_offer_count=100)
        for i, offer in enumerate(offers, 1):
            print("# %i." % i)
            print("source=%s" % offer["address_section"])
            print("source=%s" % offer["title"].replace("\n", "").replace("\r", ""))
            print("source=%s" % offer["summary"].replace("\n", "").replace("\r", ""))
            print("expected= ")
       
                     
    @staticmethod
    def print_5_olx_offer_details():
        """Prints out details of 5 offers found on OLX"""
       
        params = OfferParams.from_key_values(city=u"Kraków", 
                                             num_rooms=3)        
        offers = Olx.get_offers(offer_params=params, max_offer_count=5)
        for i, offer in enumerate(offers, 1):
            print("%i." % i)
            print(offer["title"])
            print(offer["date"])
            print(offer["price"])
            print(offer["address_section"])
            print(offer["summary"])
            print("")
       
              
    @staticmethod
    def print_5_olx_offer_urls():
        """Prints out 5 urls to offers found on OLX"""
        
        query = OlxOfferSearchQuery.from_key_values(city=u"Krakow",  
                                                    whereabouts=u"ruczaj")
        print(query)
        urls = OlxOfferSearcher.search(query, 5, WebDocumentFetcher)
        for i, url in enumerate(urls, 1):
            print("{0}. {1}".format(i, url))
       
             
    @staticmethod
    def print_5_gumtree_offer_details():
        """Prints out details of 5 offers found on Gumtree"""
        
        params = OfferParams.from_key_values(city="Krakow", 
                                             whereabouts="prądnik",
                                             num_rooms="1", 
                                             max_price="1200")
        
        offers = Gumtree.get_offers(offer_params=params, max_offer_count=5)
        for i, offer in enumerate(offers, 1):
            print("%i." % i)
            print(offer["title"])
            print(offer["date"])
            print(offer["price"])
            print(offer["address_section"])
            print(offer["summary"])
            print("")


    @staticmethod
    def print_5_gumtree_offer_urls():
        """Prints out 5 urls to offers found on Gumtree"""
        
        query = GumtreeOfferSearchQuery.from_key_values(city="Krakow")
        for url in GumtreeOfferSearcher.search(query, 5, WebDocumentFetcher):
            print(url)

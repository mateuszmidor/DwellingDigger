# -*- coding: utf-8 -*-

'''
Created on 24 mar 2015

@author: m.midor
'''

# initialize_dependency_injection must be imported first in the main module to initialize all needed dependencies
import src.ioc.initialize_dependency_injection  # @UnusedImport

import cProfile
import pstats

from src.mvc.model.gumtree.offer_searcher import OfferSearcher as GumtreeOfferSearcher
from src.mvc.model.gumtree.apartment_offer_search_query import ApartmentOfferSearchQuery as GumtreeApartmentOfferSearchQuery
from src.mvc.model.gumtree.singleroom_offer_search_query import SingleroomOfferSearchQuery as GumtreeSingleroomOfferSearchQuery
from src.mvc.model.gumtree.gumtree import Gumtree

from src.mvc.model.olx.offer_searcher import OfferSearcher as OlxOfferSearcher
from src.mvc.model.olx.apartment_offer_search_query import ApartmentOfferSearchQuery as OlxApartmentOfferSearchQuery
from src.mvc.model.olx.singleroom_offer_search_query import SingleroomOfferSearchQuery as OlxSingleroomOfferSearchQuery
from src.mvc.model.olx.olx import Olx

from src.outerspaceaccess.web_document_fetcher import WebDocumentFetcher

from src.mvc.model.addressextractor.address_extractor import AddressExtractor
from src.mvc.model.addressextractor.evaluator.evaluator import Evaluator
from src.mvc.model.offer_params import OfferParams


class Demo(object):
    """ DEMO - for testing and playing around with separated components of the project """

    @staticmethod
    def run():
        """ Run the demo to do whatever it is configured to """

#         run_func = Demo.print_learning_samples
#         run_func = Demo.print_5_olx_offer_urls
        run_func = Demo.print_5_olx_offer_details
#         run_func = Demo.print_5_gumtree_offer_urls
#         run_func = Demo.print_5_gumtree_offer_details
#         run_func = Demo.evaluate_address_extractor
        Demo.profile_func(run_func)


    @staticmethod
    def profile_func(run_func):
        """ Run given func under profiler and print the timing statistics """
        cProfile.runctx("run_func()",
                        globals={"global_variables":"none"},
                        locals={"run_func":run_func},
                        filename="diagnostics/DesktopMain_profile.txt")
        profiling_stats = pstats.Stats("diagnostics/DesktopMain_profile.txt")
        profiling_stats.strip_dirs().sort_stats('cumulative').print_stats(20)


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
                                             whereabouts=u"kazimierz",
                                             num_rooms=u"0") # 0 rooms means: single rooms not apartments
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

        query = OlxSingleroomOfferSearchQuery.from_key_values(city=u"Krakow",
                                                                whereabouts=u"ruczaj")
        print(query)
        urls = OlxOfferSearcher.search(query, 5, WebDocumentFetcher)
        for i, url in enumerate(urls, 1):
            print("{0}. {1}".format(i, url))


    @staticmethod
    def print_5_gumtree_offer_details():
        """Prints out details of 5 offers found on Gumtree"""

        params = OfferParams.from_key_values(city="Krakow",
                                             whereabouts="kazimierz",
                                             num_rooms="0") # 0 rooms = single room offers

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

        query = GumtreeSingleroomOfferSearchQuery.from_key_values(city="Krakow",
                                                        whereabouts="kazimierz")
        print(query)
        for url in GumtreeOfferSearcher.search(query, 5, WebDocumentFetcher):
            print(url)


if __name__ == '__main__':
    Demo.run()

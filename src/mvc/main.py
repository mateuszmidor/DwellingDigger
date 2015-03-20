'''
Created on 27-02-2015

@author: mateusz
'''
from src.mvc.model.offers import Offers
from src.ioc.dependency_injector import DependencyInjector, Inject

@DependencyInjector("config")
class Main(object):
    
    config = Inject
    
    '''
    DwellingDigger main page controller.
    '''
    @staticmethod
    def run(params, view):
        num_offers = Main.config.getint("OUTPUT", "numPresentedOffers")
        num_threads = Main.config.getint("PERFORMANCE", "numWorkerThreads")
        offers = Offers.get_from_all_sources(offer_params=params, 
                                             max_offer_count=num_offers, 
                                             max_parallel_count=num_threads)
        view.show_offers(offers)
        
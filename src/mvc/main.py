'''
Created on 27-02-2015

@author: mateusz
'''
from src.mvc.model.offers import Offers
from src.ioc.dependency_injector import DependencyInjector, Inject
from src.diagnostics.method_enter_logger import MethodEnterLogger
from src.diagnostics.method_exit_logger import MethodExitLogger

@DependencyInjector("config", "logger")
class Main(object):
    ''' DwellingDigger main page controller '''
    
    config = Inject
    logger = Inject
    
    
    @staticmethod
    @MethodEnterLogger("New session")
    @MethodExitLogger("Session done.\n")  
    def run(params, view):
        
        # get num offers to be fetched and num threads that can be used to fetch offers in parallel
        num_offers = Main.config.getint("OUTPUT", "numPresentedOffers")
        num_threads = Main.config.getint("PERFORMANCE", "numWorkerThreads")
        
        # get the offers
        offers = Offers.get_from_all_sources(offer_params=params, 
                                             max_offer_count=num_offers, 
                                             max_parallel_count=num_threads)
        
        # show the offers
        view.show_offers_and_params(offers, params)

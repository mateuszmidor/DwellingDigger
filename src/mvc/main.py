'''
Created on 27-02-2015

@author: mateusz
'''
from src.mvc.model.offers import Offers

class Main(object):
    '''
    DwellingDigger main page controller.
    '''
    @staticmethod
    def run(params, view):
        offers = Offers.get_from_all_sources(offer_params=params, 
                                             max_offer_count=25, 
                                             max_parallel_count=5)
        view.show_offers(offers)
        
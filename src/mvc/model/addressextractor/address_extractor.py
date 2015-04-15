# -*- coding: utf-8 -*-

'''
Created on 08-02-2015

@author: mateusz
FACADE. All needed functionality from addressextractor you can find here
'''
from src.mvc.model.addressextractor.rankbased.dictionary import Dictionary
from src.mvc.model.addressextractor.rankbased.asciinator import Asciinator
from src.mvc.model.addressextractor.rankbased.declinator import Declinator
from src.mvc.model.addressextractor.rankbased.surnamenator import Surnamenator
from src.mvc.model.addressextractor.rankbased.rank_based_extractor import RankBasedExtractor
from src.ioc.dependency_injector import Inject, DependencyInjector


@DependencyInjector("config")
class AddressExtractor(object):
    '''
    This class is facade for addressextractor package.
    '''

    config = Inject
    
    
    @staticmethod
    def rank_based(dictionary_file_type):
        """
        Builds and returns RankBasedExtractor.
        """
        
        dictionary = Dictionary()
        for filename, address_type in dictionary_file_type:
            dictionary.extend(Dictionary.from_file(filename, address_type))
        
        Asciinator.asciinate_dictionary(dictionary)
        Declinator.declinate_dictionary(dictionary)
        Surnamenator.surnamenate_dictionary(dictionary)
        dictionary.sort_longest_first()
        
        return RankBasedExtractor(dictionary)
        
    @staticmethod
    def for_krakow():
        DATA_PATH = AddressExtractor.config.get("PATHS", "data")
        dicts = [(DATA_PATH + "krakow_streets.txt", Dictionary.STREET), 
                 (DATA_PATH + "krakow_districts.txt", Dictionary.DISTRICT)]
        return AddressExtractor.rank_based(dicts)

    @staticmethod
    def for_city(city):
        if city.lower() in [u"krakow", u"kraków"]:
            return AddressExtractor.for_krakow()
        
        raise NotImplementedError()
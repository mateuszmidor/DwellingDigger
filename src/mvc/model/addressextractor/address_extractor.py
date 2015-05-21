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
    def __address_dict_for_city(city_name):
        """ 
        Creates a dictionary of streets and districts of given city.
        The streets and districts are loaded from data files.
        @param city_name: must correspond to proper filename in /data directory.     
        """
        # path to folder with files containing streets and districts of given city 
        # see: config.ini->PATHS to find out what the "data" path really is
        data_path = AddressExtractor.config.get("PATHS", "data")
        
        # path to file containing streets, eg. data/krakow_streets.txt
        streets_path = data_path + city_name + "_streets.txt"
        
        # path to file containing districts, eg. data/krakow_districts.txt
        districts_path = data_path + city_name + "_districts.txt"
        
        # build the dictionary from streets and districts
        dictionary = Dictionary()
        dictionary.extend(Dictionary.from_file(streets_path, Dictionary.STREET))
        dictionary.extend(Dictionary.from_file(districts_path, Dictionary.DISTRICT))
        
        # complement the dictionary with no-national-characters versions of streets and districts
        Asciinator.asciinate_dictionary(dictionary)
        
        # complement the dictionary with declinated ie. eg. "wielickiej" or "slonecznym" versions of streets and districts
        Declinator.declinate_dictionary(dictionary)
        
        # complement the dictionary with shortened eg. "Dietla" instead of "Józefa Dietla" versions of streets and districts
        Surnamenator.surnamenate_dictionary(dictionary)        
        return dictionary
      

    @staticmethod
    def for_city(city_name):
        """
        Creates an address extractor specialized for given city.
        @param city_name: non-ascii, lowercase name of the city. Eg. "krakow"
        """
         
        # prepare dictionary of streets and addresses that can be found in given city 
        dictionary = None
        
        # only support the cities for which files with streets and districts are prepared
        if city_name.lower() in [u"krakow", u"kraków"]:
            dictionary = AddressExtractor.__address_dict_for_city("krakow")
        else:
            raise NotImplementedError("City %s not supported, yet" % city_name)
        
        return RankBasedExtractor(dictionary)
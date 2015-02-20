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

class AddressExtractor(object):
    '''
    This class is facade for addressextractor package.
    '''

    @staticmethod
    def rank_based(dictionary_filenames):
        """
        Builds and returns RankBasedExtractor.
        The order of entries in dictionary_filenames is important:
        the extractor will look up the dictionaries in the same order as provided,
        so should be from most precise (streets) to most general (cities)
        """
        
        dictionaries = map(Dictionary.from_file, dictionary_filenames)
        map(lambda d : d.sort_longest_first(), dictionaries)
        map(Asciinator.asciinate_dictionary, dictionaries)
        map(Declinator.declinate_dictionary, dictionaries)
        map(Surnamenator.surnamenate_dictionary, dictionaries)
        
        return RankBasedExtractor(*dictionaries)
        
    @staticmethod
    def for_krakow():
        dict_files = ["DwellingDigger/data/krakow_streets.txt", 
                    "DwellingDigger/data/krakow_districts.txt"]
        return AddressExtractor.rank_based(dict_files)

    @staticmethod
    def for_city(city):
        if city.lower() in [u"krakow", u"kraków"]:
            return AddressExtractor.for_krakow()
        
        raise NotImplementedError()
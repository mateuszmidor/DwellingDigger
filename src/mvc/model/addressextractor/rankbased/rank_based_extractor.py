'''
Created on 27-01-2015

@author: mateusz
'''
import re
from src.mvc.model.addressextractor.rankbased.address_candidates import AddressCandidates
from src.mvc.model.addressextractor.rankbased.rank_prefix import RankPrefix
from src.mvc.model.addressextractor.rankbased.rank_suffix import RankSuffix
from src.mvc.model.addressextractor.rankbased.rank_capital_letter import RankCapitalLetter
from src.mvc.model.addressextractor.rankbased.declinator import Declinator
from src.mvc.model.addressextractor.rankbased.address_candidate import AddressCandidate

class RankBasedExtractor(object):
    '''
    Extracts address using provided address dictionaries and rank evaluators,
    and returns best ranked result as string
    '''
    dictionaries = list()

    def __init__(self, *dictionaries):
        """
        Constructor.
        The order of provided dictionaries in important:
        the extractor will look up the dictionaries in the same order as provided,
        so should be from most precise (streets) to most general (cities)
        """
                
        self.dictionaries = dictionaries
        
    def extract(self, sources):
        candidates = AddressCandidates()
        
        for dictionary in self.dictionaries:
            self.__extract_from_sources(sources, dictionary, candidates)
        
        prefix = RankPrefix()
        prefix.rank(candidates)
        
        suffix = RankSuffix()
        suffix.rank(candidates)
        
        capital = RankCapitalLetter()
        capital.rank(candidates)
        
        if len(candidates) > 0:
            candidates.sort_by_correctness_precision()
            return Declinator.undeclinate(candidates[0].address.lower())
        
        return None
        
    
    def __extract_from_sources(self, sources, dictionary, candidates):
        for source in sources:
            self.__extract_from_source(source, dictionary, candidates)
            
        
    def __extract_from_source(self, source, dictionary, candidates):
        lowercase_source = source.lower()
        for address in dictionary:
            if address in lowercase_source:
                self.__extract_address_with_number(address, source, candidates)
        
                
    def __extract_address_with_number(self, address, source, candidates):
        pattern = self.__compose_pattern(address)
        f = re.search(pattern, source, re.IGNORECASE | re.UNICODE)
        if f:
            address = f.group(0)
            self.__add_address_candidate(address, source, candidates)
        
        
    def __compose_pattern(self, address):
        OPTIONAL_NUMBER = ur"(?:[ ]{1,5}\d{1,5}\w?)?"
        return ur"\b{0}{1}\b".format(address, OPTIONAL_NUMBER)
    
    
    def __add_address_candidate(self, address, source, candidates):
        c = AddressCandidate()
        c.address = address
        c.source = source
        candidates.append(c)
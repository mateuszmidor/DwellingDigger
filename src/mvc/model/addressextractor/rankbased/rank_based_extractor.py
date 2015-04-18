'''
Created on 27-01-2015

@author: mateusz
'''
import re
from src.mvc.model.addressextractor.rankbased.address_candidates import AddressCandidates
from src.mvc.model.addressextractor.rankbased.rank_prefix import RankPrefix
from src.mvc.model.addressextractor.rankbased.rank_suffix import RankSuffix
from src.mvc.model.addressextractor.rankbased.rank_capital_letter import RankCapitalLetter
from src.mvc.model.addressextractor.rankbased.address_candidate import AddressCandidate
from src.mvc.model.addressextractor.rankbased.dictionary import Dictionary

class RankBasedExtractor(object):
    '''
    Extracts address using provided address dictionaries and rank evaluators,
    and returns best ranked result as string
    '''
    dictionaries = list()

    def __init__(self, dictionary):
        """
        Constructor.
        As input takes dictionary of known addresses (DictionaryEntry)
        """
                
        self.dictionary = dictionary
        
    def extract(self, sources):
        candidates = AddressCandidates()
        
        self.__extract_from_sources(sources, self.dictionary, candidates)
        
        prefix = RankPrefix()
        prefix.rank(candidates)
         
        suffix = RankSuffix()
        suffix.rank(candidates)
         
        capital = RankCapitalLetter()
        capital.rank(candidates)
        
        if len(candidates) > 0:
            candidates.sort_by_correctness_precision()
            return candidates[0].full_form_address
        
        return None
        
    
    def __extract_from_sources(self, sources, dictionary, candidates):
        for source in sources:
            self.__extract_from_source(source, dictionary, candidates)
            
        
    def __extract_from_source(self, source, dictionary, candidates):
        lowercase_source = source.lower()
        for entry in dictionary:
            # if name is in source, then possibly the address is found
            # unless name is only a part of another word
            if entry.name in lowercase_source:
                lowercase_source = self.__extract_candidate(entry, source, lowercase_source, candidates)
        
                
    def __extract_candidate(self, entry, source, lower_source, candidates):
        """ Returns lowercase source without the extracted candidate """
        
        pattern = self.__compose_pattern(entry.name)
        f = re.search(pattern, source, re.IGNORECASE | re.UNICODE)
        
        # no address found - return just lowercase source 
        if not f:
            return lower_source
        
        # get the number if we are talking about address being a street that has a number provided   
        prefix = self.__normalize_prefix_or_none(f.group(1), entry.address_type)
        address =  f.group(2) 
        number = f.group(3) if entry.address_type == Dictionary.STREET and f.groups() else None
        # remove the found candidate from the source (remove "nowa huta" so "nowa" street doesnt come up in results)
        source_without_candidate = lower_source.replace(address.lower(), u"")
        
        c = AddressCandidate()
        c.address = address
        c.full_form_address = self.__compose_full_form_address(entry.original_form, prefix, number)
        c.source = source 
        c.precision_rank = self.__precision_from_addrtype(entry.address_type)
        c.correctness_rank = self.__correctness_from_genuinity(entry.name, entry.original_form)
        candidates.append(c)
        
        return source_without_candidate
        
        
    def __compose_pattern(self, address):
        # ?: means "non-capturing group" ie. doesnt show up in matchobj.group()
        # at least 2 letters, optional period, 0-3 spaces
        OPTIONAL_PREFIX = ur"(?:(\w{2,}\.?)\s{0,3})?"
        # 1-5 spaces, 1-5 digits, optional letter, eg. " 15a"
        OPTIONAL_NUMBER = ur"(?:\s{1,5}(\d{1,5})\w?)?"
        return ur"\b{0}({1}){2}\b".format(OPTIONAL_PREFIX, address, OPTIONAL_NUMBER)
    
    
    def __compose_full_form_address(self, address, prefix, number):
        result = u""
        
        # add prefix eg "ul. " if exists
        if prefix:
            result += prefix + u" "
            
        # add address itself, eg "Wielicka"
        result += address     
        
        # add number if exists
        if number:
            result += u" " + number
        return result    
        
        
    def __normalize_prefix_or_none(self, supposed_prefix, address_type):
        STREET = [u"ulica", u"ulicy", u"ul ", u"ul."]
        ALLEY = [u"aleja", u"alei", u"al ", u"al."]
        SETTLEMENT = [u"os ", u"os.", u"osiedle", u"osiedlu"]
        MAPPINGS = {u"ul." : STREET,
                    u"al." : ALLEY,
                    u"os." : SETTLEMENT}

        for prefix, mutations in MAPPINGS.items():
            if supposed_prefix in mutations:
                return prefix
                          
        return None
        
        
    def __precision_from_addrtype(self, address_type):
        if address_type == Dictionary.STREET:
            return 2
        if address_type == Dictionary.DISTRICT:
            return 1
        
        return 0
    
    
    def __correctness_from_genuinity(self, used_form, original_form):
        if used_form.lower() == original_form.lower():
            # if genuine address form - its fine to use it
            return 0
        else:
            # if mutated address form - penalty earned
            return -1;
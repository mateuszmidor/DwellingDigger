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
        
        # dictionary needs to be sorted so eg.
        # "Nowa Huta" is examined and excluded before "Nowa" street
        dictionary.sort_longest_first()
        self.dictionary = dictionary
        
        
    def extract(self, sources):
        candidates = AddressCandidates()
        
        RankBasedExtractor.extract_from_sources(sources, self.dictionary, candidates)
        
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
        
    
    @staticmethod
    def extract_from_sources(sources, dictionary, candidates):
        for source in sources:
            RankBasedExtractor.extract_from_source(source, dictionary, candidates)
            
        
    @staticmethod
    def extract_from_source(source, dictionary, candidates):
        lowercase_source = source.lower()
        for entry in dictionary:
            # if name is in source, then possibly the address is found
            # unless name is only a part of another word
            if entry.name in lowercase_source:
                lowercase_source = RankBasedExtractor.extract_candidate(entry, source, lowercase_source, candidates)
        
                
    @staticmethod
    def extract_candidate(entry, source, lower_source, candidates):
        """ 
        Searches and adds new candidate to 'candidates'.
        Returns lowercase source without the extracted candidate. 
        """
        
        # this pattern allows to extract street/settlement/district name ignorecase 
        # and the number, if present (good to know street number, hmm?)
        pattern = RankBasedExtractor.compose_pattern(entry.name)
        found = re.search(pattern, source, re.IGNORECASE | re.UNICODE)
        
        # no such address found - return just lowercase source 
        if not found:
            return lower_source

        # street/settlement/district name ignorecase         
        address =  found.group(1) 
        
        # get the number if we are talking about address being a street that has a number provided   
        number = found.group(2) if entry.address_type == Dictionary.STREET and found.groups() else None
        
        
        # create address candidate
        candidate = AddressCandidate()
        candidate.address = address
        candidate.full_form_address = RankBasedExtractor.compose_full_form_address(entry.original_form, number)
        candidate.source = source 
        candidate.precision_rank = RankBasedExtractor.precision_from_addrtype(entry.address_type)
        candidate.correctness_rank = 0
        candidates.append(candidate)
        
        # remove the found candidate from the search source string;
        # eg. remove "nowa huta" so "nowa" street doesnt come up in results
        source_without_candidate = lower_source.replace(address.lower(), u"")
        
        return source_without_candidate
        
        
    @staticmethod
    def compose_pattern(address):
        # ?: means "non-capturing group" ie. doesnt show up in matchobj.group()
        # 1-5 spaces, 1-5 digits, optional letter, eg. " 15a"
        optional_number = ur"(?:\s{1,5}(\d{1,5})\w?)?"
        
        # address, case insensitive, will end up in capture group 1
        # street number, if present, will end up in capture group 2
        return ur"\b({0}){1}\b".format(address, optional_number)
    
    
    @staticmethod
    def compose_full_form_address(address, number):
        result = u""
        
        # add address itself, eg "Wielicka"
        result += address     
        
        # add number if exists
        if number:
            result += u" " + number
        return result    
               
        
    @staticmethod
    def precision_from_addrtype(address_type):
        if address_type == Dictionary.STREET:
            return 2
        if address_type == Dictionary.DISTRICT:
            return 1
        
        return 0

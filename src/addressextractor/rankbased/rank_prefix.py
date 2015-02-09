# -*- coding: utf-8 -*-

'''
Created on 5 lut 2015

@author: m.midor
'''
import re

class RankPrefix(object):
    '''
    This class ranks up address candidate precission and correctness based on
    having meaningful prefix eg. "ulica Wielicka", "os Kurdwanow", "obok Ruczaju"
    '''


    def rank(self, address_candidates):
        HI_PRECISION_RANK = 3
        MED_PRECISION_RANK = 2
        LO_PRECISION_RANK = 0
        
        HI_PRECISION_PREFIX = [u"ulica", u"ulicy", u"ul ", u"ul.", u"aleja", u"alei", u"al ", u"al."]
        MED_PRECISION_PREFIX = [u"os ", u"os.", u"osiedle", u"osiedlu"]
        LO_PRECISION_PREFIX = [u"przy", u"na", u"obok", u"w pobliżu"]
        
        self.__rank_by_prefix(address_candidates, HI_PRECISION_PREFIX, HI_PRECISION_RANK)
        self.__rank_by_prefix(address_candidates, MED_PRECISION_PREFIX, MED_PRECISION_RANK)
        self.__rank_by_prefix(address_candidates, LO_PRECISION_PREFIX, LO_PRECISION_RANK)
        
        
    def __rank_by_prefix(self, address_candidates, prefixes, rank_award):
        for candidate in address_candidates:
            self.__rank_candidate(candidate, prefixes, rank_award)
            
    

    def __rank_candidate(self, candidate, prefixes, rank_award):
        address = self.__escape_special_characters(candidate.address)
        pattern = self.__compose_pattern(address)
        found = pattern.search(candidate.source)
        if found:
            found_prefix_lowercase = found.group(1).lower()
            self.__rank_if_known_prefix(found_prefix_lowercase, prefixes, rank_award, candidate)
                                        

    def __rank_if_known_prefix(self, found_prefix, known_prefixes, rank_award, candidate):
        for prefix in known_prefixes:
            if found_prefix == prefix:
                candidate.correctness_rank += 1
                candidate.precision_rank += rank_award
        
        
    def __escape_special_characters(self, s):
        return s.replace(u".", ur"\.")  
    
    
    def __compose_pattern(self, addres):
        # word boundary, prefix, 0-3 spaces, address
        # [\w\.]{2,} part matches the prefix
        return re.compile(ur"\b([\w\.]{2,})\s{0,3}%s" % addres, re.IGNORECASE | re.UNICODE)
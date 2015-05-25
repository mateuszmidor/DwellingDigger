# -*- coding: utf-8 -*-

'''
Created on 5 lut 2015

@author: m.midor
'''
import re

class RankPrefix(object):
    '''
    This class ranks up address correctness based on
    having meaningful prefix eg. "ulica Wielicka", "os Kurdwanow", "obok Ruczaju"
    '''

    # Pattern to look for address prefix when source string ends with that prefix
    # word boundary, prefix possibly ending with period, 0-3 spaces, end of line
    # (\w{2,}\.?) part matches the prefix
    __PATTERN = re.compile(ur"\b(\w{2,}\.?)\s{0,3}$", re.IGNORECASE | re.UNICODE)
    
    def rank(self, address_candidates):        
        hi_precision_prefix = [u"ulica", u"ulicy", u"ul ", u"ul.", u"aleja", u"alei", u"al ", u"al."]
        med_precision_prefix = [u"os ", u"os.", u"osiedle", u"osiedlu"]
        lo_precision_prefix = [u"przy", u"na", u"obok", u"w pobliżu"]
        
        RankPrefix.rank_by_prefix(address_candidates, hi_precision_prefix)
        RankPrefix.rank_by_prefix(address_candidates, med_precision_prefix)
        RankPrefix.rank_by_prefix(address_candidates, lo_precision_prefix)
        
        
    @staticmethod
    def rank_by_prefix(address_candidates, prefixes):
        for candidate in address_candidates:
            RankPrefix.rank_candidate(candidate, prefixes)
    

    @staticmethod
    def rank_candidate(candidate, prefixes):
        source_until_address = RankPrefix.get_source_until_address(candidate)
        found = RankPrefix.__PATTERN.search(source_until_address)
        if found:
            found_prefix_lowercase = found.group(1).lower()
            RankPrefix.rank_if_known_prefix(found_prefix_lowercase, prefixes, candidate)
                         
                                        
    @staticmethod
    def get_source_until_address(candidate):
        address = candidate.address
        source = candidate.source
        address_position_in_source = source.find(address)
        source_until_address = source[:address_position_in_source]
        return source_until_address


    @staticmethod
    def rank_if_known_prefix(found_prefix, known_prefixes, candidate):
        for prefix in known_prefixes:
            if found_prefix == prefix:
                candidate.correctness_rank += 1
                break

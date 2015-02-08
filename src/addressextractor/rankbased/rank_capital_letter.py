# -*- coding: utf-8 -*-

'''
Created on 5 lut 2015

@author: m.midor
'''
import re

class RankCapitalLetter(object):
    '''
    This class ranks address candidate correctness probability based on 
    whether the address starts with capital letter
    '''

    def rank(self, address_candidates):
        PATTERN = ur"^[A-ZĄĆĘŁŃÓŚŹŻ]"
        
        for candidate in address_candidates:
            if re.search(PATTERN, candidate.address):
                candidate.correctness_rank += 1
            
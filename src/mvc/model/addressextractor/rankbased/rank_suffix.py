'''
Created on 5 lut 2015

@author: m.midor
'''
import re

class RankSuffix(object):
    '''
    This class ranks address candidate correctness +1 and precission +1 
    based on having suffix number, eg. "wielicka 24b"
    '''


    def rank(self, address_candidates):
        #  word space number optional_letter eg. "wielicka 23b"
        PATTERN = ur"\w+\s{0,3}\d{1,3}\w?\b"
        
        for candidate in address_candidates:
            if re.search(PATTERN, candidate.address, re.IGNORECASE):
                candidate.correctness_rank += 1
                candidate.precision_rank += 1
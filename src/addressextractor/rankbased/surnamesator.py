# -*- coding: utf-8 -*-

'''
Created on 5 lut 2015

@author: m.midor
'''
import re

class Surnamesator(object):
    '''
    This class extracts possible surnames from addresses 
    eg. "Michała Sochy" -> "Sochy"
    '''


    @staticmethod
    def surnamesate_dictionary(dictionary):
        """ Iterate over dictionary entries and extract surnames if any, then add them to dictinoary """
        
        surnames = list()
        for address in dictionary:
            surname = Surnamesator.__surnamisate(address)
            Surnamesator.__append_if_differs(surname, address, surnames)
            
        dictionary.extend(surnames)        
        
    
    @staticmethod
    def __surnamisate(address):
        if Surnamesator.__contains_surname(address):
            return Surnamesator.__extract_surname(address)
        
        # Return original address if no surname found
        return address
    
    @staticmethod
    def __contains_surname(address):
        return " " in address or "-" in address
    
    @staticmethod
    def __extract_surname(address):
        return re.split(" |-", address)[-1]
    
    
    @staticmethod
    def __append_if_differs(surname, address, surnames):
        if surname != address:
            surnames.append(surname)
# -*- coding: utf-8 -*-

'''
Created on 5 lut 2015

@author: m.midor
'''
import re
from src.mvc.model.addressextractor.rankbased.dictionary_entry import DictionaryEntry

class Surnamenator(object):
    '''
    This class extracts possible surnames from address dictionary and adds them to dictionary 
    eg. "Michała Sochy" -> "Sochy"
    '''


    @staticmethod
    def surnamenate_dictionary(dictionary):
        """ Iterate over dictionary entries and extract surnames if any, then add them to dictinoary """
        
        surnames = list()
        for entry in dictionary:
            surname = Surnamenator.__surnamenate(entry.name)
            Surnamenator.__append_if_differs(surname, entry, surnames)
            
        dictionary.extend(surnames)        
        
    
    @staticmethod
    def __surnamenate(address):
        if Surnamenator.__contains_surname(address):
            surname = Surnamenator.__extract_surname(address)
            if len(surname) > 2:
                return surname 
        
        # Return original address if no surname found
        return address
    
    @staticmethod
    def __contains_surname(address):
        return " " in address or "-" in address
    
    @staticmethod
    def __extract_surname(address):
        return re.split(" |-", address)[-1]
    
    
    @staticmethod
    def __append_if_differs(surname, entry, surnames):
        if surname != entry.name:
            new_entry = DictionaryEntry(surname, entry.name, entry.address_type)
            surnames.append(new_entry)
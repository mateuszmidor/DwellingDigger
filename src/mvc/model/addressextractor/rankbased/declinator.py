# -*- coding: utf-8 -*-

'''
Created on 04-02-2015

@author: mateusz
'''
from src.mvc.model.addressextractor.rankbased.dictionary_entry import DictionaryEntry

class Declinator(object):
    '''
    This class declinates words from dictionary, then puts them into that dictionary
    '''
    
    NORMAL_MODAL = {"ska" : "skiej", # krakowskiej
                    "cka" : "ckiej", # tynieckiej
                    "ny"  : "nach",  # czyżynach
                    "czne": "cznym"  # slonecznym 
                    }
    
    
    @staticmethod
    def declinate_dictionary(dictionary):
        """ Iterate over all addresses in dictionary and generate declinations when possible """
        
        declinations = list()
        for entry in dictionary:
            declination = Declinator.__declinate(entry.name)
            Declinator.__append_if_differs(declination, entry, declinations)
            
        dictionary.extend(declinations)
        
        
    @staticmethod
    def __declinate(address):
        """ Check if address can be declinated, if so - change the address ending to modal form and return """
        
        for normal, modal in Declinator.NORMAL_MODAL.iteritems():
            if address.endswith(normal):
                return address.replace(normal, modal)
        
        # If no declination of address possible, return original form
        return address
        
       
    @staticmethod 
    def __append_if_differs(declination, entry, declinations):
        if declination != entry.name:
            new_entry = DictionaryEntry(declination, entry.name, entry.address_type)
            declinations.append(new_entry)
        
    @staticmethod
    def undeclinate(address):
        for normal, modal in Declinator.NORMAL_MODAL.iteritems():
            if modal in address:
                return address.replace(modal, normal)
            
        # If no undeclination of address possible, return original form
        return address 
    
'''
Created on 5 lut 2015

@author: m.midor
'''
import unicodedata
from src.mvc.model.addressextractor.rankbased.dictionary_entry import DictionaryEntry

class Asciinator(object):
    '''
    This class takes from a dictionary words with national characters, 
    turns them into words with ascii characters only and adds them to the dictionary
    '''

    @staticmethod
    def asciinate_dictionary(dictionary):
        """ Iterate over dictionary entries and generate ascii-only counterparts for words containing national characters """
        
        asciinations = list()
        for entry in dictionary:
            asciination = Asciinator.__asciinate(entry.name)
            Asciinator.__append_if_differs(asciination, entry, asciinations)
            
        dictionary.extend(asciinations)
        
        
    @staticmethod
    def __asciinate(address):
        return "".join(c for c in unicodedata.normalize('NFD', address) if unicodedata.category(c) != 'Mn')
    

    @staticmethod
    def __append_if_differs(asciination, entry, asciisations):
        if asciination != entry.name:
            new_entry = DictionaryEntry(asciination, entry.original_form, entry.address_type)
            asciisations.append(new_entry)
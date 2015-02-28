'''
Created on 28-02-2015

@author: mateusz
'''

class DictionaryEntry(object):
    '''
    Represents single entry in address dictionary
    '''

    
    CITY        = 0
    DISTRICT    = 1
    STREET      = 2
    UNKNOWN     = 99
    
    def __init__(self, name, original_form, address_type):
        # Address name, possibly mutated, eg. Wielickiej
        self.name = name.strip("\t\n\r ").lower()
        
        # Original form the name was derived from, eg. Wielicka
        self.original_form = original_form.strip("\t\n\r ")
        
        # Address type
        self.address_type = address_type
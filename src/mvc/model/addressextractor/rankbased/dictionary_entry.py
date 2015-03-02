'''
Created on 28-02-2015

@author: mateusz
'''

class DictionaryEntry(object):
    '''
    Represents single entry in address dictionary.
    Enforces the address name and original form to be in proper form.
    '''

    
    CITY        = 0
    DISTRICT    = 1
    STREET      = 2
    
    def __init__(self, name, original_form, address_type):
        # Address name, possibly mutated, eg. wielickiej
        self.name = name.strip("\t\n\r ").lower()
        
        # Original form the name was derived from, eg. Wielicka
        self.original_form = original_form.strip("\t\n\r ")
        
        # Address type
        self.address_type = address_type
        
        
    def is_valid(self):
        """ Valid DictionaryEntry has name, original_form and address_type properly set """
        return self.name and self.original_form and self.address_type in [DictionaryEntry.CITY, DictionaryEntry.DISTRICT, DictionaryEntry.STREET]

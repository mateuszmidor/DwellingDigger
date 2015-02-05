'''
Created on 5 lut 2015

@author: m.midor
'''
import unicodedata

class Asciisator(object):
    '''
    This class turns words with national characters into words with ascii characters only
    '''

    @staticmethod
    def asciisate_dictionary(dictionary):
        """ Iterate over dictionary entries and generate ascii-only counterparts for words containing national characters """
        
        asciisations = list()
        for address in dictionary:
            asciisation = Asciisator.__asciisate(address)
            Asciisator.__append_if_differs(asciisation, address, asciisations)
            
        dictionary.extend(asciisations)
        
        
    @staticmethod
    def __asciisate(address):
        return "".join(c for c in unicodedata.normalize('NFD', address) if unicodedata.category(c) != 'Mn')
    

    @staticmethod
    def __append_if_differs(asciisation, address, asciisations):
        if asciisation != address:
            asciisations.append(asciisation)
    
    
        
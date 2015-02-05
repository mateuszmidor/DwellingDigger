'''
Created on 5 lut 2015

@author: m.midor
'''
import unicodedata

class Asciinator(object):
    '''
    This class takes from a dictionary words with national characters, 
    turns them into words with ascii characters only and adds them to the dictionary
    '''

    @staticmethod
    def asciinate_dictionary(dictionary):
        """ Iterate over dictionary entries and generate ascii-only counterparts for words containing national characters """
        
        asciinations = list()
        for address in dictionary:
            asciination = Asciinator.__asciinate(address)
            Asciinator.__append_if_differs(asciination, address, asciinations)
            
        dictionary.extend(asciinations)
        
        
    @staticmethod
    def __asciinate(address):
        return "".join(c for c in unicodedata.normalize('NFD', address) if unicodedata.category(c) != 'Mn')
    

    @staticmethod
    def __append_if_differs(asciination, address, asciisations):
        if asciination != address:
            asciisations.append(asciination)
    
    
        
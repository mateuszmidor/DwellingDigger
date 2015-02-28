'''
Created on 4 lut 2015

@author: m.midor
'''
from src.outerspaceaccess.text_file_reader import TextFileReader
from src.mvc.model.addressextractor.rankbased.dictionary_entry import DictionaryEntry

class Dictionary(object):
    '''
    This class represents a dictionary of known addresses.
    It allows to load the addresses from file.
    '''
    
    STREET      = DictionaryEntry.STREET
    DISTRICT    = DictionaryEntry.DISTRICT
    CITY        = DictionaryEntry.CITY
    
    # Storage for dictionary contents (DictionaryEntry list)
    __keys = None

    @staticmethod
    def from_file(filename, address_type, filereader = TextFileReader):
        dictionary = Dictionary()
        for address in filereader.read_lines(filename):
            stripped_address = address.strip("\t\n\r ")
            if not stripped_address:
                continue
            entry = DictionaryEntry(stripped_address, stripped_address, address_type)
            dictionary.append(entry)
        return dictionary


    def __init__(self, entries = []):
        self.__keys = list()
        self.extend(entries)


    def extend(self, entries):
        self.__keys.extend(entries)
             

    def append(self, entry):
        if entry.name != u"" and entry.original_form != u"" and entry.address_type in [DictionaryEntry.CITY, DictionaryEntry.DISTRICT, DictionaryEntry.STREET]:
            self.__keys.append(entry)
        
        
    def sort_longest_first(self):
        # longest first - for 'find' to match Krakowska before Krakow
        longToShort = lambda s1, s2: cmp(len(s2.name), len(s1.name))
        self.__keys.sort(longToShort)
                
        
    def __iter__(self):
        ''' Provide iterator interface '''
        return self.__keys.__iter__()
    
    
    def __contains__(self, key):
        ''' Provide "KEY in COLLECTION" interface '''
        return self.__keys.__contains__(key)
    
    
    def __len__(self):
        ''' Provide len interface '''
        return self.__keys.__len__()
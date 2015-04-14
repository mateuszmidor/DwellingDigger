'''
Created on 4 lut 2015

@author: m.midor
'''
from src.outerspaceaccess.text_file_reader import TextFileReader
from src.mvc.model.addressextractor.rankbased.dictionary_entry import DictionaryEntry
from src.outerspaceaccess.text_file_writer import TextFileWriter

class Dictionary(object):
    '''
    This class represents a dictionary of known addresses.
    It allows to load the addresses from a file.
    '''
    
    STREET      = DictionaryEntry.STREET
    DISTRICT    = DictionaryEntry.DISTRICT
    CITY        = DictionaryEntry.CITY
    
    # Storage for dictionary contents (DictionaryEntry list)
    __entries = None
    
        
    @staticmethod
    def from_file(filename, address_type, filereader = TextFileReader):
        dictionary = Dictionary()
        for address in filereader.read_lines(filename):
            entry = DictionaryEntry(address, address, address_type)
            dictionary.append(entry)
            
        return dictionary


    def __init__(self, entries = []):
        self.__entries = list()
        map(self.append, entries)


    def extend(self, entries):
        map(self.append, entries)
             

    def append(self, entry):
        if entry.is_valid():
            self.__entries.append(entry)
        
        
    def sort_longest_first(self):
        # longest first - for 'find' to match Krakowska before Krakow
        longToShort = lambda s1, s2: cmp(len(s2.name), len(s1.name))
        self.__entries.sort(longToShort)
                
       
    def to_file(self, filename):
        content = ""
        for e in self:
            content = content + e.name + "\n"
            
        TextFileWriter.write(filename, content)
        
                
    def __iter__(self):
        ''' Provide iterator interface '''
        
        return self.__entries.__iter__()
    
    
    def __getitem__(self, index):
        ''' Provide indexing interface '''
        return self.__entries.__getitem__(index)
    
    
    def __contains__(self, key):
        ''' Provide "KEY in COLLECTION" interface '''
        return self.__entries.__contains__(key)
    
    
    def __len__(self):
        ''' Provide len interface '''
        return self.__entries.__len__()
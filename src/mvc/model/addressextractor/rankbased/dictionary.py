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
        ''' 
        Input file in format:
        ul. Adama Mickiewicza
        al. Jerozolimskie
        os. Wawelskie
        Notice the prefixes, not necessary, but improve precision
        '''
        dictionary = Dictionary()
        for address in filereader.read_lines(filename):
            no_prefix_address = Dictionary.__strip_from_prefix(address)
            entry = DictionaryEntry(no_prefix_address, address, address_type)
            dictionary.append(entry)
            
        return dictionary


    @staticmethod
    def __strip_from_prefix(address):
        prefixes = [u"ul.", u"al.", u"os."]
        for prefix in prefixes:
            if prefix in address:
                # remove the prefix and trim from remaining whitespaces
                return address.strip(prefix).lstrip()
            
        # no prefix found
        return address
    

    def __init__(self, entries=[]):
        self.__entries = list()
        self.extend(entries)


    def extend(self, entries):
        [self.append(entry) for entry in entries]
             

    def append(self, entry):
        if entry.is_valid():
            self.__entries.append(entry)
        
        
    def sort_longest_first(self):
        # longest first - for 'find' to match Krakowska before Krakow
        long_to_short = lambda s1, s2: cmp(len(s2.name), len(s1.name))
        self.__entries.sort(long_to_short)
                
       
    def to_file(self, filename):
        content = ""
        for entry in self:
            content = content + entry.name + "\t" * 8 + entry.original_form + "\n"
            
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

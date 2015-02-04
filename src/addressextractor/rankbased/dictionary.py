'''
Created on 4 lut 2015

@author: m.midor
'''
from src.outerspaceaccess.text_file_reader import TextFileReader

class Dictionary(object):
    '''
    This class represents a dictionary of known addresses.
    It allows to load the addresses from file.
    It enforces that the stored addresses are always lowercase,
    no empty entries are allowed in dictionary
    '''
    
    # Storage for dictionary contents
    __keys = None

    @staticmethod
    def from_file(filename, filereader = TextFileReader):
        
        lines = filereader.read_lines(filename)
        dictionary = Dictionary()
        dictionary.extend(lines)
        return dictionary


    def __init__(self):
        self.__keys = list()
             

    def append(self, value):
        address = self.__format_address_string(value)
        self.__add_address_if_not_empty(address)


    def extend(self, values):
        map(self.append, values)
        
        
    def __format_address_string(self, value):
        return value.strip("\n\r\t ").lower()

        
    def __add_address_if_not_empty(self, address):
        if address != "":
            self.__keys.append(address.lower())

        
    def __iter__(self):
        ''' Provide iterator interface '''
        return self.__keys.__iter__()
    
    
    def __contains__(self, key):
        ''' Provide "KEY in COLLECTION" interface '''
        return key in self.__keys
    
    def __len__(self):
        ''' Provide len interface '''
        return self.__keys.__len__()
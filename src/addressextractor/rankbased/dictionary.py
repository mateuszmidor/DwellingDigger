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
        return Dictionary(lines)


    def __init__(self, addresses = []):
        self.__keys = list()
        self.extend(addresses)


    def extend(self, addresses):
        map(self.append, addresses)
             

    def append(self, address):
        address = self.__format_address_string(address)
        self.__add_address_if_not_empty(address)
        
        
    def __format_address_string(self, s):
        return s.strip("\n\r\t ").lower()

        
    def __add_address_if_not_empty(self, address):
        if address != "":
            self.__keys.append(address)

        
    def __iter__(self):
        ''' Provide iterator interface '''
        return self.__keys.__iter__()
    
    
    def __contains__(self, key):
        ''' Provide "KEY in COLLECTION" interface '''
        return self.__keys.__contains__(key)
    
    
    def __len__(self):
        ''' Provide len interface '''
        return self.__keys.__len__()
'''
Created on 4 lut 2015

@author: m.midor
'''
from src.outerspaceaccess.text_file_reader import TextFileReader

class Dictionary(object):
    '''
    This class represents a dictionary of known addresses.
    It allows to load the addresses from file.
    It enforces that the stored addresses are always lowercase
    '''
    
    # Storage for dictionary contents
    __keys = None

    @staticmethod
    def from_file(filename, filereader = TextFileReader):
        
        dictionary = Dictionary()
        lines = filereader.read_lines(filename)
        map(dictionary.add, lines)
        return dictionary

    def __init__(self):
        self.__keys = list()
                
    def __iter__(self):
        ''' Provide iterator interface '''
        
        return self.__keys
    
    def __contains__(self, key):
        return key in self.__keys
    
    def add(self, value):
        self.__keys.append(value.lower())
'''
Created on 4 lut 2015

@author: m.midor
'''
import codecs
from src.ioc.dependency_injector import DependencyInjector, Inject

@DependencyInjector('logger')
class TextFileReader(object):
    """ This class allows to read string data in utf-8 format from local storage. """

    logger = Inject
    
    
    @staticmethod
    def read(filename):
        """ Read entire file contents and return it as as string """
        
        try:
            return codecs.open(filename, "r", "utf-8").read()
        except IOError as e:  
            TextFileReader.logger.exception(e)
        
        
    @staticmethod
    def read_lines(filename):
        """ Read all the lines from file and return as a list of strings """
        
        try:
            return codecs.open(filename, "r", "utf-8").readlines()
        except IOError as e: 
            TextFileReader.logger.exception(e)

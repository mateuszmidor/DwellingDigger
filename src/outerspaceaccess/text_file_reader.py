'''
Created on 4 lut 2015

@author: m.midor
'''
import codecs

class TextFileReader(object):
    '''
    This class allows to read string data in utf-8 format from local storage.
    '''

    @staticmethod
    def read(filename):
        try:
            return codecs.open(filename, "r", "utf-8").read()
        except IOError as e:  # @UnusedVariable
            print(e)
            #logger.exception(e)
            return u""        
        
    @staticmethod
    def read_lines(filename):
        try:
            return codecs.open(filename, "r", "utf-8").readlines()
        except IOError as e:  # @UnusedVariable
            print(e)
            #logger.exception(e)
            return list()
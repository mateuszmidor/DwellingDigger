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
    def read_lines(filename):
        try:
            return codecs.open(filename, "utf-8").readlines()
        except IOError as e:  # @UnusedVariable
            #logger.exception(e)
            return list()
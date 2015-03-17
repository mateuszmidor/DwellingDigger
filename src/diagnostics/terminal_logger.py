'''
Created on 17 mar 2015

@author: m.midor
'''
import logging
from multiprocessing import Lock

class TerminalLogger(object):
    '''
    This class allows you log information to terminal.
    It is thread-safe.
    '''


    def __init__(self, level=logging.INFO):
        self.__lock = Lock()

        
    def exception(self, e):
        with self.__lock:
            print(str(e))
    
        
    def debug(self, msg):
        with self.__lock:
            print(msg)
        
        
    def info(self, msg):
        with self.__lock:
            print(msg)
        
        
    def warn(self, msg):
        with self.__lock:
            print(msg)
        
        
    def error(self, msg):
        with self.__lock:
            print(msg)             
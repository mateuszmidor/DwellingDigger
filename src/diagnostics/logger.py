'''
Created on 17 mar 2015

@author: m.midor
'''
import logging
from multiprocessing import Lock

class Logger(object):
    '''
    This class is a base logging class intended for extending.
    It is thread-safe.
    '''
    
    DEBUG   = logging.DEBUG
    INFO    = logging.INFO
    WARN    = logging.WARN
    ERROR   = logging.ERROR 
    FATAL   = logging.FATAL
    
    
    def __init__(self):
        # the below is to be implemented in extending classes
        # logging.basicConfig(filenamy=?, level=?)
        self.__lock = Lock()
        
        
    def debug(self, msg):
        with self.__lock:
            logging.debug(msg)
        
        
    def info(self, msg):
        with self.__lock:
            logging.info(msg)
        
        
    def warn(self, msg):
        with self.__lock:
            logging.warn(msg)
        
        
    def error(self, msg):
        with self.__lock:
            logging.error(msg)  
            
            
    def exception(self, e):
        with self.__lock:
            logging.exception(str(e))            
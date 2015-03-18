'''
Created on 17 mar 2015

@author: m.midor
'''
import logging
from multiprocessing import Lock


class Logger(object):
    '''
    This class allows for simple logging to file or to terminal.
    It is thread-safe.
    '''
    
    DEBUG   = logging.DEBUG
    INFO    = logging.INFO
    WARN    = logging.WARN
    ERROR   = logging.ERROR 
    FATAL   = logging.FATAL
    
    
    @staticmethod
    def to_terminal(log_level = WARN):  
        handler = logging.StreamHandler()
        handler.setLevel(log_level)
        return Logger(handler)
        
 
    @staticmethod
    def to_file(filename, log_level = WARN):  
        handler = logging.FileHandler(filename)
        handler.setLevel(log_level)
        return Logger(handler)
              
          
    def __init__(self, handler):
        self.__lock = Lock()
        formatter = logging.Formatter('[%(asctime)s]  %(levelname)s:  %(message)s')
        handler.setFormatter(formatter)
        logger = logging.getLogger("MainLogger")
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        self.__logger = logger
        
        
    def debug(self, msg):
        with self.__lock:
            self.__logger.debug(msg)
        
        
    def info(self, msg):
        with self.__lock:
            self.__logger.info(msg)
        
        
    def warn(self, msg):
        with self.__lock:
            self.__logger.warn(msg)
        
        
    def error(self, msg):
        with self.__lock:
            self.__logger.error(msg)  
            
            
    def exception(self, e):
        with self.__lock:
            self.__logger.exception(str(e))            
'''
Created on 17 mar 2015

@author: m.midor
'''
import logging
from multiprocessing import Lock

class FileLogger(object):
    '''
    This class allows you log information to a file.
    It is thread-safe.
    '''


    def __init__(self, filename, level=logging.INFO):
        logging.basicConfig(filename=filename, level=level)
        self.__lock = Lock()

        
    def exception(self, e):
        with self.__lock:
            logging.exception(str(e))
    
        
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
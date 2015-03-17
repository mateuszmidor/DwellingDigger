'''
Created on 17 mar 2015

@author: m.midor
'''
import logging
from src.diagnostics.logger import Logger

class FileLogger(Logger):
    '''
    This class allows you log information to a file.
    It is thread-safe.
    '''


    def __init__(self, filename, level=Logger.WARN):
        super(FileLogger, self).__init__()
        logging.basicConfig(filename=filename, level=level)
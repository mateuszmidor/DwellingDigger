'''
Created on 17 mar 2015

@author: m.midor
'''
import logging
from src.diagnostics.logger import Logger

class TerminalLogger(Logger):
    '''
    This class allows you log information to terminal.
    It is thread-safe.
    '''
    

    def __init__(self, level=Logger.WARN):
        super(TerminalLogger, self).__init__()
        logging.basicConfig(level=level)
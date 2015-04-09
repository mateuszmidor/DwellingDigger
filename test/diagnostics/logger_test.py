'''
Created on 01-04-2015

@author: mateusz
'''
import unittest
from src.diagnostics.logger import Logger
from mock import patch
import logging


class LogHandler(logging.Handler):
    """ 
    This class intercepts records composed by examined logger,
    so we can see the logger puts desired message in the record.
    """
    
    last_record = "<no record outputted>"
    
    def handle(self, record):
        self.last_record = str(record)
        
        
        
class LoggerTest(unittest.TestCase):

    @patch("src.diagnostics.logger.StreamHandler")
    def test_log_to_terminal(self, handler_class_mock):
        # Setup mock
        handler = LogHandler()
        handler_class_mock.return_value = handler

        # Setup terminal logger
        logger = Logger.to_terminal(Logger.DEBUG)
        
        # Check the logger properly outputs messages
        self.check_logger(logger, handler)


    @patch("src.diagnostics.logger.FileHandler")
    def test_log_to_file(self, handler_class_mock):
        # Setup mock
        handler = LogHandler()
        handler_class_mock.return_value = handler

        # Setup file logger
        logger = Logger.to_file("dummy.log", Logger.DEBUG)
        
        # Check the logger properly outputs messages
        self.check_logger(logger, handler)
        

    @patch("src.diagnostics.logger.NullHandler")
    def test_log_to_dev_null(self, handler_class_mock):
        # Setup mock    
        handler = LogHandler()
        handler_class_mock.return_value = handler

        # Setup null logger
        logger = Logger.to_dev_null()
        
        # Check the logger properly outputs messages.
        # In reality it will not output anything as it is /dev/null logger, 
        # but we replace its devnull handler to see it properly handles incoming messages
        # before sending them to oblivion
        self.check_logger(logger, handler)
        
        
    def check_logger(self, l, h):
        DEBUG_MSG = "debug_message"
        l.debug(DEBUG_MSG)
        self.assertTrue(DEBUG_MSG in h.last_record, 
                        "Logger output '%s' doesnt include expected message '%s' for debug() method" %  
                        (h.last_record, DEBUG_MSG))

        INFO_MSG = "info_message"
        l.info(INFO_MSG)
        self.assertTrue(INFO_MSG in h.last_record, 
                        "Logger output '%s' doesnt include expected message '%s' for info() method" %  
                        (h.last_record, INFO_MSG))
     
        WARNING_MSG = "warning_message"
        l.warn(WARNING_MSG)
        self.assertTrue(WARNING_MSG in h.last_record, 
                        "Logger output '%s' doesnt include expected message '%s' for warn() method" %  
                        (h.last_record, WARNING_MSG))   
        
        ERROR_MSG = "error_message"
        l.error(ERROR_MSG)
        self.assertTrue(ERROR_MSG in h.last_record, 
                        "Logger output '%s' doesnt include expected message '%s' for error() method" %  
                        (h.last_record, ERROR_MSG))   
       
        EXCEPTION_MSG = "exception_message"
        l.exception(Exception(EXCEPTION_MSG))
        self.assertTrue(EXCEPTION_MSG in h.last_record, 
                        "Logger output '%s' doesnt include expected message '%s' for exception() method" %  
                        (h.last_record, EXCEPTION_MSG)) 
                        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
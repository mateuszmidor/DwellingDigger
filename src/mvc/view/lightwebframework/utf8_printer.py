'''
Created on 29-03-2015

@author: mateusz
'''

import sys
import codecs

class Utf8Printer():
    
    @staticmethod
    def setup_utf8_printing():
        reload(sys)
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
        
        
    @staticmethod
    def print_text(utf8_text):
        Utf8Printer.setup_utf8_printing()
        print(utf8_text)
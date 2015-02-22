'''
Created on 31-07-2014

@author: mateusz
This class allows to load HTML template, 
substitue values for predefined $fields$ and return resulting html.
'''
from src.outerspaceaccess.text_file_writer import TextFileWriter
from src.outerspaceaccess.text_file_reader import TextFileReader

class WebPageTemplate():
    __html = u""
    
    @staticmethod
    def from_file(filename):
        html = TextFileReader.read(filename)
        return WebPageTemplate(html)
        
    @staticmethod
    def from_html_string(html):
        return WebPageTemplate(html)
    
    def __init__(self, html):
        self.__html = html
        
    def set_field(self, fieldname, value):
        if isinstance(value, str):
            value = unicode(value, 'utf-8') # from string
        else:
            value = unicode(value) # from eg float, integer, etc
            
        self.__html = self.__html.replace(unicode(fieldname), value)
        
    def save_to_file(self, filename):
        TextFileWriter.write(filename, self.__html)
        
    def get_html_string(self):
        return self.__html
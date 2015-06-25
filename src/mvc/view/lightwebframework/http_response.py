'''
Created on 29-03-2015

@author: mateusz
'''
from src.mvc.view.lightwebframework.utf8_printer import Utf8Printer

class HttpResponse(object):
    
    @staticmethod
    def render_page(html):
        HttpResponse.print_http_header() 
        HttpResponse.print_text(html)  
             
    @staticmethod
    def print_http_header():
        Utf8Printer.print_text(u"Content-type: text/html;charset=utf-8\n\n")

    @staticmethod
    def print_text(html):
        Utf8Printer.print_text(html)
        
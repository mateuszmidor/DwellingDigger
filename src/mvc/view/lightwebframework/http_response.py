'''
Created on 29-03-2015

@author: mateusz
'''
from src.mvc.view.lightwebframework.utf8_printer import Utf8Printer

class HttpResponse():
    
    @staticmethod
    def renderPage(html):
        HttpResponse.printHttpContentTypeHeader() 
        HttpResponse.printText(html)  
             
    @staticmethod
    def printHttpContentTypeHeader():
        Utf8Printer.printText(u"Content-type: text/html;charset=utf-8\n\n")

    @staticmethod
    def printText(html):
        Utf8Printer.printText(html)
        
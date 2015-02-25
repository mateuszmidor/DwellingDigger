# -*- coding: UTF-8 -*-

'''
Created on 20-01-2015

@author: mateusz
'''
import re
from datetime import datetime

class OfferExtractor(object):
    '''
    This class parses an offer page html and returns a dictionary with offer details.
    '''
    
    @staticmethod
    def extract(html):
        oe = OfferExtractor()  
        
        title = oe.__extract_title(html)
        date = oe.__extract_date(html)
        price = oe.__extract_price(html)
        address_section = oe.__extract_address(html)
        description = oe.__extract_description(html)
        summary = oe.__extract_summary(html)
        image_url = oe.__extract_image_url(html)
        
        offer = {"title" : title,
                 "date" : date,
                 "price" : price,
                 "address_section" : address_section,
                 "description" : description,
                 "summary" : summary,
                 "image_url" : image_url}
        return offer    

    def __extract_price(self, offer_html):
        START_TAG = "<td style='font-weight:bold'>"
        STOP_TAG = "</td>"
        return self.__get_string_between(offer_html, START_TAG, STOP_TAG)
    
    def __extract_date(self, offer_html):
        START_TAG = '<td class="first_row" >'
        STOP_TAG = '</td>' 
        day, month, year = self.__get_string_between(offer_html, START_TAG, STOP_TAG).split("/") # eg. "29/07/2014"
        return datetime(int(year), int(month), int(day))
    
    def __extract_title(self, offer_html):
        START_TAG = '<title>'
        STOP_TAG = '</title>'
        return self.__get_string_between(offer_html, START_TAG, STOP_TAG)
    
    def __extract_address(self, offer_html):
        START_TAG = u'<td itemscope itemtype="http://schema.org/Place">'
        STOP_TAG = u'</td>'
        address = self.__get_string_between(offer_html, START_TAG, STOP_TAG)
        address = address.replace(u"Pokaż mapę", "")
        return self.__strip_from_html_tags(address).strip()
    
    def __extract_description(self, offer_html):
        START_TAG = '<span id="preview-local-desc">'
        STOP_TAG = '</span>'
        desciption = self.__get_string_between(offer_html, START_TAG, STOP_TAG)
        return self.__strip_from_html_tags(desciption)

    def __extract_summary(self, offer_html):
        START_TAG = 'property="og:description" content="'
        STOP_TAG = '"/>'
        summary = self.__get_string_between(offer_html, START_TAG, STOP_TAG)
        return self.__strip_from_html_tags(summary)

    def __extract_image_url(self, offer_html):
        START_TAG = '<meta property="og:image" content="'
        STOP_TAG = '"/>'
        return self.__get_string_between(offer_html, START_TAG, STOP_TAG)   

    def __strip_from_html_tags(self, text):
        return re.sub('<[^<]+>', '', text)
    
    def __get_string_between(self, source, start, stop):
        i_start = source.find(start) + len(start)
        i_stop = source.find(stop, i_start)
        return source[i_start:i_stop].strip()
        
# -*- coding: utf-8 -*-

'''
Created on 24-01-2015

@author: mateusz
'''
import re

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
        START_TAG = 'property="og:description" content="'
        STOP_TAG = '"/>'
        price_and_summary = self.__get_string_between(offer_html, START_TAG, STOP_TAG)
        price = price_and_summary[:price_and_summary.index(":")] # extract the price, eg. "1 400zł: " beginning 
        return price
    
    def __extract_date(self, offer_html):
        REGEX_PATTERN = r"Dodane\s+o \d\d:\d\d, ([^,]+)"
        f = re.search(REGEX_PATTERN, offer_html)
        return f.group(1) if f else None
    
    def __extract_title(self, offer_html):
        START_TAG = '<meta property="og:title" content="'
        STOP_TAG = '"/>'
        return self.__get_string_between(offer_html, START_TAG, STOP_TAG)
    
    def __extract_address(self, offer_html):
        START_TAG = u'<strong class="c2b small">'
        STOP_TAG = u'</strong>'
        address = self.__get_string_between(offer_html, START_TAG, STOP_TAG)
        return self.__strip_from_html_tags(address).strip()
    
    def __extract_description(self, offer_html):
        START_TAG = '<p class="pding10 lheight20 large">'
        STOP_TAG = '</p>'
        desciption = self.__get_string_between(offer_html, START_TAG, STOP_TAG)
        return self.__strip_from_html_tags(desciption)

    def __extract_summary(self, offer_html):
        START_TAG = 'property="og:description" content="'
        STOP_TAG = '"/>'
        price_and_summary = self.__get_string_between(offer_html, START_TAG, STOP_TAG)
        summary = price_and_summary[price_and_summary.index(":") + 2:] # cut out the price, eg. "1 400zł: " beginning 
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
        
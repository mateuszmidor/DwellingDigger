# -*- coding: utf-8 -*-

'''
Created on 24-01-2015

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
        """
        Takes offer page html source and returns offer details as a dictionary
        @param html:    offer page source html
        """
        
        # alias for short
        ofe = OfferExtractor
        
        title           = ofe.extract_title(html)
        date            = ofe.extract_date(html)
        price           = ofe.extract_price(html)
        address_section = ofe.extract_address(html)
        description     = ofe.extract_description(html)
        summary         = ofe.extract_summary(html)
        image_url       = ofe.extract_image_url(html)
        num_rooms       = ofe.extract_num_rooms(html)
        area            = ofe.extract_area(html)
        
        offer = {"title"            : title,
                 "date"             : date,
                 "price"            : price,
                 "address_section"  : address_section,
                 "description"      : description,
                 "summary"          : summary,
                 "image_url"        : image_url,
                 "num_rooms"        : num_rooms,
                 "area"             : area }
        
        return offer    


    @staticmethod
    def extract_price(offer_html):
        start_tag = 'property="og:description" content="'
        stop_tag = '"/>'
        price_and_summary = OfferExtractor.get_string_between(offer_html, start_tag, stop_tag)
        
        # extract the price, eg. "1 400zł: " beginning
        price = price_and_summary[:price_and_summary.index(":")]  
        return price
    
    @staticmethod
    def extract_date(offer_html):
        months = {u"stycznia"   : 1,
                  u"lutego"     : 2,
                  u"marca"      : 3,
                  u"kwietnia"   : 4,
                  u"maja"       : 5,
                  u"czerwca"    : 6,
                  u"lipca"      : 7,
                  u"sierpnia"   : 8,
                  u"września"   : 9,
                  u"października"   : 10,
                  u"listopada"  : 11,
                  u"grudnia"    : 12}
        
        regex_pattern = r"Dodane\s+o \d\d:\d\d, ([^,]+)"
        found = re.search(regex_pattern, offer_html)
        
        # If no date found - return invalid but not harmful year 1900 :)
        if not found:
            return datetime(1900, 1, 1)
   
        date_str = found.group(1).lower()
        day, month_str, year = date_str.split(" ")
        return datetime(int(year), months[month_str], int(day))
    
    
    @staticmethod
    def extract_title(offer_html):
        start_tag = '<meta property="og:title" content="'
        stop_tag = '"/>'
        return OfferExtractor.get_string_between(offer_html, start_tag, stop_tag)
    
    
    @staticmethod
    def extract_address(offer_html):
        start_tag = u'<strong class="c2b small">'
        stop_tag = u'</strong>'
        address = OfferExtractor.get_string_between(offer_html, start_tag, stop_tag)
        return OfferExtractor.strip_from_html_tags(address).strip()
    
    
    @staticmethod
    def extract_description(offer_html):
        start_tag = '<p class="pding10 lheight20 large">'
        stop_tag = '</p>'
        desciption = OfferExtractor.get_string_between(offer_html, start_tag, stop_tag)
        return OfferExtractor.strip_from_html_tags(desciption)


    @staticmethod
    def extract_summary(offer_html):
        start_tag = 'property="og:description" content="'
        stop_tag = '"/>'
        price_and_summary = OfferExtractor.get_string_between(offer_html, start_tag, stop_tag)
        
        # cut out the price, eg. "1 400zł: " beginning
        summary = price_and_summary[price_and_summary.index(":") + 2:] 
        return OfferExtractor.strip_from_html_tags(summary)


    @staticmethod
    def extract_image_url(offer_html):
        start_tag = '<meta property="og:image" content="'
        stop_tag = '"/>'
        return OfferExtractor.get_string_between(offer_html, start_tag, stop_tag)   


    @staticmethod
    def extract_num_rooms(offer_html):
        start_tag = u'Liczba pokoi'
        stop_tag = u'</strong>' 
        
        # extract entire section from html table
        num_rooms_section = OfferExtractor.get_string_between(offer_html, start_tag, stop_tag)
        
        # extract number and label, eg. "2 pokoje"
        number_label = OfferExtractor.strip_from_html_tags(num_rooms_section).strip()
        
        # get the number 
        num_rooms_str = number_label.split()[0] 
        
        if u"Kawalerka" in num_rooms_str:
            return 1
        
        # return numeric
        return int(num_rooms_str)
    
   
    @staticmethod
    def extract_area(offer_html):
        start_tag = 'Powierzchnia'
        stop_tag = '</strong>' 
        
        # extract entire section from html table
        area_section = OfferExtractor.get_string_between(offer_html, start_tag, stop_tag)
        
        # extract area and unit, eg. "55 m"
        area_label = OfferExtractor.strip_from_html_tags(area_section).strip()
        
        # get the number
        area_str = area_label.split()[0]
        
        # return numeric
        return int(area_str)
        
    
    @staticmethod
    def strip_from_html_tags(text):
        return re.sub('<[^<]+>', '', text)
    
    
    @staticmethod
    def get_string_between(source, start, stop):
        i_start = source.find(start) + len(start)
        i_stop = source.find(stop, i_start)
        return source[i_start:i_stop].strip()
        
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
        start_tag = u"<td style='font-weight:bold'>"
        stop_tag = u"</td>"
        return OfferExtractor.get_string_between(offer_html, start_tag, stop_tag)
    
    
    @staticmethod
    def extract_date(offer_html):
        start_tag = u'<td class="first_row" >'
        stop_tag = u'</td>' 
        
        # address format with slash separator, eg. "29/07/2014"
        day, month, year = OfferExtractor.get_string_between(offer_html, start_tag, stop_tag).split("/") 
        return datetime(int(year), int(month), int(day))
    
    
    @staticmethod
    def extract_title(offer_html):
        start_tag = u'<title>'
        stop_tag = u'</title>'
        return OfferExtractor.get_string_between(offer_html, start_tag, stop_tag)
    
    
    @staticmethod
    def extract_address(offer_html):
        start_tag = u'<td itemscope itemtype="http://schema.org/Place">'
        stop_tag = u'</td>'
        address = OfferExtractor.get_string_between(offer_html, start_tag, stop_tag)
        address = address.replace(u"Pokaż mapę", "")
        return OfferExtractor.strip_from_html_tags(address).strip()
    
    
    @staticmethod
    def extract_description(offer_html):
        start_tag = u'<span id="preview-local-desc">'
        stop_tag = u'</span>'
        desciption = OfferExtractor.get_string_between(offer_html, start_tag, stop_tag)
        return OfferExtractor.strip_from_html_tags(desciption)


    @staticmethod
    def extract_summary(offer_html):
        start_tag = u'property="og:description" content="'
        stop_tag = u'"/>'
        summary = OfferExtractor.get_string_between(offer_html, start_tag, stop_tag)
        return OfferExtractor.strip_from_html_tags(summary)


    @staticmethod
    def extract_image_url(offer_html):
        start_tag = u'<meta property="og:image" content="'
        stop_tag = u'"/>'
        return OfferExtractor.get_string_between(offer_html, start_tag, stop_tag)   


    @staticmethod
    def extract_num_rooms(offer_html):
        start_tag = u'Liczba pokoi'
        stop_tag = u'pok' 
        
        # extract entire section from html table
        num_rooms_section = OfferExtractor.get_string_between(offer_html, start_tag, stop_tag)
        
        # extract number and label, eg. "2 pokoje"
        num_rooms_label = OfferExtractor.strip_from_html_tags(num_rooms_section).strip()
        
        # get the number 
        num_rooms_str = num_rooms_label.split()[0]
        if u"Kawalerka" in num_rooms_str:
            return 1
        
        # return numeric
        return int(num_rooms_str)
    
  
    @staticmethod
    def extract_area(offer_html):
        start_tag = u'Wielkość (m2)'
        stop_tag = u'</tr>'
        
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
        
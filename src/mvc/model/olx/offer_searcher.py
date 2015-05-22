# -*- coding: UTF-8 -*-

'''
Created on 24-01-2015

@author: mateusz
'''
import re

class OfferSearcher(object):
    """This class queries OLX for offers and returns list of urls to these offers"""


    @staticmethod
    def search(search_query, max_url_count, web_document_fetcher):
        """This method returns urls generator. To be used in "for...in" construction"""
        
        urls = OfferSearcher(search_query, max_url_count, web_document_fetcher)
        
        # url generator
        while True:
            try:
                yield urls.next_url()
            except StopIteration:
                return
  
  
    def __init__(self, search_query, max_url_count, web_document_fetcher):
        
        # olx search_query 
        self.search_query = search_query 
        
        # max number of urls to return
        self.max_url_count = max_url_count 
        
        # used to fetch html page from url address
        self.web_document_fetcher = web_document_fetcher 
        
        # current url no
        self.curr_url_number = 0 
        
        # url list to return
        self.urls = [] 
        
        # current search result page no, we start from page 1
        self.curr_page = 1 
        
        # is there a next search result page? Start True; there is at least empty page
        self.has_next_page = True 


    def next_url(self):
        # max_url_count hit - stop iteration
        if self.curr_url_number == self.max_url_count:
            raise StopIteration()
        
        # fetch urls if list empty
        if not self.urls:
            self.urls = self.__fetch_urls()

        # check if fetched any urls
        if not self.urls:
            raise StopIteration()
        
        # increase returned url counter
        self.curr_url_number += 1

        # and return url
        return self.urls.pop()
    
    
    def __fetch_urls(self):
        # if no more pages to fetch urls from - stop iteration
        if not self.has_next_page:
            raise StopIteration()

        # add page number to offers search_query
        search_result_page_url = "{0}&page={1}".format(self.search_query, self.curr_page)
        
        # fetch html with offers listed
        html = self.web_document_fetcher.fetch(search_result_page_url)
        self.has_next_page = OfferSearcher.get_has_next_page(html)
        self.curr_page += 1
        
        return OfferSearcher.extract_offer_urls(html)
    
    
    @staticmethod
    def get_has_next_page(html):
        next_page_tag = u'<span>następna &raquo;</span>'
        return next_page_tag in html
    
    
    @staticmethod
    def extract_url_from_href(html):
        pattern = u'a href="([^"]*)'
        return re.search(pattern, html).group(1)
    
    
    @staticmethod
    def extract_offer_urls(html):
        start_tag = '<h3 class="large lheight20 margintop10">'
        stop_tag = ' class="marginright5 link linkWithHash detailsLink">'
        urls = []
        
        i_start = html.find(start_tag)
        while i_start != -1:
            i_stop = html.find(stop_tag, i_start)
    
            # a href=http://...
            href = html[i_start + len(start_tag):i_stop]
    
            # http://...
            url = OfferSearcher.extract_url_from_href(href)
            urls.append(url)
            i_start = html.find(start_tag, i_stop)
    
        return urls

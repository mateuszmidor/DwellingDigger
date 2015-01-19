# -*- coding: UTF-8 -*-

'''
Created on 19-01-2015

@author: mateusz
'''
import re

class SearchOffers():
    """This class querries Gumtree for offers and returns urls to these offers"""
    
    @staticmethod
    def search(search_querry, offer_limit, web_document_fetcher):
        """This method returns generator of urls to be used in for...in construction"""
        
        urls = SearchOffers(search_querry, offer_limit, web_document_fetcher)
        
        # url generator
        while(True):
            try:
                yield urls.__next_url()
            except StopIteration:
                return

    def __init__(self, search_querry, offer_limit, web_document_fetcher):
        self.search_querry = search_querry # gumtree search_querry 
        self.offer_limit = offer_limit # max number of urls to return
        self.web_doc_fetcher = web_document_fetcher # used to fetch html page from url address
        self.curr_url_number = 0 # current url no
        self.urls = [] # url list to return
        self.curr_page = 1 # current offers page no, we start from page 1
        self.has_next_page = True # is there a next page to fetch offers from?

    def __next_url(self):
        # offer_limit hit - stop iteration
        if (self.curr_url_number == self.offer_limit):
            raise StopIteration()
        
        # fetch urls if list empty
        if (not self.urls):
            self.urls = self.__fetch_urls()

        # check if fetched any urls
        if (not self.urls):
            raise StopIteration()
        
        # increase returned url counter
        self.curr_url_number += 1

        # and return url
        return self.urls.pop()
        

    def __fetch_urls(self):
        # if no more pages to fetch urls from - stop iteration
        if (not self.has_next_page):
            raise StopIteration()

        # add page number to offers search_querry
        search_result_page_url = "{0}&Page={1}".format(self.search_querry, self.curr_page)
        
        # fetch html with offers listed
        html = self.web_doc_fetcher.fetch(search_result_page_url)
        self.has_next_page = self.__get_has_next_page(html)
        self.curr_page += 1
        
        return self.__extract_offer_urls(html)
        
    def __get_has_next_page(self, html):
        NEXT_PAGE_TAG = u'class="prevNextLink">Następne'
        return (NEXT_PAGE_TAG in html)
        
    def __extract_url_from_href(self, html):
        pattern = u'a href="([^"]*)'
        return re.search(pattern, html).group(1)
    
    def __extract_offer_urls(self, html):
        START_TAG = '<div class="ar-title">'
        STOP_TAG = '</div>'
        urls = []
        
        i_start = html.find(START_TAG)
        while (i_start != -1):
            i_stop = html.find(STOP_TAG, i_start)
    
            # a href=http://...
            htmlLink = html[i_start + len(START_TAG):i_stop]
    
            # http://...
            url = self.__extract_url_from_href(htmlLink)
            urls.append(url)
            i_start = html.find(START_TAG, i_stop)
    
        return urls
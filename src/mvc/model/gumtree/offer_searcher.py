# -*- coding: UTF-8 -*-

'''
Created on 19-01-2015

@author: mateusz
'''
import re

class OfferSearcher(object):
    """This class queries Gumtree for offers and returns list of urls to these offers"""
    
    
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
        # gumtree search_query as a string that could be put in web browser address bar
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
        return self.urls.pop(0)
        

    def __fetch_urls(self):
        # if no more pages to fetch urls from - stop iteration
        if not self.has_next_page:
            raise StopIteration()

        # add page number to offers search_query
        search_result_page_url = str(self.search_query).format(_page=self.curr_page)
        print search_result_page_url
        # fetch html with offers listed
        html = self.web_document_fetcher.fetch(search_result_page_url)
        self.has_next_page = OfferSearcher.__get_has_next_page(html)
        self.curr_page += 1
        
        return OfferSearcher.__extract_offer_urls(html)
        
        
    @staticmethod
    def __get_has_next_page(html):
        next_page_tag = u'<a class="next follows" href'
        return next_page_tag in html
    
    
    @staticmethod
    def __extract_offer_urls(html):
        start_tag = '<div class="title">'
        stop_tag = '</div>'
        urls = []
        
        i_start = html.find(start_tag)
        while i_start != -1:
            i_stop = html.find(stop_tag, i_start)
    
            # a href=http://...
            href = html[i_start + len(start_tag):i_stop]
    
            # http://...
            url = OfferSearcher.__extract_url_from_href(href)
            full_url = u"http://www.gumtree.pl" + url
            urls.append(full_url)
            i_start = html.find(start_tag, i_stop)
    
        return urls
        
        
    @staticmethod        
    def __extract_url_from_href(html):
        pattern = u'<a class="href-link" href="([^"]*)'
        return re.search(pattern, html).group(1)
    
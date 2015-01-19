'''
Created on 19-01-2015

@author: mateusz
'''
from thirdparty import urllib3

class WebDocumentFetcher(object):
    '''
    This class lets you download document located at given url address.
    '''
    
    @staticmethod
    def fetch (url):
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        return unicode(r.data, "UTF-8")
 
        
'''
Created on 19-01-2015

@author: mateusz
'''
from src.thirdparty import urllib3
from src.diagnostics.method_profiler import MethodProfiler

class WebDocumentFetcher(object):
    '''
    This class lets you download document located at given url address.
    '''
    
    @staticmethod
    @MethodProfiler
    def fetch (url):
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        return unicode(r.data, "UTF-8")
 
        
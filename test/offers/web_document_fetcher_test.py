'''
Created on 19-01-2015

@author: mateusz
'''
import unittest
from offers.web_document_fetcher import WebDocumentFetcher

class WebDocumentFetcherTest(unittest.TestCase):
    '''
    This test requires internet connectivity
    '''
    def test_fetch(self):
        URL = "http://bash.org.pl/random/"
        try:
            html = WebDocumentFetcher.fetch(URL)  # @UnusedVariable
        except Exception as e:
            self.fail("Could not fetch document %s\nTry: check internet connectivity\n%s " % (URL, e.message))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
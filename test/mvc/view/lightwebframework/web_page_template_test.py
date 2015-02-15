'''
Created on 18-01-2015

@author: mateusz
'''
import unittest
from src.mvc.view.lightwebframework.web_page_template import WebPageTemplate

class WebPageTemplateTest(unittest.TestCase):

    def test_set_field(self):
        SOURCE_HTML = "<HTML><HEAD><TITLE>$TITLE$</TITLE></HEAD></HTML>"
        page = WebPageTemplate.from_html_string(SOURCE_HTML)
        page.set_field("$TITLE$", "WebPageTemplateTest")
        
        EXPECTED_HTML = "<HTML><HEAD><TITLE>WebPageTemplateTest</TITLE></HEAD></HTML>"
        self.assertEquals(EXPECTED_HTML, page.get_html_string())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
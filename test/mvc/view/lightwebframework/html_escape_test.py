'''
Created on 07-05-2015

@author: mateusz
'''
import unittest
from src.mvc.view.lightwebframework.html_escape import HtmlEscape


class HtmlEscapeTest(unittest.TestCase):


    def test_escape_ampersand(self):
        STRING = "Tom&Jerry"
        EXPECTED = "Tom&amp;Jerry"
        result = HtmlEscape.escape(STRING)
        self.assertEqual(result, EXPECTED, 
                         "Escaped string should be '%s' but was '%s'" % (EXPECTED, result))
        
        
    def test_escape_quotation(self):
        STRING = 'Really "fast" internet'
        EXPECTED = 'Really &quot;fast&quot; internet'
        result = HtmlEscape.escape(STRING)
        self.assertEqual(result, EXPECTED, 
                         "Escaped string should be '%s' but was '%s'" % (EXPECTED, result))
        
                
    def test_escape_apostrophe(self):
        STRING = "kill'em all"
        EXPECTED = "kill&apos;em all"
        result = HtmlEscape.escape(STRING)
        self.assertEqual(result, EXPECTED, 
                         "Escaped string should be '%s' but was '%s'" % (EXPECTED, result))


    def test_escape_lessthan(self):
        STRING = "4 < 5"
        EXPECTED = "4 &lt; 5"
        result = HtmlEscape.escape(STRING)
        self.assertEqual(result, EXPECTED, 
                         "Escaped string should be '%s' but was '%s'" % (EXPECTED, result))
        
        
    def test_escape_greaterthan(self):
        STRING = "11 > 7"
        EXPECTED = "11 &gt; 7"
        result = HtmlEscape.escape(STRING)
        self.assertEqual(result, EXPECTED, 
                         "Escaped string should be '%s' but was '%s'" % (EXPECTED, result))      
        
        
    def test_escape_newline(self):
        STRING = "line1\nline2"
        EXPECTED = "line1<br />line2"
        result = HtmlEscape.escape(STRING)
        self.assertEqual(result, EXPECTED, 
                         "Escaped string should be '%s' but was '%s'" % (EXPECTED, result))   
           
           
    def test_escape_cr(self):
        STRING = "line\rline"
        EXPECTED = "lineline"
        result = HtmlEscape.escape(STRING)
        self.assertEqual(result, EXPECTED, 
                         "Escaped string should be '%s' but was '%s'" % (EXPECTED, result))   
        
    
    def test_escape_nbsp(self):
        STRING = u"line\u00a0line"
        EXPECTED = u"line&nbsp;line"
        result = HtmlEscape.escape(STRING)
        self.assertEqual(result, EXPECTED, 
                         "Escaped string should be '%s' but was '%s'" % (EXPECTED, result)) 
        
    def test_tabulator(self):
        STRING = "left\tright"
        EXPECTED = "left&#09right"
        result = HtmlEscape.escape(STRING)
        self.assertEqual(result, EXPECTED, 
                         "Escaped string should be '%s' but was '%s'" % (EXPECTED, result)) 
        
    def test_backspace(self):
        STRING = "left \b right"
        EXPECTED = "left  right"
        result = HtmlEscape.escape(STRING)
        self.assertEqual(result, EXPECTED, 
                         "Escaped string should be '%s' but was '%s'" % (EXPECTED, result)) 
 
    def test_form_feed(self):
        STRING = "left \f right"
        EXPECTED = "left  right"
        result = HtmlEscape.escape(STRING)
        self.assertEqual(result, EXPECTED, 
                         "Escaped string should be '%s' but was '%s'" % (EXPECTED, result)) 
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
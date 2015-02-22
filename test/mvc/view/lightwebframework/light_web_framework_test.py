'''
Created on 21-02-2015

@author: mateusz
'''
import unittest
from mock import patch, Mock
from src.mvc.view.lightwebframework.light_web_framework import LightWebFramework


class LightWebFrameworkTest(unittest.TestCase):

    # Important note to patch: patch where the object is used, not where it comes from
    # In this case it is used in light_web_framework, and there we patch it
    @patch('src.mvc.view.lightwebframework.light_web_framework.WebPageTemplate')
    def test_render_page_as_file(self, wpt_mock):
        """ 
        Check if the facade first gets a page using WebPageTemplate.from_file,
        then sets the template field using set_field,
        and then saves the page using page.save_to_file
        """
        # Prepare mocks
        page = Mock()
        page.set_field = Mock()
        page.save_to_file = Mock()
        wpt_mock.from_file = Mock(return_value = page)
        
        # Run the method
        LightWebFramework.render_page_as_file("input.html", "output.html", {"key" : "value"})
        
        # Assert the proper scenario has been executed (load-setfield-save)
        wpt_mock.from_file.assert_called_once_with("input.html")
        page.set_field.assert_called_once_with("key", "value")
        page.save_to_file.assert_called_once_with("output.html")


    def test_render_page_as_http_response(self):
        """
        This test fails when render_page_as_http_response gets finally implemented,
        so we dont forget writing a test for it :) 
        """
        try:
            LightWebFramework.render_page_as_http_response("input.html", {"key" : "value"})
            self.fail("LightWebFramework.render_page_as_http_response doesnt throw NotImplementedError anymore?" +
                      "Update this test, then!")
        except NotImplementedError:
            pass
            
                
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_render_page_as_file']
    unittest.main()
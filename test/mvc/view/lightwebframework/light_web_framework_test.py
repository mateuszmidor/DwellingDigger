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


    @patch('src.mvc.view.lightwebframework.light_web_framework.WebPageTemplate')
    @patch('src.mvc.view.lightwebframework.light_web_framework.HttpResponse')
    def test_render_page_as_http_response(self, httpresponse_mock, wpt_mock):
        """ 
        Check if the facade first gets a page using WebPageTemplate.from_file,
        then sets the template field using set_field,
        and then retrieves the page contents using page.get_html_string,
        and then render the contents using HttpResponse.renderPag
        """
        # Prepare mocks
        httpresponse_mock.renderPage = Mock()
        
        page = Mock()
        page.set_field = Mock()
        page.get_html_string = Mock(return_value = "html_string")
        wpt_mock.from_file = Mock(return_value = page)
        
        # Run the method
        LightWebFramework.render_page_as_http_response("input.html", {"key" : "value"})

        # Assert the proper scenario has been executed (load-setfield-render)
        wpt_mock.from_file.assert_called_once_with("input.html")
        page.set_field.assert_called_once_with("key", "value")
        page.get_html_string.assert_called_once_with()
        httpresponse_mock.renderPage.assert_called_once_with("html_string")        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_render_page_as_file']
    unittest.main()
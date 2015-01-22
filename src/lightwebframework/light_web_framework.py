'''
Created on 18-01-2015

@author: mateusz
FACADE. All needed functionality from lightwebframework you can find here
'''
from web_page_template import WebPageTemplate

class LightWebFramework(object):
    '''
    This class is facade for lightwebframework package.
    '''

    @staticmethod
    def __load_and_fill_template_page(html_template_filename, name_value_pairs):
        page = WebPageTemplate.from_file(html_template_filename)
        for name, value in name_value_pairs.items():
            page.set_field(name, value)
        return page

    @staticmethod
    def render_page_as_file(input_template_filename, output_page_filename, template_name_value_pairs):
        page = LightWebFramework.__load_and_fill_template_page(input_template_filename, template_name_value_pairs)  
        page.save_to_file(output_page_filename)
        
    @staticmethod
    def render_page_as_http_response(html_template_filename, template_name_value_pairs):
        raise NotImplementedError()
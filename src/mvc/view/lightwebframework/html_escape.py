'''
Created on 06-05-2015

@author: mateusz
'''

class HtmlEscape(object):
    '''
    This class escapes special characters to HTML equivalents
    '''


    @staticmethod
    def escape(text):
        html_escape_table = {
                               u"\u00a0"    : u"&nbsp;",
                               u"&": u"&amp;",
                               u'"': u"&quot;",
                               u"'": u"&apos;",
                               u">": u"&gt;",
                               u"<": u"&lt;",
                               u"\n" : u"<br />",
                               u"\r" : u"",
                                } 
        return u"".join(html_escape_table.get(c,c) for c in text)       
        
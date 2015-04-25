'''
Created on 23 kwi 2015

@author: m.midor
'''
import unittest
from mock import patch
from src.mvc.view.lightwebframework.user_agent import UserAgent


class DictStub(object):
    ''' This guy is used to stub "os.environ" dictionary '''
    def __init__(self, return_value):
        self.return_value = return_value
        
    def __getitem__(self, key):    
        ''' Always return the same value. This is what we need '''
        return self.return_value
    
     

class UserAgentTest(unittest.TestCase):

    @patch("src.mvc.view.lightwebframework.user_agent.os")
    def test_recognizes_mobile(self, os_mock):
        EXAMPLE_MOBILE_AGENTS = ("Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
                                  "Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+",
                                  "SamsungI8910/SymbianOS/9.1 Series60/3.0",
                                  "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC6-00/20.0.042; Profile/MIDP-2.1 Configuration/CLDC-1.1; zh-hk) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.2.6.9 3gpp-gba",
                                  "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
                                  "MOT-L7/NA.ACR_RB MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1",
                                  "Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54",
                                  "Opera/12.02 (Android 4.1; Linux; Opera Mobi/ADR-1111101157; U; en-US) Presto/2.9.201 Version/12.02",
                                  "SonyEricssonW800i/R1BD001/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1")
       
        for agent in EXAMPLE_MOBILE_AGENTS:
            os_mock.environ = DictStub(agent)
            self.assertTrue(UserAgent.is_mobile(), "is_mobile() should return true for '%s'" % agent)


    @patch("src.mvc.view.lightwebframework.user_agent.os")
    def test_recognizes_nonmobile(self, os_mock):
        EXAMPLE_DESKTOP_AGENTS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
                                  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
                                  "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2",
                                  "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
                                  "Mozilla/5.0 (X11; Linux) KHTML/4.9.1 (like Gecko) Konqueror/4.9",
                                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; MyIE2; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0)",
                                  "Mozilla/5.0 (X11; U; Linux i686; pt-BR) AppleWebKit/533.3 (KHTML, like Gecko) Navscape/Pre-0.2 Safari/533.3",
                                  "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
                                  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A")
       
        for agent in EXAMPLE_DESKTOP_AGENTS:
            os_mock.environ = DictStub(agent)
            self.assertFalse(UserAgent.is_mobile(), "is_mobile() should return false for '%s'" % agent)

        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
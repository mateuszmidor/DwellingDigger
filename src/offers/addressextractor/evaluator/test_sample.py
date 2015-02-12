'''
Created on 6 lut 2015

@author: m.midor
'''

class TestSample(object):
    '''
    This class represents a test sample ie. a bunch of address sources and the
    best address string that can be extracted from the sources
    '''
    date = None
    sources = []
    expected_result = u""
    
    def __init__(self):
        self.date = None
        self.sources = []
        self.expected_result = u""        

    def __unicode__(self):
        s = u"\n".join(self.sources)
        s += u"\nexpected: " + self.expected_result
        return s
   
        
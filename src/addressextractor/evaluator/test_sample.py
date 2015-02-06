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
    expected_result = ""
    

    def __str__(self):
        s = "\n".join(self.sources)
        s += "\nexpected: " + self.expected_result
        return s
   
        
'''
Created on 20 maj 2015

@author: m.midor
'''

class OfferProcessingException(Exception):
    '''
    This class represents an exception that may occur during processing offer from external source like gumtree or olx
    '''


    def __init__(self, offer_url, chained_exception = None):
        exception_description = u"Exception during processing offer %s" % offer_url
        super(OfferProcessingException, self).__init__(exception_description, chained_exception)
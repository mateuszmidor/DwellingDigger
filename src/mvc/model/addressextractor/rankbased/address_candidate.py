'''
Created on 03-02-2015

@author: mateusz
'''

class AddressCandidate(object):
    '''
    This class represents an extracted address candidate.
    Extraction can yield many results, such as city name, district name, street name.
    The address candidate can be ranked in two areas.
    Street with number has highest precision_rank.
    City has lowest precision_rank.
    Based on context, the correctness_rank is evaluated, eg "ul. Wielicka 23" will have 
    higher correctness_rank than just "wielicka" (based on keyword "ul.", number, capital letter)
    
    @author m.midor
    '''
    
    def __init__(self):
        self.address = u""    # the address itself, eg "Wyslouchow"
        self.full_form_address = u"" # the full form of the address, eg "ul. Marii i Boleslawa Wyslouchow"
        self.source = u""     # string where the address was found
        self.correctness_rank = 0    # how sure we are this address is correct?
        self.precision_rank = 0      # how precise (valuable to us) this address is?
        
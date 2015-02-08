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
    address = u""    # the address itself
    source = u""     # string where the address was found
    correctness_rank = 0    # how sure we are this address is correct?
    precision_rank = 0      # how precise (valuable to us) this address is?
        
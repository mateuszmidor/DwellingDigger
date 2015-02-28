'''
Created on 08-02-2015

@author: mateusz
'''
from src.mvc.model.addressextractor.evaluator.test_samples import TestSamples
from src.mvc.model.addressextractor.rankbased.address_candidates import AddressCandidates

class Evaluator(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    @staticmethod
    def evaluate(address_extractor):
        samples = TestSamples.from_file("DwellingDigger/data/test_samples_krakow.txt")
        num_correctly_extracted = 0
        
        for sample in samples:
            address = address_extractor.extract(sample.sources)
            expected = sample.expected_result

            if Evaluator.__contains_ignore_case(expected, address.strip(u"ul. ")):
                num_correctly_extracted += 1
            else:
                print(unicode(AddressCandidates.last_processed))
                print(unicode(sample))
                print(u"Found address: %s" % address)
                print(u"")

        print(u"Num samples: %s" % len(samples))
        print(u"Num found: %s" % num_correctly_extracted)
        print(u"Effectiveness: %i%%" % (100 * num_correctly_extracted / len(samples))) 
        
    @staticmethod
    def __contains_ignore_case(s1, s2):
        return s2.lower() in s1.lower()
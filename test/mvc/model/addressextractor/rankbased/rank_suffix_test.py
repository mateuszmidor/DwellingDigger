'''
Created on 5 lut 2015

@author: m.midor
'''
import unittest
from src.mvc.model.addressextractor.rankbased.address_candidates import AddressCandidates
from src.mvc.model.addressextractor.rankbased.address_candidate import AddressCandidate
from src.mvc.model.addressextractor.rankbased.rank_suffix import RankSuffix


class RankSuffixTest(unittest.TestCase):


    def test_rank_suffix(self):
        candidate = AddressCandidate()
        candidate.address = "Wielicka"
        candidate.full_form_address = "ul. Wielicka 24B"
        candidates = AddressCandidates()
        candidates.append(candidate)
        
        r = RankSuffix()
        r.rank(candidates)
        self.assertEqual(candidate.correctness_rank, 1, "Based on having suffix number, 'Wielicka 24' should be ranked 1 for correctness but was ranked {0}".format(candidate.correctness_rank))
        self.assertEqual(candidate.precision_rank, 1, "Based on having suffix number, 'Wielicka 24' should be ranked 1 for precision but was ranked {0}".format(candidate.precision_rank))


    def test_rank_nosuffix(self):
        candidate = AddressCandidate()
        candidate.address = "Wielicka"
        candidate.full_form_address = "ul. Wielicka"
        candidates = AddressCandidates()
        candidates.append(candidate)
        
        r = RankSuffix()
        r.rank(candidates)
        self.assertEqual(candidate.correctness_rank, 0, "Based on having no suffix number, 'Wielicka' should be ranked 0 for correctness but was ranked {0}".format(candidate.correctness_rank))
        self.assertEqual(candidate.precision_rank, 0, "Based on having no suffix number, 'Wielicka' should be ranked 0 for precision but was ranked {0}".format(candidate.precision_rank))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
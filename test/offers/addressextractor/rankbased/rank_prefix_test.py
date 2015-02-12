'''
Created on 5 lut 2015

@author: m.midor
'''
import unittest
from src.offers.addressextractor.rankbased.address_candidate import AddressCandidate
from src.offers.addressextractor.rankbased.address_candidates import AddressCandidates
from src.offers.addressextractor.rankbased.rank_prefix import RankPrefix


class RankPrefixTest(unittest.TestCase):


    def test_rank_street(self):
        candidate = AddressCandidate()
        candidate.address = "Wielicka"
        candidate.source = "Nowe mieszkanie ul. Wielicka TANIO"
        candidates = AddressCandidates()
        candidates.append(candidate)
        
        r = RankPrefix()
        r.rank(candidates)
        self.assertEqual(candidate.correctness_rank, 1, "Based on having meaningful prefix, 'ul. Wielicka' should be ranked 1 for correctness but was ranked {0}".format(candidate.correctness_rank))
        self.assertEqual(candidate.precision_rank, 3, "Based on having meaningful prefix, 'ul. Wielicka' should be ranked 3 for precision but was ranked {0}".format(candidate.precision_rank))
       
    
    def test_rank_district(self):
        candidate = AddressCandidate()
        candidate.address = "Na Stoku"
        candidate.source = "Nowe mieszkanie os. Na Stoku TANIO"
        candidates = AddressCandidates()
        candidates.append(candidate)
        
        r = RankPrefix()
        r.rank(candidates)
        self.assertEqual(candidate.correctness_rank, 1, "Based on having meaningful prefix, 'os. Na Stoku' should be ranked 1 for correctness but was ranked {0}".format(candidate.correctness_rank))
        self.assertEqual(candidate.precision_rank, 2, "Based on having meaningful prefix, 'os. Na Stoku' should be ranked 2 for precision but was ranked {0}".format(candidate.precision_rank))
       
    
    def test_rank_whereabouts(self):
        candidate = AddressCandidate()
        candidate.address = "Ruczaj"
        candidate.source = "Nowe mieszkanie na Ruczaju TANIO"
        candidates = AddressCandidates()
        candidates.append(candidate)
        
        r = RankPrefix()
        r.rank(candidates)
        self.assertEqual(candidate.correctness_rank, 1, "Based on having meaningful yet not precise prefix, 'na Ruczaju' should be ranked 1 for correctness but was ranked {0}".format(candidate.correctness_rank))
        self.assertEqual(candidate.precision_rank, 0, "Based on having meaningful yet not precise prefix, 'na Ruczaju' should be ranked 0 for precision but was ranked {0}".format(candidate.precision_rank))
       
    
    def test_rank_noprefix(self):
        candidate = AddressCandidate()
        candidate.address = "Wielicka"
        candidate.source = "Nowe mieszkanie Wielicka TANIO"
        candidates = AddressCandidates()
        candidates.append(candidate)
        
        r = RankPrefix()
        r.rank(candidates)
        self.assertEqual(candidate.correctness_rank, 0, "Based on having no meaningful prefix, 'Wielicka' should be ranked 0 for correctness but was ranked {0}".format(candidate.correctness_rank))
        self.assertEqual(candidate.precision_rank, 0, "Based on having no meaningful prefix, 'Wielicka' should be ranked 0 for precision but was ranked {0}".format(candidate.precision_rank))
       


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
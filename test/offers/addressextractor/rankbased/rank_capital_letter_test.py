'''
Created on 5 lut 2015

@author: m.midor
'''
import unittest
from src.offers.addressextractor.rankbased.address_candidate import AddressCandidate
from src.offers.addressextractor.rankbased.address_candidates import AddressCandidates
from src.offers.addressextractor.rankbased.rank_capital_letter import RankCapitalLetter


class RankCapitalLetterTest(unittest.TestCase):


    def test_rank_capital_letter(self):
        candidate = AddressCandidate()
        candidate.address = "Wielicka"
        candidates = AddressCandidates()
        candidates.append(candidate)
        
        r = RankCapitalLetter()
        r.rank(candidates)
        self.assertEqual(candidate.correctness_rank, 1, "Based on capital letter, 'Wielicka' should be ranked 1 but was ranked {0}".format(candidate.correctness_rank))


    def test_rank_nocapital_letter(self):
        candidate = AddressCandidate()
        candidate.address = "wielicka"
        candidates = AddressCandidates()
        candidates.append(candidate)
        
        r = RankCapitalLetter()
        r.rank(candidates)
        self.assertEqual(candidate.correctness_rank, 0, "Based on no capital letter, 'wielicka' should be ranked 0 but was ranked {0}".format(candidate.correctness_rank))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

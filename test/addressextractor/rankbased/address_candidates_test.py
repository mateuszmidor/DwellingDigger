'''
Created on 03-02-2015

@author: mateusz
'''
import unittest
from src.addressextractor.rankbased.address_candidates import AddressCandidates
from src.addressextractor.rankbased.address_candidate import AddressCandidate

class AddressCandidatesTest(unittest.TestCase):

    def test_sort_by_correctness_precision(self):
        candidates = AddressCandidates()
        
        a = AddressCandidate()
        a.correctness_rank = 1
        a.precision_rank = 1
        candidates.append(a)
        
        b = AddressCandidate()
        b.correctness_rank = 1
        b.precision_rank = 2
        candidates.append(b)
        
        c = AddressCandidate()
        c.correctness_rank = 2
        c.precision_rank = 2
        candidates.append(c)
        
        candidates.sort_by_correctness_precision()
        
        self.assertEqual(c, candidates[0], "Highest ranked address candidate not found on first position")
        self.assertEqual(b, candidates[1], "Medium ranked address candidate not found on second position")
        self.assertEqual(a, candidates[2], "Lowest ranked address candidate not found on third position")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
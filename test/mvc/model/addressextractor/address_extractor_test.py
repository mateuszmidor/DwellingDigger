'''
Created on 22-02-2015

@author: mateusz
'''
import unittest
from src.mvc.model.addressextractor.address_extractor import AddressExtractor
from mock import patch, Mock, call


class AddressExtractorTest(unittest.TestCase):

    @patch('src.mvc.model.addressextractor.address_extractor.Surnamenator')
    @patch('src.mvc.model.addressextractor.address_extractor.Declinator')
    @patch('src.mvc.model.addressextractor.address_extractor.Asciinator')
    @patch('src.mvc.model.addressextractor.address_extractor.Dictionary')
    @patch('src.mvc.model.addressextractor.address_extractor.RankBasedExtractor')
    def test_rank_based(self, extractor_mock, dictionary_mock, asciinator_mock, declinator_mock, surnamenator_mock):
        """ 
        Check if input dictionaries are properly prepared before providing them to RankBasedExtractor(dictionaries)
        """
        
        # Prepare mocks
        # dictionary instances (streets, disctricts)
        d1 = Mock() 
        d2 = Mock()
        
        # Dictionary class 
        dictionary_mock.from_file = Mock(side_effect = [d1, d2])
        
        # dictionary mutators
        asciinator_mock.asciinate_dictionary = Mock()
        declinator_mock.declinate_dictionary = Mock()
        surnamenator_mock.surnamenate_dictionary = Mock()
        
        # Run tested method
        AddressExtractor.rank_based(["streets.dat", "districts.dat"])
        
        # Check the scenario properly played
        d1.sort_longest_first.assert_called_once_with()
        d2.sort_longest_first.assert_called_once_with()
        dictionary_mock.assert_has_calls([call.from_file("streets.dat"), call.from_file("districts.dat")])
        asciinator_mock.assert_has_calls([call.asciinate_dictionary(d1), call.asciinate_dictionary(d2)])
        declinator_mock.assert_has_calls([call.declinate_dictionary(d1), call.declinate_dictionary(d2)])
        surnamenator_mock.assert_has_calls([call.surnamenate_dictionary(d1), call.surnamenate_dictionary(d2)])
        extractor_mock.assert_called_once_with(d1, d2)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
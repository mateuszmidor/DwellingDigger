'''
Created on 22-02-2015

@author: mateusz
'''
import unittest
from src.mvc.model.addressextractor.address_extractor import AddressExtractor
from mock import patch, Mock, call
from src.mvc.model.addressextractor.rankbased.dictionary import Dictionary


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
        # dictionary instances returned by "from_file" [strets, districts]
        d1 = Mock() 
        d2 = Mock()
        
        # Dictionary class 
        dictionary_mock.from_file = Mock(side_effect = [d1, d2])
        # dictionary instance returned by constructor "Dictionary()"
        d3 = Mock()
        dictionary_mock.return_value = d3
        
        # dictionary mutators
        asciinator_mock.asciinate_dictionary = Mock()
        declinator_mock.declinate_dictionary = Mock()
        surnamenator_mock.surnamenate_dictionary = Mock()
        
        # Run tested method
        AddressExtractor.rank_based([("streets.dat", Dictionary.STREET),
                                     ("districts.dat", Dictionary.DISTRICT)])
        
        # Check the scenario properly played
        d3.assert_has_calls([call.extend(d1), call.extend(d2)])
        d3.sort_longest_first.assert_called_once_with()
        
        # any_order since dictionary_mock has also the constructor and extend() and sort_longest_first called
        dictionary_mock.assert_has_calls([call.from_file("streets.dat", Dictionary.STREET), 
                                          call.from_file("districts.dat", Dictionary.DISTRICT)],
                                          any_order=True)
        asciinator_mock.asciinate_dictionary.assert_called_once_with(d3)
        declinator_mock.declinate_dictionary.assert_called_once_with(d3)
        surnamenator_mock.surnamenate_dictionary.assert_called_once_with(d3)
        extractor_mock.assert_called_once_with(d3)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
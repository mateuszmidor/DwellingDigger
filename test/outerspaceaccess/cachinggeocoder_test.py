'''
Created on 12-03-2015

@author: mateusz
'''
import unittest
from mock import patch, Mock
from src.outerspaceaccess.cachinggeocoder import CachingGeocoder


class CachingGeocoderTest(unittest.TestCase):


    @patch('src.outerspaceaccess.cachinggeocoder.Geocoder')
    @patch('src.outerspaceaccess.cachinggeocoder.ExclusiveCacheFile')
    def test_geocode_cached_addr(self, cache_file, geocoder):
        "Check that CachingGeocoder gets the geocoding from cache if it is there"
        
        # prepare mocks
        cache_file.read_or_empty = Mock(return_value={"A" : "addressA", "B" : "addressB"})
        geocoder.geocode = Mock(return_value = "should_never_be_called")
         
        # run test scenario
        geocoder = CachingGeocoder("dummy_cache_file.txt")
        
        # check results
        self.assertEqual(geocoder.geocode("A"), "addressA", "geocoder(A) should return addressA")
        self.assertEqual(geocoder.geocode("B"), "addressB", "geocoder(B) should return addressB")
        

    @patch('src.outerspaceaccess.cachinggeocoder.Geocoder')
    @patch('src.outerspaceaccess.cachinggeocoder.ExclusiveCacheFile')
    def test_geocode_noncached_addr(self, cache_file, geocoder):
        "Check that CachingGeocoder runs Geocoder.geocode(addr) if addr not in cache"
        
        # prepare mocks
        cache_file.read_or_empty = Mock(return_value={})
        
        def geocode(addr):
            d = {"A" : "addressA", "B" : "addressB"}
            return d[addr]
        
        geocoder.geocode = Mock(side_effect = geocode)
        
        # run test scenario
        caching_geocoder = CachingGeocoder("dummy_cache_file.txt")
        
        # check results
        self.assertEqual(caching_geocoder.geocode("A"), "addressA", "geocoder(A) should return addressA")
        geocoder.geocode.assert_called_with("A")
       
        self.assertEqual(caching_geocoder.geocode("B"), "addressB", "geocoder(B) should return addressB")
        geocoder.geocode.assert_called_with("B")
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_geocode_cached']
    unittest.main()
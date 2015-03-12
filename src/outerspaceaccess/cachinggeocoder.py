'''
Created on 14-02-2015

@author: mateusz
'''
from src.outerspaceaccess.geocoder import Geocoder
from src.outerspaceaccess.exclusive_cache_file import ExclusiveCacheFile

class CachingGeocoder(object):
    '''
    This class geocodes addresses and stores results in cache file
    to speed up geocoding next time the same address appears.
    '''
    
    def __init__(self, cache_filename):
        self.__cache_filename = cache_filename
        
        # read the cache dictionary from file
        self.__cache = self.try_read_cache_file(cache_filename)
        
        # __extending_cache is where we store new geocodings
        self.__extending_cache = dict()        
        

    def __del__(self):
        """ Update the cache file with new geocodings """
        self.try_update_cache_file(self.__cache_filename, self.__extending_cache)
        
        
    def try_read_cache_file(self, filename):
        """ 
        Reads cache as dict from file.
        If no file exists - returns empty dict.
        """
         
        d = ExclusiveCacheFile.read_or_empty(filename)
        print ("Num addresses read from cache file: %d" % len(d))
        return d
        
         
    def try_update_cache_file(self, filename, update_dict):
        """ 
        Updates cache file with new geocodings.
        Gives up if can't open the cache file exclusively in 3 seconds.
        """
        # try for 3 seconds to exclusive lock the cache file
        FILE_LOCK_TIMEOUT = 3
        print ("Num new addresses: %d" % len(update_dict))
        ExclusiveCacheFile.new_or_update(filename, update_dict, FILE_LOCK_TIMEOUT)
        

    def geocode(self, address):
        if address in self.__cache:
            print("returnig geocoding from cache")
            return self.__cache[address]
        
        if address in self.__extending_cache:
            print("returnig geocoding from extending cache")
            return self.__extending_cache[address]
        
        print("new geocoding started")
        coords = Geocoder.geocode(address)
        self.__extending_cache[address] = coords            
        return coords
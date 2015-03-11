'''
Created on 14-02-2015

@author: mateusz
'''
from src.outerspaceaccess.geocoder import Geocoder
from src.thirdparty.portalocker import portalocker
from src.thirdparty.portalocker.utils import Lock
import json
import os.path

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
        self.try_update_cache_file(self.__cache_filename)
        
        
    def try_read_cache_file(self, filename):
        """ 
        Reads cache as dict from file.
        If no file exists - returns empty dict.
        """
        
        # if no such file - return empty dict
        if not os.path.isfile(filename):
            print("File %s not exist. Returning empty cache dictionary" % filename)
            return dict()
         
        with open(filename, "r") as f:
            # make sure no one writes to the cache file while we read
            portalocker.lock(f, portalocker.LOCK_SH)
            d = json.load(f)
            print ("Num addresses read from cache file: %d" % len(d))
            return d
            # the file will be automatically closed and thus unlocked
        
         
    def try_update_cache_file(self, filename):
        """ 
        Updates cache file with new geocodings.
        Gives up if can't open the cache file exclusively in 3 seconds.
        """
        # try for 3 seconds to exclusive lock the cache file
        FILE_LOCK_TIMEOUT = 3
        
        print ("try update cache file started")
        
        # any new contents to update the cache file with?
        if not self.__extending_cache:
            print ("no new contents to update the cache file")
            return
        
        # read the cache file to get the latest contents
        cache = self.try_read_cache_file(filename)
        cache.update(self.__extending_cache)
        
        print ("Num new geocodings: %d" % len(self.__extending_cache))
            
        # try lock and update
        print("trying update the cache file..")
        with Lock(filename, fail_when_locked=False, timeout=FILE_LOCK_TIMEOUT) as f:
            json.dump(cache, f)
            print("made it")
            return
        
        print("couldnt exclusivel lock the file; cache file not updated")
                   

    def geocode(self, address):
        if address in self.__cache:
            print("returnig geocoding from cache")
            return self.__cache[address]
        
        if address in self.__extending_cache:
            print("returnig geocoding from extending cache")
            return self.__extending_cache
        
        print("new geocoding started")
        coords = Geocoder.geocode(address)
        self.__extending_cache[address] = coords            
        return coords
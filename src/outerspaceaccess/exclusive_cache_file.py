'''
Created on 12 mar 2015

@author: m.midor
'''
from src.thirdparty.portalocker import portalocker
import json
import os
from portalocker.utils import Lock

class ExclusiveCacheFile(object):
    '''
    This class represents a cache file that allows reading and updating the file contents.
    The structure used to store cache data is a dict.
    The class can be used by concurrent processes - it uses file locking mechanism to synchronize access:
    1. For reading - it shared-locks the file
    2. For updating- it exclusively-locks the file
    '''
        
    @staticmethod
    def read_or_empty(filename):
        """ Read the cache dict from file if it exists, return empty dict otherwise """
        
        # if no such file - return empty dict
        if not os.path.isfile(filename):
            return dict()
                
        with open(filename, "r") as f:
            # make sure no one writes to the file while we read
            portalocker.lock(f, portalocker.LOCK_SH)
            return json.load(f)
            # the file will be automatically closed and thus unlocked        
        
        
    @staticmethod
    def new_or_update(filename, update_dict, timeout_seconds):
        """ 
        Create new cache file if doesnt exist yet, update existing otherwise.
        Give up updating if cant get exclusive access in <timeout_seconds>
        """
        
        # anything to put in the file?
        if not update_dict:
            return
        
        if os.path.isfile(filename):
            ExclusiveCacheFile.__update_existing_cachefile(filename, update_dict, timeout_seconds)
        else:
            ExclusiveCacheFile.__create_new_cachefile(filename, update_dict)
        

    @staticmethod
    def __create_new_cachefile(filename, cache):
        """
        Dump the cache to new file or overwrite existing one.
        Assumed the cache is not empty.
        """
        
        # create and exclusively lock the file 
        with Lock(filename, fail_when_locked=False) as f:
            # save new contents to the file
            json.dump(cache, f)
            return
            
            
    @staticmethod
    def __update_existing_cachefile(filename, update_dict, timeout_seconds):
        """ 
        Update the cache file if exclusive lock can be acquired, timeout otherwise.
        Assumed that file exists and update_dict is not empty
        """

        # try lock and update
        with Lock(filename, mode='r+', truncate=None, fail_when_locked=False, timeout=timeout_seconds) as f:
            # read original cache contents
            cache = json.load(f)
            
            # add new contents to original contents
            cache.update(update_dict)
            
            # empty the file
            f.truncate(0)
            f.seek(0)
            
            # save updated contents to the file
            json.dump(cache, f)
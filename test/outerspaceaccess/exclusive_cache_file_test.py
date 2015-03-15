'''
Created on 13-03-2015

@author: mateusz
'''
import os
import threading
import time
import unittest

from src.outerspaceaccess.exclusive_cache_file import ExclusiveCacheFile
from src.thirdparty.portalocker import portalocker
from src.thirdparty.portalocker.portalocker import LockException
from multiprocessing.synchronize import Event


class ExclusiveCacheFileTest(unittest.TestCase):
    """
    Recognized testcases:
    1. Trying to read cache file but the file doesn't exist.
    2. Trying to read cache file and the file exists.
    3. Trying to read cache file but it is shared-locked since being read by another thread.
    4. Trying to read cache file but it is exclusively-locked since being written by another thread.
    5. Trying to update cache file but it doesn't exist yet.
    6. Trying to update cache file that exists.
    7. Trying to update cache file but it is shared-locked since being read by another thread. Success
    8. Trying to update cache file but it is exclusively-locked since being written by another thread. Success
    9. Trying to update cache file but it is exclusively-locked since being written by another thread. Fail-timeout
    """
    
    FILENAME = "file"
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        with open(ExclusiveCacheFileTest.FILENAME, 'w') as f:
            f.write('{"A": "Anna"}')
            
    def tearDown(self):
        os.remove("file")
        unittest.TestCase.tearDown(self)
        
        
    def test_read_file_doesnt_exist(self):
        "Test case 1."
         
        d = ExclusiveCacheFile.read_or_empty("nonexisting_file")
        
        self.assertTrue(isinstance(d, dict), "Returned cache should be a dictionary")
        self.assertTrue(not d, "Should return empty cache if the cache file doesnt exist")
 
     
    def test_read_file_exists(self):
        "Test case 2."
          
        d = ExclusiveCacheFile.read_or_empty(ExclusiveCacheFileTest.FILENAME)
          
        self.assertTrue(isinstance(d, dict), "Returned cache should be a dictionary")
        self.assertTrue("A" in d, "Key 'A' should have been read from cache file")
        self.assertEqual(d["A"], "Anna", "For key 'A' there should be 'Anna' in cache that was read from file")
#          
#          
    def test_read_sharelocked(self):
        "Test case 3."
    
        LOCK_SECS = 0.1
              
        # shared lock the file
        ExclusiveCacheFileTest.lock_file_for_delay(ExclusiveCacheFileTest.FILENAME, LOCK_SECS, portalocker.LOCK_SH)
          
        # calc the waiting time before ExclusiveCacheFile reads the file
        start = time.time()
        d = ExclusiveCacheFile.read_or_empty(ExclusiveCacheFileTest.FILENAME)
        stop = time.time()
        delay_secs = stop - start
  
        # sleep the lock time so file gets unlocked and can be removed in tearDown
        time.sleep(LOCK_SECS) 
  
        # check there was no delay_secs 
        self.assertTrue(delay_secs < 0.01, "There should be no waiting for reading sharedlocked file: %fsec" % delay_secs)
          
        # check file was properly read
        self.assertTrue("A" in d, "Key 'A' should have been read from cache file")
        self.assertEqual(d["A"], "Anna", "For key 'A' there should be 'Anna' in cache that was read from file")
          
          
    def test_read_exclusivelocked(self):
        "Test case 4."
    
        LOCK_SECS = 0.1
          
        # exclusively lock the file
        ExclusiveCacheFileTest.lock_file_for_delay(ExclusiveCacheFileTest.FILENAME, LOCK_SECS, portalocker.LOCK_EX)
          
        # calc the waiting time before ExclusiveCacheFile reads the file
        start = time.time()
        d = ExclusiveCacheFile.read_or_empty(ExclusiveCacheFileTest.FILENAME)
        stop = time.time()
        delay_secs = stop - start
  
        # sleep the lock time in case didnt wait and will fail in next line
        time.sleep(LOCK_SECS)
           
        # check there was a proper delay
        self.assertTrue(0.5*LOCK_SECS < delay_secs < 1.5*LOCK_SECS, 
                        "There should be ~%fsec waiting for reading exclusively locked file, but was %fsec" % 
                        (LOCK_SECS, delay_secs))
          
        # check file was properly read
        self.assertTrue("A" in d, "Key 'A' should have been read from cache file")
        self.assertEqual(d["A"], "Anna", "For key 'A' there should be 'Anna' in cache that was read from file")
          
          
    def test_update_doesnt_exist(self):
        """ Test case 5. """
          
        FILENAME = "testcase5_file"
        WAIT_SECS = 0.1
          
        # check file not exists 
        self.assertTrue(not os.path.isfile(FILENAME), "File %s should not exist yet!" % FILENAME)
          
        # create the file with contents
        ExclusiveCacheFile.new_or_update(FILENAME, {"A" : "Anna"}, WAIT_SECS)
          
        # make sure the file was created
        self.assertTrue(os.path.isfile(FILENAME), "File %s should be already created" % FILENAME)
          
        # get file contents
        with open(FILENAME) as f:
            actual = f.read()
              
        # cleanup
        os.remove(FILENAME)
  
        # check the contents
        expected = '{"A": "Anna"}'
        self.assertEqual(expected, actual, 
                         'File created should contain %s, not %s' % (expected, actual))
              
          
    def test_update_exist(self):
        """ Test case 6. """
          
        WAIT_SECS = 0.1
          
        # update the file with new contents
        ExclusiveCacheFile.new_or_update(ExclusiveCacheFileTest.FILENAME, {"B" : "Barbara"}, WAIT_SECS)
          
        # get the updated contents
        with open(ExclusiveCacheFileTest.FILENAME) as f:
            actual = f.read()
              
        # check the contents
        expected = '{"A": "Anna", "B": "Barbara"}'
        self.assertEqual(expected, actual, 
                         'File should be updated to contain %s, not %s' % (expected, actual))
              
                  
    def test_update_sharelocked(self):
        """ Test case 7. """
          
        LOCK_CHECK_INTERVAL = 0.1 # this value since: Lock(check_interval=0.1) in ExclusiveCacheFile.new_or_update 
        LOCK_SECS = LOCK_CHECK_INTERVAL # lock for 1 interval
        WAIT_SECS = 2*LOCK_CHECK_INTERVAL # wait 2 intervals
              
        # shared lock the file
        ExclusiveCacheFileTest.lock_file_for_delay(ExclusiveCacheFileTest.FILENAME, LOCK_SECS, portalocker.LOCK_SH)
          
        # calc the waiting time before ExclusiveCacheFile updates the file
        start = time.time()
        ExclusiveCacheFile.new_or_update(ExclusiveCacheFileTest.FILENAME, {"B" : "Barbara"}, WAIT_SECS)
        stop = time.time()
        delay_secs = stop - start
  
        # sleep the lock time in case didnt wait and delay check should fail
        time.sleep(LOCK_SECS)            
        
        # get the contents
        with open(ExclusiveCacheFileTest.FILENAME) as f:
            actual = f.read()
                      
        # check there was a proper delay, 2.5* since can be 1 or 2 intervals + little overhead
        self.assertTrue(0.5*LOCK_SECS < delay_secs < 2.5*LOCK_SECS, 
                        "There should be ~%fsec waiting for updating shared locked file, but was %fsec" % 
                        (LOCK_SECS, delay_secs))
           
        # check the file contents was right
        expected = '{"A": "Anna", "B": "Barbara"}'
        self.assertEqual(expected, actual, 
                         'File should be updated to contain %s, not %s' % (expected, actual))
             
         
    def test_update_exclusivelylocked(self):
        """ Test case 8. """
          
        LOCK_CHECK_INTERVAL = 0.1 # this value since: Lock(check_interval=0.1) in ExclusiveCacheFile.new_or_update 
        LOCK_SECS = LOCK_CHECK_INTERVAL # lock for 1 interval
        WAIT_SECS = 2*LOCK_CHECK_INTERVAL # wait 2 intervals
          
        # exclusively lock the file
        ExclusiveCacheFileTest.lock_file_for_delay(ExclusiveCacheFileTest.FILENAME, LOCK_SECS, portalocker.LOCK_EX)
          
        # calc the waiting time before ExclusiveCacheFile updates the file
        start = time.time()
        ExclusiveCacheFile.new_or_update(ExclusiveCacheFileTest.FILENAME, {"B" : "Barbara"}, WAIT_SECS)
        stop = time.time()
        delay_secs = stop - start
  
              
        # sleep the lock time  
        time.sleep(LOCK_SECS)            
                      
        # check there was a proper delay, 2.5* since can be 1 or 2 intervals + little overhead
        self.assertTrue(0.5*LOCK_SECS < delay_secs < 2.5*LOCK_SECS, 
                        "There should be ~%fsec waiting for updating exclusively locked file, but was %fsec" % 
                        (LOCK_SECS, delay_secs))
           
        # get the file contents
        with open(ExclusiveCacheFileTest.FILENAME) as f:
            actual = f.read()

        # make sure the updated file contents is as expected
        expected = '{"A": "Anna", "B": "Barbara"}'
        self.assertEqual(expected, actual, 
                         'File should be updated to contain %s, not %s' % (expected, actual))
             
             
    def test_update_ex_locked_timeout(self):
        """ Test case 9. """
         
        LOCK_CHECK_INTERVAL = 0.1 # this value since: Lock(check_interval=0.1) in ExclusiveCacheFile.new_or_update 
        LOCK_SECS = 3*LOCK_CHECK_INTERVAL # lock for 3 intervals
        WAIT_SECS = LOCK_CHECK_INTERVAL # wait only 1 intervals to make ExclusiveCacheFile.new_or_update timeout
         
        # exclusively lock the file
        ExclusiveCacheFileTest.lock_file_for_delay(ExclusiveCacheFileTest.FILENAME, LOCK_SECS, portalocker.LOCK_EX)
         
        # check it timeouts
        try:
            ExclusiveCacheFile.new_or_update(ExclusiveCacheFileTest.FILENAME, {"B" : "Barbara"}, WAIT_SECS)
            time.sleep(LOCK_SECS) 
            self.fail("Should have timeout waiting for the locked file for this long time")
        except LockException:
            pass
 
        # sleep the lock time and delay
        time.sleep(LOCK_SECS)
 
        # get the not-updated file contents
        with open(ExclusiveCacheFileTest.FILENAME) as f:
            actual = f.read()
         
        # make sure the not-updated file contents is as expected
        expected = '{"A": "Anna"}'
        self.assertEqual(expected, actual, 
                         'After timeout the file should not be updated and still contain %s, not %s' % (expected, actual))
        
        
    @staticmethod
    def lock_file_for_delay(filename, seconds, locktype):
        " locktype <portalocker.LOCK_SH|portalocker.LOCK_EX>"
        
        def lock_file(seconds, file_locked_event):
            my_file = open(filename, "r")
            portalocker.lock(my_file, locktype)
            file_locked_event.set()
            time.sleep(seconds)
            my_file.close() # automatically unlock my_file
            
        file_locked = Event()    
        threading.Thread(target=lock_file, args=(seconds, file_locked)).start()
        
        # wait til the file is locked before returning control
        file_locked.wait()
        
                
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
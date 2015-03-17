'''
Created on 13-03-2015

@author: mateusz
'''
import unittest
from src.multitasking.teamwork import TeamWork
import threading
import time
from mock import Mock
from src.ioc.dependency_injector import DependencyInjector


class TestTeamWork(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestTeamWork, self).__init__(*args, **kwargs)
        
        # TeamWork is depending on injected "logger"
        logger_mock = Mock()
        DependencyInjector.manual_inject("logger", logger_mock, TeamWork) 
        
        
    def test_all_work_is_processed(self):
        """ Check all work is processed and returns expected results"""
        
        def calc_square(number):
            return number**2
        
        # start team work with 5 team members
        tw = TeamWork.start_work(calc_square, 5)
        
        # prepare work items and feed them to the team
        work_items = [1, 2, 3, 4, 5]
        map(tw.add_work, work_items)
        
        # prepare expected results
        expected_results = map(calc_square, work_items)
        
        # check we got only expected results
        for result in tw.end_work():
            self.assertTrue(result in expected_results, "%d is not in %s" % (result, str(expected_results)))
            expected_results.remove(result)
         
        # check all work has been processed
        self.assertEqual(len(expected_results), 0, "Not all expected results received: %s" % str(expected_results))   
        
    
    def test_handle_invalid_workitem(self):
        """ Check that invalid input data is properly handled and doesnt break the work """
         
        def calc_square(number):
            return number**2
         
        # start team work with 2 team members
        tw = TeamWork.start_work(calc_square, 2)
        
        # feed valid work to the team
        tw.add_work(12)
             
        # feed some invalid work that should cause exception 
        tw.add_work("some invalid data")
         
        # prepare expected results
        expected_results = [144]
         
        # check we got only expected results
        for result in tw.end_work():
            self.assertTrue(result in expected_results, "%d is not in %s" % (result, str(expected_results)))
            expected_results.remove(result)
          
        # check all work has been processed
        self.assertEqual(len(expected_results), 0, "Not all expected_results received: %s" % str(expected_results))   
         
         
    def test_seperate_threads_used(self):
        """ Check the work is actually processed using separate threads """
         
        NUM_SEPERTE_THREADS = 5
         
        def get_thread_id(_):
            # sleep the thread to let other threads pick the rest of work items
            time.sleep(0.01)
             
            # return the thread number
            return threading.current_thread()
         
        # start the team work
        tw = TeamWork.start_work(get_thread_id, NUM_SEPERTE_THREADS) 
         
        # feed some work to the team
        for i in xrange(NUM_SEPERTE_THREADS):  # @UnusedVariable
            tw.add_work(None)
            
        # finish the team work and collect unique results (thread id'thread_ids)
        thread_ids = set()
        map(thread_ids.add, tw.end_work())
             
        # ensure every work item was picked by separate thread
        # resulting in 5 different thread id'thread_ids in results
        actual_num_threads_used = len(thread_ids)
        self.assertEqual(actual_num_threads_used, NUM_SEPERTE_THREADS, 
                         "Should have used %d threads, not %d" % 
                         (NUM_SEPERTE_THREADS, actual_num_threads_used))
         
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
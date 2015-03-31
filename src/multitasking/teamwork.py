'''
Created on 13-03-2015

@author: mateusz
'''
from Queue import Queue
from threading import Thread
from src.ioc.dependency_injector import DependencyInjector, Inject

@DependencyInjector("logger")
class TeamWork(object):
    '''
    This class allows to process workload in parallel:
    1. tw = TeamWork.start_work(what_to_do, num_team_members)
    2. tw.ad_work(work_item) # many times
    3. results = tw.end_work()
    '''
         
    logger = Inject    
       
    # means that no more work will be supplied and worker threads should terminate
    FINISH_WORK = object()
    
    # means that processing of work item failed
    PROCESSING_FAILURE = object()

    
    @staticmethod 
    def start_work(work_to_do, num_team_members):
        return TeamWork(work_to_do, num_team_members)


    def __init__(self, work_to_do, num_workers):
        self.__in_queue = Queue()
        self.__out_queue = Queue() 
        self.__num_work_items = 0
        
        for i in xrange(num_workers):  # @UnusedVariable
            t = Thread(target=self.__worker_thread_func,
                       name="TeamWork worker thread",
                       args=(work_to_do, self.__in_queue, self.__out_queue))
            t.setDaemon(True)
            t.start()
        
        
    def __worker_thread_func(self, work_to_do, in_queue, out_queue):
        """ Worker thread target func """
        
        work_item = in_queue.get()
        
        # work until the finish_work is received
        while work_item != TeamWork.FINISH_WORK:
            try:
                result = work_to_do(work_item)
                out_queue.put(result)
            except Exception as e:
                try:
                    TeamWork.logger.exception(e)
                finally:
                    out_queue.put(TeamWork.PROCESSING_FAILURE)
            finally:
                in_queue.task_done()
                
            work_item = in_queue.get()
            
        # finish received - notify other threads to finish as well
        in_queue.put(TeamWork.FINISH_WORK)
    
    
    def add_work(self, work_item):
        self.__num_work_items += 1
        self.__in_queue.put(work_item)
        
        
    def end_work(self):
        # inform the threads to terminate
        self.__in_queue.put(TeamWork.FINISH_WORK)

        # yield all the valid results
        for i in xrange(self.__num_work_items):  # @UnusedVariable
            result = self.__out_queue.get()
            if result != TeamWork.PROCESSING_FAILURE:
                yield result
'''
Created on 18 mar 2015

@author: m.midor
'''
from functools import wraps
import time
from src.ioc.dependency_injector import Inject, DependencyInjector


@DependencyInjector("logger")
class LoggerAccess(object):
    logger = Inject
    
    
def MethodProfiler(target_method):
    """ 
    This decorator allows to easily measure any method execution time. Use:
    
    @MethodProfiler
    def connect_database(self): 
    """
    
    
    @wraps(target_method) 
    def time_it(*args, **kwargs):
        start = time.time()
        result = target_method(*args, **kwargs)
        end = time.time()
        delta =  end-start
        
        log_string = "%f[sec] consumed for %s called with args=%s and kwargs=%s"
        LoggerAccess.logger.debug(log_string % (delta, target_method.__name__, str(args), str(kwargs)))
        return result
    
    return time_it    

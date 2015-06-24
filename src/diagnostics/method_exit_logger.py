'''
Created on 24 jun 2015

@author: m.midor
'''
from functools import wraps
from src.ioc.dependency_injector import Inject, DependencyInjector


@DependencyInjector("logger")
class LoggerAccess(object):
    logger = Inject
    
    
def MethodExitLogger(log_string):
    """ 
    This decorator allows to easily log the method exit event. Use:
    
    @MethodExitLogger("EXIT connect_database")
    def connect_database(self): 
    """
    
    def method_wrapper(target_method):
        
        @wraps(target_method) 
        def args_wrapper(*args, **kwargs):
            result = target_method(*args, **kwargs)
            LoggerAccess.logger.info(log_string)
            return result
            
        return args_wrapper  
    return method_wrapper  

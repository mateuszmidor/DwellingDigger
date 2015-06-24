'''
Created on 24 jun 2015

@author: m.midor
'''
from functools import wraps
from src.ioc.dependency_injector import Inject, DependencyInjector


@DependencyInjector("logger")
class LoggerAccess(object):
    logger = Inject
    
    
def MethodEnterLogger(log_string):
    """ 
    This decorator allows to easily log the method entry event. Use:
    
    @MethodEnterLogger("ENTER connect_database")
    def connect_database(self): 
    """
    
    def method_wrapper(target_method):
        
        @wraps(target_method) 
        def args_wrapper(*args, **kwargs):
            LoggerAccess.logger.info(log_string)
            return target_method(*args, **kwargs)
            
        return args_wrapper  
    return method_wrapper  

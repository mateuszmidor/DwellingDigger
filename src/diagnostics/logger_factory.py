'''
Created on 24 mar 2015

@author: m.midor
'''
from src.diagnostics.logger import Logger
from src.ioc.dependency_injector import DependencyInjector, Inject

@DependencyInjector("config")
class LoggerFactory(object):
    config = Inject
    '''
    This class allows to create a Logger based on injected config.
    '''
    
    @staticmethod 
    def from_config():
        
        LEVEL_MAP = {'DEBUG'    : Logger.DEBUG,
                     'INFO'     : Logger.INFO,
                     'WARNING'  : Logger.WARN,
                     'ERROR'    : Logger.ERROR,
                     'FATAL'    : Logger.FATAL}
        
        
        config = LoggerFactory.config
        output = config.get("DIAGNOSTICS", "loggingOutput")
        level = config.get("DIAGNOSTICS", "loggingLevel")
        
        if output == 'NONE':
            return Logger.to_dev_null()
        elif output == 'TERMINAL':
            return Logger.to_terminal(LEVEL_MAP[level])
        elif output == 'FILE':
            filename = config.get("DIAGNOSTICS", "loggingOutputFile")
            return Logger.to_file(filename, LEVEL_MAP[level])
        else:
            return Logger.to_dev_null()
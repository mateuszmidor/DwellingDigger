'''
Created on 24 mar 2015

@author: m.midor
'''

# initialize_dependency_injection must be imported first in the main module to initialize all needed dependencies
import src.ioc.initialize_dependency_injection  # @UnusedImport
from src.mvc.controller import Controller

'''
DEMO RUN
'''
if __name__ == '__main__':
    Controller.demo_run()

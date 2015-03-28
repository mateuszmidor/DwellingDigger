'''
Created on 17 mar 2015

@author: m.midor
'''
from src.ioc.dependency_injector import DependencyInjector
from ConfigParser import ConfigParser
from src.diagnostics.logger_factory import LoggerFactory

"""
This module must be imported before all others;
it is responsible for configuring the dependency injection controller
so that all the classes using injected dependencies are setup correctly
before they are first time used.
The configuration can be later reimplemented using some sort of config file.
"""


# Set the config first so other modules can use it
config = ConfigParser()
config.read([r"config/config.ini"])
DependencyInjector.set_dependency("config", config)


# Set the logger
logger = LoggerFactory.from_config()
DependencyInjector.set_dependency("logger", logger)
'''
Created on 17 mar 2015

@author: m.midor
'''
from src.ioc.dependency_injector import DependencyInjector
from src.diagnostics.terminal_logger import TerminalLogger

"""
This module must be imported before all others;
it is responsible for configuring the dependency injection controller
so that all the classes using injected dependencies are setup correctly
before they are first time used.
The configuration can be later reimplemented using some sort of config file.
"""

# DependencyInjector.set_dependency("logger", FileLogger("DwellingDigger/diagnostics/logger.txt", FileLogger.WARN))
DependencyInjector.set_dependency("logger", TerminalLogger(TerminalLogger.WARN))
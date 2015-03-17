'''
Created on 17 mar 2015

@author: m.midor
'''
from src.ioc.dependency_proxy import DependencyProxy
from src.ioc.not_registered_dependency import NotRegisteredDependency
from src.ioc.dependency_injection_exception import DependencyInjectionException


class Inject():
    """
    Dependency Injection marker.
    Assign it to fields that are supposed to be subject of dependency injection, eg.
    
    @DependencyInjector('dependency') 
    class Example():
        dependency = Inject
    """
    def str(self):
        return "[This field should be substituted with actual value by @DependencyInjector decorator]"
    
        
        
class DependencyInjector():
    """"
    Dependency injection decorator for classes.
    There is only one DependencyInjector in system.
    """
    
    # dictionary with "dependency_name : value" pairs 
    dependencies = {}
    
    
    def __init__(self, *dependencies_to_inject):
        """takes list of dependencies names to be injected into the class"""
        self.dependencies_to_inject = dependencies_to_inject
    
    
    def __call__(self, target_object):
        """takes target class to inject dependencies into"""
        for name in self.dependencies_to_inject: 
            DependencyInjector.__throw_if_no_such_field(name, target_object)
            DependencyInjector.__throw_if_not_applicable(name, target_object)
            DependencyInjector.__register_if_not_registered(name)
            DependencyInjector.__inject(name, target_object)
            
        # return class with injected dependencies
        return target_object


    @staticmethod
    def __register_if_not_registered(name):
        if name not in DependencyInjector.dependencies:
            DependencyInjector.dependencies[name] = DependencyProxy(NotRegisteredDependency)      
          
             
    @staticmethod
    def __inject(dependency_name, target_object):
        setattr(target_object, dependency_name, DependencyInjector.dependencies[dependency_name])
          
          
    @staticmethod
    def manual_inject(field_name, value, target_object):
        """ this method is to avoid automatic DI machinery in tests; use it in tests"""
        DependencyInjector.__throw_if_no_such_field(field_name, target_object)
        setattr(target_object, field_name, value)
          
          
    @staticmethod
    def set_dependency(name, value):
        DependencyInjector.__register_if_not_registered(name)
        DependencyInjector.dependencies[name].set_proxy_target(value)
            
            
    @staticmethod
    def __throw_if_no_such_field(name, target_object):
        ERROR_STR = 'Cant inject dependency. No field "%s" in object of class "%s"'
        if name not in target_object.__dict__:
            raise DependencyInjectionException(ERROR_STR % (name, target_object.__name__))
        
        
    @staticmethod
    def __throw_if_not_applicable(name, target_object):
        ERROR_STR = 'Field "%s.%s" not designated for injection. Should be initially set to "Inject" instead of "%s"'
        if target_object.__dict__[name] != Inject: 
            raise DependencyInjectionException(ERROR_STR % (target_object.__name__, name, target_object.__dict__[name]))
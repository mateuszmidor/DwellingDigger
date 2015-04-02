'''
Created on 2 kwi 2015

@author: m.midor
'''
import unittest
from src.ioc.dependency_injector import DependencyInjector, Inject
from src.ioc.dependency_injection_exception import DependencyInjectionException



class TestDependencyInjector(unittest.TestCase):
    

    def test_first_setup_then_inject(self):
        """ Check if setup-dependency-then-inject-it order results in proper value injection into target class """ 
        
        ERROR_MSG = "The injected dependency should have value '%s', not '%s'"
        
        # set the dependency value first
        DependencyInjector.set_dependency("dependency", "dependency_value")
        
        # then inject the dependency
        @DependencyInjector('dependency')
        class Target:
            dependency = Inject
            
        # check the dependency actually got set
        self.assertEquals(Target.dependency, 
                          "dependency_value",
                          ERROR_MSG % ("dependency_value", str(Target.dependency)))
                          

    def test_first_inject_then_set(self):
        """ Check if inject-dependency-then-setup-it order results in proper value injection into target class """ 
        
        ERROR_MSG = "The injected dependency should have value '%s', not '%s'"
        
        # inject the dependency first
        @DependencyInjector('dependency')
        class Target:
            dependency = Inject
            
        # then set the value
        DependencyInjector.set_dependency("dependency", "dependency_value")
            
        # check the dependency actually got set
        self.assertEquals(Target.dependency, 
                          "dependency_value",
                          ERROR_MSG % ("dependency_value", str(Target.dependency)))
        
        
    def test_throws_on_no_such_field(self):
        """ Check if DependencyInjector throws proper exception when trying to inject dependency into field that doesnt exist in target class """
        try:
            @DependencyInjector('non_existing_field_to_inject_into')
            class Target:
                pass
            
            self.fail("DependencyInjector should have thrown DependencyInjectionException when given field not found in target class")
        except DependencyInjectionException:
            pass
       
       
    def test_throws_on_invalid_field(self):
        """ Check if DependencyInjector throws proper exception when trying to inject dependency into field that is not marked with Inject """
        try:
            @DependencyInjector('field_not_marked_for_injecting')
            class Target:
                field_not_marked_for_injecting = "Not for injecting!"
 
            self.fail("DependencyInjector should have thrown DependencyInjectionException when given field not marked for injection")
        except DependencyInjectionException:
            pass
                
                
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
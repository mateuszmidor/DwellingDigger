'''
Created on 17 mar 2015

@author: m.midor
'''

class Inject():
    """
    Dependency Injection marker.
    Assign it to fields that are supposed to be subject of dependency injection, eg.
    
    @InjectDependency('dependency') 
    class Example():
        dependency = Inject
    """
    def str(self):
        return "[This field should be substituted with actual value by @InjectDependency decorator]"
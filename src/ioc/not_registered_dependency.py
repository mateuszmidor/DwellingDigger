'''
Created on 17 mar 2015

@author: m.midor
'''

class NotRegisteredDependency():
    """
    Dependency Injection pending registration marker.
    If we need to inject dependency that has not been registered yet,
    we inject this class to mark that it needs registration prior to use
    """
    def str(self):
        return "[Dependency for this field should be registered by InjectDependency.registerDependency]"
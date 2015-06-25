'''
Created on 17 mar 2015

@author: m.midor
'''

class DependencyProxy():
    """
    We actually inject proxy to given object, not the object itself.
    This way we can easily exchange one dependency for another
    even after all dependencies have already been injected.
    This class is purposely left as an oldstyle (not inherited from object),
    as it is much simpler to implement required proxy functionality
    in oldstyle class.
    """
    
    # proxy _target
    _target = None
    
    
    def __init__(self, target):
        self.set_proxy_target(target)
        
        
    def __getattr__(self, name):
        return getattr(self._target, name)
        
    
    def set_proxy_target(self, target):
        self._target = target

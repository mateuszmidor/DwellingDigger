'''
Created on 03-02-2015

@author: mateusz
'''

class AddressCandidates(list):
    '''
    List of address candidates extrated from source string.
    '''
    last_processed = None
    
    def sort_by_correctness_precision(self):
        self.sort(lambda a, b: cmp(b.correctness_rank + b.precision_rank, a.correctness_rank + a.precision_rank))
        AddressCandidates.last_processed = self
        
    def __unicode__(self):
        r = u""
        for candidate in self:
            r += u"{0}[c:{1},p:{2}] ".format(candidate.address, candidate.correctness_rank, candidate.precision_rank)
        
        return r
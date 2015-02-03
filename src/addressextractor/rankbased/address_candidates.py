'''
Created on 03-02-2015

@author: mateusz
'''

class AddressCandidates(list):
    '''
    List of address candidates extrated from source string.
    '''

    def sort_by_correctness_precision(self):
        self.sort(lambda a, b: cmp(b.correctness_rank + b.precision_rank, a.correctness_rank + a.precision_rank))
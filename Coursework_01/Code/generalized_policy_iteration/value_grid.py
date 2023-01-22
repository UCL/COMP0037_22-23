'''
Created on 29 Jan 2022

@author: ucacsjj
'''

# This grid stores the value function for each state. It's defined to be a 
# real number in all cases, so we specialise it here.

import numpy as np

from grid_search.grid import Grid

# TODO: USE NUMPY INSTEAD?

class ValueGrid(Grid):

    def __init__(self, name, environment_map, set_random = False):
        Grid.__init__(self, name, \
                      environment_map.width(), environment_map.height())
        
        self._values = np.zeros((self._width, self._height))
    
    def set_value(self, x, y, V):
        self._values[x, y] = V
        
    def value(self, x, y):
        return self._values[x, y]
       
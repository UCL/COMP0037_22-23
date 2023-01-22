'''
Created on 29 Jan 2022

@author: ucacsjj
'''

# This grid should be used to store the policy at each cell.
# The action is very system dependent, and so we can't provide
# any more details at this level in the class

from grid_search.grid import Grid

class PolicyGrid(Grid):

    def __init__(self, name, environment_map, set_random = False):
        Grid.__init__(self, name, \
                      environment_map.width(), environment_map.height())
    
    def set_action(self, x, y, action):
        raise NotImplementedError()
        
    def action(self, x, y):
        raise NotImplementedError()
       
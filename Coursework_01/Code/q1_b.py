#!/usr/bin/env python3

'''
Created on 27 Jan 2022

@author: ucacsjj
'''

from common.airport_map_drawer import AirportMapDrawer
from common.scenarios import full_scenario

from p1.high_level_environment import PlannerType
from p1.high_level_environment import HighLevelEnvironment
from p1.high_level_actions import HighLevelActionType

if __name__ == '__main__':
    
    # Create the scenario
    airport_map, drawer_height = full_scenario()

    print(airport_map)
    
    # Draw what the map looks like. This is optional and you
    # can comment it out
    airport_map_drawer = AirportMapDrawer(airport_map, drawer_height)
    airport_map_drawer.update()    
    airport_map_drawer.wait_for_key_press()
        
    # Create the gym environment
    # Q1b:
    # Evaluate breadth and depth first algorithms.
    # Check the implementation of the environment
    # to see how the planner type is used.
    airport_environment = HighLevelEnvironment(airport_map, PlannerType.BREADTH_FIRST)
    
    # Set to False to just show the final state of the
    # planner at the end of each planning operation
    airport_environment.enable_verbose_graphics(True)
    
    # First specify the start location of the robot
    action = (HighLevelActionType.TELEPORT_ROBOT_TO_NEW_POSITION, (0, 0))
    observation, reward, done, info = airport_environment.step(action)
    
    if reward is -float('inf'):
        print('Unable to teleport to (1, 1)')
        
    # Get all the rubbish bins and toilets; these are places which need cleaning
    all_rubbish_bins = airport_map.all_rubbish_bins()
        
    # Q1b:
    # Modify this code to collect the data needed to assess the different algorithms
    
    # Now go through them and plan a path sequentially
    for rubbish_bin in all_rubbish_bins:
            action = (HighLevelActionType.DRIVE_ROBOT_TO_NEW_POSITION, rubbish_bin.coords())
            observation, reward, done, info = airport_environment.step(action)
    
            try:
                input("Press enter in the command window to continue.....")
            except SyntaxError:
                pass  
    

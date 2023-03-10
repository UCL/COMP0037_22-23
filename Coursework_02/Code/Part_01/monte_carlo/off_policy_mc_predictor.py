'''
Created on 23 Feb 2023

@author: steam
'''

import numpy as np

from .monte_carlo_policy_predictor import MonteCarloPolicyPredictor

class OffPolicyMCPredictor(MonteCarloPolicyPredictor):

    def __init__(self, environment):
        
        MonteCarloPolicyPredictor.__init__(self, environment)
        self._Q = None
        self._b = None

    def set_behaviour_policy(self, b):
        self._b = b
        
        self.initialize()

    def initialize(self):
        
        MonteCarloPolicyPredictor.initialize(self)
        
        environment = self._environment
        environment_map = environment.environment_map()
        w = environment_map.width()
        h = environment_map.height()
        
        action_space = environment.action_space
        
        # Allocate Q and A
        self._Q = np.zeros((w, h, action_space.n))
        self._C = np.zeros((w, h, action_space.n))
        
        self._v.set_name("OffPolicyMCPredictor")

    def _select_episode_start(self):
        
        if self._use_exploring_starts is True:
            start_x = self._environment.random_initial_state()
            start_a = self._environment.random_initial_action(start_x)
        else:
            start_x = self._environment.get_state(0, 0)
            start_a = 0
        
        return start_x, start_a

    def _update_value_function_from_episode(self, episode):

        G = 0
        W = 1
        
        # Very simple way to implement first visit
        environment_map = self._environment.environment_map()
        w = environment_map.width()
        h = environment_map.height()
        visited_grid = np.zeros((w, h, self._environment.action_space.n))

        for s in range(episode.number_of_steps() - 1, -1, -1):
            
            # Work out the return              
            G = self._gamma * G + episode.reward(s)
            
            a = episode.action(s)
            coords = episode.state(s).coords()
            
            if (self._use_first_visit is False) or (visited_grid[coords[0], coords[1], a] == 0):
                visited_grid[coords[0], coords[1], a] = visited_grid[coords[0], coords[1], a] + 1
                self._C[coords[0], coords[1], a] = self._C[coords[0], coords[1], a] + W
                c = W / self._C[coords[0], coords[1], a]
                self._Q[coords[0], coords[1], a] = (1 - c) * self._Q[coords[0], coords[1], a] + c * G
        
            target_policy_action_probability = self._pi.action_probability(coords[0], coords [1], a)
            
            behaviour_policy_action_probability = self._b.action_probability(coords[0], coords [1], a)
            
            #print(f"target_policy_action_probability={target_policy_action_probability};behaviour_policy_action_probability={behaviour_policy_action_probability}")
            W = W * target_policy_action_probability / behaviour_policy_action_probability

            # If W is too small, assume we can terminate the episode
            if W < 1e-15:
                break

        # Now update V by going through and storing the Q value according to the action
        environment = self._environment
        environment_map = environment.environment_map()
        w = environment_map.width()
        h = environment_map.height()
        
        for x in range(w):
            for y in range(h):
                a = self._pi.action(x, y)
                self._v.set_value(x, y, self._Q[x, y, a])
                
        
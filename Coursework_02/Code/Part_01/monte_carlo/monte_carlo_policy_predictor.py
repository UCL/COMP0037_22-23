'''
Created on 20 Feb 2023

@author: ucacsjj
'''

from .mc_algorithm_base import MCAlgorithmBase

# Monte Carlo techniques
from .episode_sampler import EpisodeSampler

class MonteCarloPolicyPredictor(MCAlgorithmBase):
    '''
    classdocs
    '''

    def __init__(self, environment):
        
        MCAlgorithmBase.__init__(self, environment)

    def set_target_policy(self, policy):        
        self._pi = policy        
        self.initialize()

    def evaluate(self):
        
        episode_sampler = EpisodeSampler(self._environment)
        
        for episode in range(self._number_of_episodes):

            # Choose the start for the episode            
            start_x, start_a = self._select_episode_start()
            
            # Now sample it
            new_episode = episode_sampler.sample_episode(self._pi, start_x, start_a)

            # If we didn't terminate, skip this episode
            if new_episode.terminated_successfully() is False:
                continue
            
            # Update with the current episode
            self._update_value_function_from_episode(new_episode)
            
            # Pick several randomly from the experience replay buffer and update with those as well
            for _ in range(5):
                episode = self._draw_random_episode_from_experience_replay_buffer()
                if episode is not None:
                    self._update_value_function_from_episode(episode)
                
            self._add_episode_to_experience_replay_buffer(new_episode)
            
    def _select_episode_start(self):
        raise NotImplementedError
            
    def _update_value_function_from_episode(self, episode):
        raise NotImplementedError 
            
            
            
        
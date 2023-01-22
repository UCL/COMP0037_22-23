from math import sqrt
from queue import PriorityQueue

from .planner_base import PlannerBase

class GreedyShortestDistancePlanner(PlannerBase):

    # This order the cells on a priority queue, sorted in terms of distance to target: shorter is better
    
    def __init__(self, occupancy_grid):
        PlannerBase.__init__(self, occupancy_grid)
        self._priority_queue = PriorityQueue()

    # Sort in order of distance from the target and use that
    def push_cell_onto_queue(self, cell):

    #Q4a:

        # Distance to the goal
        cell_coords = cell.coords()
        goal_coords = self.goal.coords()

        dX = cell_coords[0] - goal_coords[0]
        dY = cell_coords[1] - goal_coords[1]
        d = sqrt(dX * dX + dY * dY)
        self._priority_queue.put((d, cell))

    # Check the queue size is zero
    def is_queue_empty(self):
        return self._priority_queue.empty()

    # Simply pull from the front of the list
    def pop_cell_from_queue(self):
        t = self._priority_queue.get()
        return t[1]

    def resolve_duplicate(self, cell, parent_cell):
        # Nothing to do in this case
        pass

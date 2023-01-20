from .planner_base import PlannerBase

class DepthFirstPlanner(PlannerBase):

    # This implements a simple LIFO search algorithm
    
    #
    
    def __init__(self, occupancyGrid):
        PlannerBase.__init__(self, occupancyGrid)
        self.lifoQueue = list()

    # Simply put on the end of the queue
    def push_cell_onto_queue(self, cell):
        self.lifoQueue.append(cell)

    # Check the queue size is zero
    def is_queue_empty(self):
        return not self.lifoQueue

    # Simply pull from the front of the list
    def pop_cell_from_queue(self):
        cell = self.lifoQueue.pop()
        return cell

    def resolve_duplicate(self, cell, parent_cell):
        # Nothing to do in this case
        pass

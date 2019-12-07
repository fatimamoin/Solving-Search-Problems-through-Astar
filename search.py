# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
       
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """

        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """

        util.raiseNotDefined()
        
    def getHeuristic(self,state):
        """
         state: the current state of agent

         THis function returns the heuristic of current state of the agent which will be the 
         estimated distance from goal.
        """
        util.raiseNotDefined()


def aStarSearch(problem):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    initial = problem.getStartState()
    frontier = util.PriorityQueue()
    heurestic = problem.getHeuristic(initial)
    frontier.push(initial, heurestic)
    path = []
    f_cost={} 
    visited =[] 
    nodes ={}
    nodes[initial] = None
    f_cost[initial] = 0

    while frontier:
        curr = frontier.pop()
        if curr not in visited:
            visited.append(curr)
            if problem.isGoalState(curr):
                while curr:
                    path.append(curr)
                    curr=nodes[curr]
                return path[::-1]
                
            neighbors = problem.getSuccessors(curr)
            for neighbor in neighbors:
                total = neighbor[3] + f_cost[curr]
                if neighbor[0] not in f_cost or total < f_cost[neighbor[0]]:
                    f_cost[neighbor[0]] = total
                    priority= total + problem.getHeuristic(neighbor[0])
                    frontier.push(neighbor[0],priority)
                    nodes[neighbor[0]] = curr
          
        
#inspiration taken from http://mat.uab.cat/~alseda/MasterOpt/AStar-Algorithm.pdf
#                    and http://coecsl.ece.illinois.edu/ge423/lecturenotes/AstarHandOut.pdf






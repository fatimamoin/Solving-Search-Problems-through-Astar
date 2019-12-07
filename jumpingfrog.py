# eightpuzzle.py
# --------------
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


import search
import random
import util

# Module Classes

class JumpingFrogState:

    def __init__( self, numbers ):
        """
          The arrangement of the frogs as given in the question is
          [green, green, green, space, red, red, red]
          We use 1 to represent green and -1 to represent red
        """
        self.cells = []
        numbers = numbers[:] # Make a copy so as not to cause side-effects.
        numbers.reverse()
        for row in range( 7 ):
            self.cells.append( numbers.pop() )
            if self.cells[row] == 0:
                self.blankLocation = row
                
    def isGoal( self ):
        """    
        >>> JumpingFrogState([-1, -1, -1, 0, 1, 1, 1]).isGoal()
        True
        """
        goal = [-1,-1,-1,0,1,1,1]
        for current in range(7):
            if goal[current] != self.cells[current]:
                return False
        return True

    def legalMoves( self ):
        """
          Returns a list of legal moves from the current state.

        Moves consist of moving the empty stone left, right,
        double right( jump right twice), and  double left.

        >>> JumpingFrogState([1,0,-1,1,1,-1,-1]).legalMoves()
        ['down', 'right']
        """
        moves = []
        row = self.blankLocation
        if(row != 0):
            moves.append('left')
        if(row != 6):
            moves.append('right')
        if (row > 1):
            moves.append('double left')
        if (row < 5):
            moves.append('double right')
        return moves

    def result(self, move):
        row = self.blankLocation
        if(move == 'left'):
            newrow = row - 1
        elif(move == 'right'):
            newrow = row + 1
        elif (move == 'double left'):
            newrow = row - 2
        elif(move == 'double right'):
            newrow = row + 2
        else:
            raise "Illegal Move"

        newPuzzle = JumpingFrogState([0, 0, 0, 0, 0, 0, 0])
        newPuzzle.cells = [values for values in self.cells]
        newPuzzle.cells[row] = self.cells[newrow]
        newPuzzle.cells[newrow] = self.cells[row]
        newPuzzle.blankLocation = newrow

        return newPuzzle

    # Utilities for comparison and display
    def __eq__(self, other):
        """
            Overloads '==' such that two eightPuzzles with the same configuration
          are equal.

          >>> JumpingFrogState([0, 1, 1,1,-1,-1,-1]) == 
              JumpingFrogState([1, 0, 1, 1, -1, -1, -1).result('left')
          True
        """
        for row in range( 7 ):
            if self.cells[row] != other.cells[row]:
                return False
        return True

    def __hash__(self):
        return hash(str(self.cells))

    def __getAsciiString(self):
        """
          Returns a display string for the frogs
        """
        representation=''
        for row in self.cells:
            if row == -1:
                representation= representation + ' red '
            elif row == 1:
                representation = representation +' green '
            elif row == 0:
                representation= representation +' blank '
        return representation

    def __str__(self):
        return self.__getAsciiString()

# TODO: Implement The methods in this class

class JumpingFrogProblem(search.SearchProblem):

    def __init__(self,puzzle):
        "Creates a new JumpingFrogProblem which stores search information."
        self.puzzle = puzzle

    def getStartState(self):
        return puzzle

    def isGoalState(self,state):
        return state.isGoal()

    def getSuccessors(self,state):
        """
          Returns list of (successor, action, stepCost) pairs where
          each succesor is either left, right, up, or down
          from the original state and the cost is 1.0 for each
        """
        succ = []
        for a in state.legalMoves():
            if a== 'double left' or a== 'double right':
                succ.append((state.result(a), a,state, 2))
            else:
                succ.append((state.result(a), a,state, 1))
            #succ.append(state.result(a))
        return succ

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        cost = 0 
        for i in actions:
            if a== 'double left' or a== 'double right':
                cost+=2
            else:
                cost+=1
        return cost

    
    def getHeuristic(self,state):
        #defining heurestic as no. of misplaced frogs
        h=0
        current= state.cells
        goal=[-1,-1,-1,0,1,1,1]
        for i in range(0, len(goal)):
            if current[i] != goal[i]:
                 h+=1
        return h
    
JUMPING_FROG_DATA = [1, 1,1, 0, -1, -1, -1]


def loadJumpingFrogs(puzzleNumber):
    """
      puzzleNumber: The number of the eight puzzle to load.

      Returns a jumping frog puzzleobject generated from one of the
      provided puzzles in JUMPING_FROG_DATA.

      puzzleNumber can range from 0 to 
    """
    return JumpingFrogState(JUMPING_FROG_DATA)

def createJumpingFrog(moves=100):
   """ If you want to create a random starting
    state of the frogs, uncomment the following code """
   puzzle = JumpingFrogState([1, 1,1, 0, -1, -1, -1])
  # for i in range(moves):
   #    puzzle = puzzle.result(random.sample(puzzle.legalMoves(), 1)[0])
   return puzzle



#Main program
puzzle = createJumpingFrog(30)
problem = JumpingFrogProblem(puzzle)
path = search.aStarSearch(problem)

print('Search found a path of %d moves. ' %(len(path)))
for i in path:
    print(i)

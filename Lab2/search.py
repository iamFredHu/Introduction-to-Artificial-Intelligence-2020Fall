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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    actions = []
    record = []
    closedList = util.Stack()
    openList = util.Stack()
    openList.push(problem.getStartState())
    while True:
        if openList.isEmpty():
            print("Can't solve!")
            return util.raiseNotDefined()
            # to do

        node = openList.pop()
        if problem.isGoalState(node):
            break

        if node not in closedList.list:
            closedList.push(node)
            for child in problem.getSuccessors(node):
                # e.g. child = ((5, 4), 'South', 1)
                if child[0] not in closedList.list:
                    openList.push(child[0])
                    record.append(child)

    a = list(node)
    while a != list(problem.getStartState()):
        for child in record:
            if list(child[0]) == a:
                actions.append(child[1])
                if child[1] == 'South':
                    a[1] += 1
                if child[1] == 'North':
                    a[1] -= 1
                if child[1] == 'East':
                    a[0] -= 1
                if child[1] == 'West':
                    a[0] += 1
    print(actions[::-1])
    return actions[::-1]


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    actions = []
    record = []
    closedList = util.Queue()
    openList = util.Queue()
    openList.push(problem.getStartState())
    while True:
        if openList.isEmpty():
            print("Can't solve!")
            return util.raiseNotDefined()
            # to do

        node = openList.pop()
        if problem.isGoalState(node):
            break

        if node not in closedList.list:
            closedList.push(node)
            for child in problem.getSuccessors(node):
                # e.g. child = ((5, 4), 'South', 1)
                if child[0] not in closedList.list:
                    openList.push(child[0])
                    record.append(child)

    a = list(node)
    while a != list(problem.getStartState()):
        for child in record:
            if list(child[0]) == a:
                actions.append(child[1])
                if child[1] == 'South':
                    a[1] += 1
                if child[1] == 'North':
                    a[1] -= 1
                if child[1] == 'East':
                    a[0] -= 1
                if child[1] == 'West':
                    a[0] += 1
    print(actions[::-1])
    return actions[::-1]


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    temp = problem.getStartState()
    closedList = []
    openList = util.PriorityQueue()
    openList.push((temp, []), 0)
    while not openList.isEmpty():
        temp, actions = openList.pop()
        if problem.isGoalState(temp):
            return actions
        if not temp in closedList:
            closedList.append(temp)
            for child in problem.getSuccessors(temp):
                if child[0] not in closedList or problem.isGoalState(child[0]):
                    openList.update((child[0], actions + [child[1]]), problem.getCostOfActions(actions + [child[1]]))


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    pqueue = util.PriorityQueue()
    actions = []
    visited = []
    pqueue.push((problem.getStartState(), actions), 0)
    while pqueue:
        node, actions = pqueue.pop()
        if problem.isGoalState(node):
            break
        if node not in visited:
            visited.append(node)
            for child in problem.getSuccessors(node):
                # tempActions = actions + [child[1]]
                # nextCost = problem.getCostOfActions(actions + [child[1]]) + heuristic(child[0], problem)
                if child[0] not in visited:
                    pqueue.push((child[0], actions + [child[1]]),
                                problem.getCostOfActions(actions + [child[1]]) + heuristic(child[0], problem))
    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
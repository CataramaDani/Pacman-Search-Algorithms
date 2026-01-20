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
from util import Stack, Queue, PriorityQueue


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


def depthFirstSearch(problem: SearchProblem):
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
    # @author: Alexandra Nanu
    '''Definesc variabilele: 
    - noduri: stiva care contine nodurile prin care trebuie sa traversam pornind de la starea initiala
    - noduri_v: set cu nodurile viziztate, nodurile sunt unice 
    - drumuri: contine caile pana la noduri
    '''
    noduri_v = set()
    noduri = Stack()
    cai = Stack()
    noduri.push(problem.getStartState())
    cai.push([])

    '''Parcurg nodurile din graf pana la nodul Goal:
    - extragem nodurile din graf si stocam nodul si drumul pana la nod
    - daca nodul la care suntem nu a fost vizitat, il adaug in set, iar apoi il parcurgem, astfel ca:
        *prin functia getSuccesors sew va returna urmatorul nod, actiunea pe care trebuie sa o facem pentru a ajunge la nod si costul actiunii
    - daca ajungem la nodul Goal returnam drumul pana la nod
    '''
    while not noduri.isEmpty():
        nod_curent = noduri.pop()
        cale = cai.pop()

        if problem.isGoalState(nod_curent):
            return cale

        if nod_curent not in noduri_v:
            noduri_v.add(nod_curent)
            for succesor, actiune, cost_actiune in problem.getSuccessors(nod_curent):
                if succesor not in noduri_v:
                    noduri.push(succesor)
                    cai.push(cale + [actiune])
    return []


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    """Paula Moldovan"""

    coada = Queue()
    coada.push((problem.getStartState(), []))  # adaug in coada starea de pornire si o lista goala de actiuni
    vizitat = set()  # starile deja vizitate, pt a evita blucle infinite

    while not coada.isEmpty():
        state, path = coada.pop()  # cat timp mai exista elem in coada, alg extrage si elimina prima stare dim coada si drumul pana acolo

        if problem.isGoalState(state):  # daca starea extrasa e starea finala atunci
            return path  # se returneaza drumul parcurs pana la aceasta

        if state not in vizitat:  # daca starea curenta nu a fost vizitata, se adauga in vizitat
            vizitat.add(state)
            for succesor, action, cost in problem.getSuccessors(
                    state):  # succesorii starii curente care poate fi o stare sau o actiune prin care se ajunge acolo
                if succesor not in vizitat:  # pt fiecare succesor nevizitat se adauga in coada  o pereche formata din
                    coada.push((succesor, path + [
                        action]))  # succesor care e noua stare si drumul pana acolo adica drumul actual si actiunea necesara pt a ajunge la succ

    return []  # daca coada e goala si nu am gasit nici o sol, fct returneaza o lista goala, adica nu exista nici un drum pana la starea finala

    util.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    """Paula Moldovan"""

    coada_pr = PriorityQueue()  # permite extragerea elem cu cel mai mic cost
    coada_pr.push((problem.getStartState(), []),
                  0)  # adaug starea initiala si o lista goala de actiuni, si costul 0 pt a junge in acea stare (in care sunt)
    vizitat = {}  # dictionar care stocheaza costul min cunoscut la fiecare stare vizitata

    while not coada_pr.isEmpty():
        state, path = coada_pr.pop()  # se extrage si elimina elem cu cost min, adica o stare si drumul pana acolo

        if problem.isGoalState(state):  # daca starea extrasa e starea finala
            return path  # returnez drumul parcurs pana la acea stare
        if state not in vizitat or vizitat[state] > problem.getCostOfActions(
                path):  # daca starea curenta nu a fost vizitata sau daca costul cunoscut pt a ajunge la ea e > decat costul actual
            vizitat[state] = problem.getCostOfActions(path)  # actualiz dictionarul cu costul curent pt acesta stare

            for succesor, action, cost in problem.getSuccessors(state):  # pt fiecare succesor al starii curente
                path_nou = path + [action]  # creez un nou drum care e actiunea pt a ajunge la acel succesor
                coada_pr.push((succesor, path_nou), problem.getCostOfActions(
                    path_nou))  # ad succesorul si drumul asociat in coada de prioritate, fol costul total pt a ajunge acolo

    return []  # daca coada de prioritate e goala si nu avem solutie, se returneaza o lista goala

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # @author: Alexandra Nanu
    '''Definesc variabilele: 
    - noduri: stiva care contine nodurile prin care trebuie sa traversam pornind de la starea initiala
    - noduri_v: set cu nodurile viziztate, nodurile sunt unice 
    - drumuri: contine caile pana la noduri
    '''
    noduri_v = []
    noduri = PriorityQueue()
    cai = PriorityQueue()
    noduri.push(problem.getStartState(), 0)
    cai.push([], 0)
    '''Parcurg nodurile din graf pana la nodul Goal:
    - extragem nodurile din graf si stocam nodul si drumul pana la nod
    - daca nodul la care suntem nu a fost vizitat, il adaug in set, iar apoi il parcurgem, astfel ca:
        *prin functia getSuccesors sew va returna urmatorul nod, actiunea pe care trebuie sa o facem pentru a ajunge la nod si costul actiunii
        *pentru fiecare succesor care nu a fost vizitat: calculam costul pentru drumul pana la nod si adaugam si euristica utilizata
              -mentionez si elementul in functie de care ordonez coada pentru ca folosesc Priority Queue
    - daca ajungem la nodul Goal returnam drumul pana la nod
    '''
    while not noduri.isEmpty():
        nod_curent = noduri.pop()
        cale = cai.pop()

        if problem.isGoalState(nod_curent):
            return cale

        if nod_curent not in noduri_v:
            noduri_v.append(nod_curent)
            for succesor, actiune, cost_actiune in problem.getSuccessors(nod_curent):
                if succesor not in noduri_v:
                    cale_new = cale + [actiune]
                    cost_total = problem.getCostOfActions(cale_new) + heuristic(succesor, problem)
                    noduri.push(succesor, cost_total)
                    cai.push(cale_new, cost_total)
    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

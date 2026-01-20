Pacman Search Algorithms
This project implements classic search algorithms to help Pacman navigate mazes efficiently, find food, and reach target locations optimally.

License
This project is for educational purposes and follows the Berkeley AI Pacman Project framework.
Please note that the project has been solved in teams of 2:

Overview
The goal of this project is to apply fundamental AI search algorithms in a grid-based environment. Pacman must navigate through mazes using different strategies, each with its strengths and limitations.

Implemented Algorithms
Depth-First Search (DFS): Explores as deep as possible before backtracking.
Breadth-First Search (BFS): Expands nodes level by level for shortest-path guarantees.
Uniform Cost Search (UCS): Uses a priority queue to find the least-cost path.
A* Search (A*): Enhances UCS with heuristics for faster, optimal solutions.
How to Run the Search Agents
Test different search strategies by running:

DFS: python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
BFS: python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z 0.5
UCS: python pacman.py -l mediumDottedMaze -p SearchAgent -a fn=ucs
A*: python pacman.py -l bigMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
Use -h  for a list of available options: python pacman.py -h
Run the autograder to test the given implementation: python autograder.py
File Structure
search.py– Implements the search algorithms
searchAgent.py – Defines search-based agents using implemented algorithms
pacman.py – Main game engine
util.py – Helper functions for data structures

# Pacman Search Algorithms

This project implements classic AI search algorithms to help Pacman navigate mazes efficiently, locate food, and reach target locations optimally. It is based on the **UC Berkeley AI Pacman Project** framework and is intended for educational use.

> **Note:** This project was completed collaboratively by a team of **two students**.

---

## 📌 Overview

The objective of this project is to apply fundamental **search algorithms** in a grid-based environment. Pacman must navigate through mazes using different strategies, each demonstrating unique strengths and trade-offs in terms of optimality, completeness, and efficiency.

Through this project, we explore how classical AI techniques can be used to solve pathfinding and planning problems.

---

## 🧠 Implemented Search Algorithms

- **Depth-First Search (DFS)**  
  Explores as deep as possible along a path before backtracking. Fast but does not guarantee the shortest path.

- **Breadth-First Search (BFS)**  
  Expands nodes level by level and guarantees the shortest path in unweighted graphs.

- **Uniform Cost Search (UCS)**  
  Uses a priority queue to always expand the least-cost node, ensuring optimal solutions when costs vary.

- **A\* Search**  
  An informed search algorithm that combines path cost and heuristics to find optimal solutions more efficiently than UCS.

---

## ▶️ How to Run the Search Agents

You can test different search strategies using the following commands:

- **Depth-First Search (DFS)**
  ```bash
  python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
  ```

- **Breadth-First Search (BFS)**
  ```bash
  python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z 0.5
  ```

- **Uniform Cost Search (UCS)**
  ```bash
  python pacman.py -l mediumDottedMaze -p SearchAgent -a fn=ucs
  ```

- **A\* Search (Manhattan Heuristic)**
  ```bash
  python pacman.py -l bigMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
  ```

To see all available command-line options:
```bash
python pacman.py -h
```

---

## ✅ Autograder

To evaluate the correctness of the implementation, run the provided autograder:

```bash
python autograder.py
```

---

## 📂 File Structure

- **search.py** – Implements the core search algorithms (DFS, BFS, UCS, A*)
- **searchAgents.py** – Defines search-based Pacman agents
- **pacman.py** – Main game engine and entry point
- **util.py** – Utility classes and data structures (stacks, queues, priority queues)

---

## 📜 License

This project is for **educational purposes only** and follows the guidelines and structure of the **UC Berkeley AI Pacman Project**. It is not intended for commercial use.

---

## 🚀 Learning Outcomes

- Understand uninformed vs. informed search
- Apply heuristics effectively in A\* search
- Analyze trade-offs between completeness, optimality, and performance
- Gain hands-on experience with AI problem-solving in grid environments

---

Happy pathfinding! 👻🍒


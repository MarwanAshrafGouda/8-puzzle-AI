# **8-puzzle AI Solver**

## **An AI program that solves the 8-puzzle problem using various search algorithms.**

___

### **How is the 8-puzzle problem a search problem?**

If we consider the initial board configuration to be the root of a tree, then all the configurations resulting from
performing legal moves on the initial configuration can be considered the children of that configuration. Continuing by
that logic, the problem could be reduced to a tree search problem in which the goal is a configuration in which all tiles are
in the right place.

### **How do you solve a search problem?**

A search problem is solved using search algorithms. The goal of this project is to compare search algorithms based on
runtime, the number of configurations the algorithm needs to consider until it reaches the goal, and overall efficiency.
The algorithms used in this project are:
* Depth-first Search
* Breadth-first Search
* A* search using two different heuristics:
    * Euclidean Distance  
      The sum of the lengths of the shortest straight line between each tile and its correct position
    * Manhattan Distance  
      The sum of the number of horizontal and vertical tiles between each tile and its correct position

### Depth-first Search

### Breadth-first Search

### A* Search using Euclidean Distance

### A* Search using Manhattan Distance


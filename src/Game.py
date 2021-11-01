# the main file in which the game is played
# should be the interface to the program, display GUI, keep track of time,
# shuffle initial state or allow user to enter it ...etc
import timeit

from GameState import GameState
from Heuristics import ManhattanHeuristic, EuclideanHeuristic
from SearchAlgorithms import BFS, DFS, AStar


def visualize_board(string: str):
    for i in range(0, 3):
        print(string[i * 3: i * 3 + 3])
    print('')


initial_state = GameState("125340678")
algorithm = AStar(ManhattanHeuristic())
# algorithm = AStar(EuclideanHeuristic())
# algorithm = BFS()
# algorithm = DFS()
start = timeit.default_timer()
goal, expanded = algorithm.search(initial_state)
stop = timeit.default_timer()
print(str((stop - start) * 1000) + " ms")
print(len(expanded))
print(str(goal.movement_cost) + '\n')
sequence = []
while goal:
    sequence.append(goal.configuration)
    goal = goal.parent
for config in reversed(sequence):
    visualize_board(config)

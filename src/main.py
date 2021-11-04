"""
import random
import timeit

from Heuristics import *
from SearchAlgorithms import *


def visualize_board(string: str):
    for i in range(0, 3):
        print(string[i * 3: i * 3 + 3])
    print('')

initial_state = GameState(shuffled_board)

algorithm = AStar(ManhattanHeuristic())
# algorithm = AStar(EuclideanHeuristic())
# algorithm = BFS()
# algorithm = DFS()

start = timeit.default_timer()
goal, expanded, max_depth = algorithm.search(initial_state)
stop = timeit.default_timer()

print("Runtime: " + str((stop - start) * 1000) + " ms")
print("Number of expanded nodes: " + str(len(expanded)))
print("Search depth: " + str(max_depth))
if goal:
    print("Cost: " + str(goal.movement_cost))
else:
    print("Is this board configuration hontou ni invincible?")

sequence = []
while goal:
    sequence.append(goal.configuration)
    goal = goal.parent
for config in reversed(sequence):
    visualize_board(config)
"""

import sys
import gui as game
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
gui = QtWidgets.QMainWindow()
ui = game.UiGame()
ui.setup_ui(gui)
gui.show()
sys.exit(app.exec_())

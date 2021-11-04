"""
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

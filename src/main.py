"""
if goal:
    print("Cost: " + str(goal.movement_cost))
else:
    print("Is this board configuration hontou ni invincible?")
"""

import sys
import gui as game
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
gui = QtWidgets.QMainWindow()
ui = game.UiGame()
ui.setup_ui(gui, max_time_delay=0.2)
gui.show()
sys.exit(app.exec_())

import sys
import gui as game
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
gui = QtWidgets.QMainWindow()
ui = game.UiGame()
ui.setup_ui(gui, play_speed=0.25, print_configs=True)
gui.show()
sys.exit(app.exec_())

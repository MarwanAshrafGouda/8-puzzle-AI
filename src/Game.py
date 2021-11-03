import sys
import GameGUI as gui
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
GameGUI = QtWidgets.QMainWindow()
ui = gui.Ui_GameGUI()
ui.setupUi(GameGUI)
GameGUI.show()
sys.exit(app.exec_())

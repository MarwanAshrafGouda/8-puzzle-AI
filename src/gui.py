# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Code\Qt\8-puzzle-ai\form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import random
import timeit
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from algorithms import *
from heuristics import *
from stats import *

default_grid = "012345678"


# noinspection PyAttributeOutsideInit,SpellCheckingInspection
class UiGame(object):
    def setup_ui(self, gui, play_speed, print_configs):
        gui.setObjectName("GameGUI")
        gui.resize(640, 480)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(gui.sizePolicy().hasHeightForWidth())
        gui.setSizePolicy(size_policy)
        gui.setMinimumSize(QtCore.QSize(640, 480))
        gui.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./imgs/ai.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        gui.setWindowIcon(icon)
        self.play_speed = play_speed
        self.print_configs = print_configs
        self.centralwidget = QtWidgets.QWidget(gui)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 431, 431))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.game_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.game_grid.setContentsMargins(0, 0, 0, 0)
        self.game_grid.setObjectName("game_grid")
        self.grid_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.grid_21.setMaximumSize(QtCore.QSize(130, 130))
        self.grid_21.setObjectName("grid_21")
        self.game_grid.addWidget(self.grid_21, 2, 1, 1, 1)
        self.grid_02 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.grid_02.setMaximumSize(QtCore.QSize(130, 130))
        self.grid_02.setObjectName("grid_02")
        self.game_grid.addWidget(self.grid_02, 0, 2, 1, 1)
        self.grid_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.grid_11.setMaximumSize(QtCore.QSize(130, 130))
        self.grid_11.setObjectName("grid_11")
        self.game_grid.addWidget(self.grid_11, 1, 1, 1, 1)
        self.grid_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.grid_20.setMaximumSize(QtCore.QSize(130, 130))
        self.grid_20.setObjectName("grid_20")
        self.game_grid.addWidget(self.grid_20, 2, 0, 1, 1)
        self.grid_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.grid_22.setMaximumSize(QtCore.QSize(130, 130))
        self.grid_22.setObjectName("grid_22")
        self.game_grid.addWidget(self.grid_22, 2, 2, 1, 1)
        self.grid_01 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.grid_01.setMaximumSize(QtCore.QSize(130, 130))
        self.grid_01.setObjectName("grid_01")
        self.game_grid.addWidget(self.grid_01, 0, 1, 1, 1)
        self.grid_00 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.grid_00.setMaximumSize(QtCore.QSize(130, 130))
        self.grid_00.setObjectName("grid_00")
        self.game_grid.addWidget(self.grid_00, 0, 0, 1, 1)
        self.grid_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.grid_12.setMaximumSize(QtCore.QSize(130, 130))
        self.grid_12.setObjectName("grid_12")
        self.game_grid.addWidget(self.grid_12, 1, 2, 1, 1)
        self.grid_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.grid_10.setMaximumSize(QtCore.QSize(130, 130))
        self.grid_10.setObjectName("grid_10")
        self.game_grid.addWidget(self.grid_10, 1, 0, 1, 1)
        self.solve_btn = QtWidgets.QPushButton(self.centralwidget)
        self.solve_btn.setGeometry(QtCore.QRect(470, 400, 141, 31))
        self.solve_btn.setObjectName("solve_btn")
        self.algorithm_box = QtWidgets.QGroupBox(self.centralwidget)
        self.algorithm_box.setGeometry(QtCore.QRect(470, 10, 141, 61))
        self.algorithm_box.setObjectName("algorithm_box")
        self.comboBox = QtWidgets.QComboBox(self.algorithm_box)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.configuration_box = QtWidgets.QGroupBox(self.centralwidget)
        self.configuration_box.setGeometry(QtCore.QRect(470, 90, 141, 161))
        self.configuration_box.setObjectName("configuration_box")
        self.custom_config = QtWidgets.QLineEdit(self.configuration_box)
        self.custom_config.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.custom_config.setObjectName("custom_config")
        self.custom_config.setMaxLength(9)
        self.set_btn = QtWidgets.QPushButton(self.configuration_box)
        self.set_btn.setGeometry(QtCore.QRect(60, 60, 71, 31))
        self.set_btn.setObjectName("set_btn")
        self.shuffle_btn = QtWidgets.QPushButton(self.configuration_box)
        self.shuffle_btn.setGeometry(QtCore.QRect(10, 120, 121, 31))
        self.shuffle_btn.setObjectName("shuffle_btn")
        self.line = QtWidgets.QFrame(self.configuration_box)
        self.line.setGeometry(QtCore.QRect(15, 100, 111, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn.setEnabled(False)
        self.play_btn.setGeometry(QtCore.QRect(470, 330, 141, 56))
        self.play_btn.setObjectName("play_btn")
        gui.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(gui)
        self.statusbar.setObjectName("statusbar")
        gui.setStatusBar(self.statusbar)
        self.set_text(gui)
        self.comboBox.currentIndexChanged.connect(self.disable_play_btn)
        self.comboBox.currentIndexChanged.connect(self.set_grid)
        self.set_btn.clicked.connect(self.set_grid)
        self.shuffle_btn.clicked.connect(self.shuffle_grid)
        self.play_btn.clicked.connect(self.play_path_to_goal)
        self.solve_btn.clicked.connect(self.solve_grid)
        QtCore.QMetaObject.connectSlotsByName(gui)

    def set_text(self, gui):
        _translate = QtCore.QCoreApplication.translate
        gui.setWindowTitle("8 Puzzle Game")
        self.solve_btn.setText("Solve")
        self.algorithm_box.setTitle("Algorithm")
        self.comboBox.setItemText(0, "Depth-first")
        self.comboBox.setItemText(1, "Breadth-first")
        self.comboBox.setItemText(2, "A* Euclidean")
        self.comboBox.setItemText(3, "A* Manhattan")
        self.configuration_box.setTitle("Configuration")
        self.custom_config.setText(default_grid)
        self.custom_config.selectAll()
        self.set_btn.setText("Set")
        self.shuffle_btn.setText("Shuffle")
        self.play_btn.setText("Play")
        self.set_grid()

    def disable_play_btn(self):
        self.play_btn.setText("Play")
        self.play_btn.setEnabled(False)
        self.solve_btn.setFocus(Qt.ShortcutFocusReason)

    def set_grid(self):
        config = self.custom_config.text()

        if not self.valid_grid(config):
            self.custom_config.setText(default_grid)
            config = default_grid

        if not self.solvable(config):
            self.set_status("Warning: unsolvable configuration!")
        else:
            self.set_status("")

        self.disable_play_btn()
        self.grid_00.setText(self.num_img(config[0]))
        self.grid_01.setText(self.num_img(config[1]))
        self.grid_02.setText(self.num_img(config[2]))
        self.grid_10.setText(self.num_img(config[3]))
        self.grid_11.setText(self.num_img(config[4]))
        self.grid_12.setText(self.num_img(config[5]))
        self.grid_20.setText(self.num_img(config[6]))
        self.grid_21.setText(self.num_img(config[7]))
        self.grid_22.setText(self.num_img(config[8]))

    def shuffle_grid(self):
        self.custom_config.setText(''.join(random.sample(default_grid, len(default_grid))))
        self.set_grid()

    def solve_grid(self):
        initial_state = GameState(self.custom_config.text())
        algorithm = self.identify_algorithm(self.comboBox.currentIndex())
        dot = Digraph()
        dot.format = 'png'
        start = timeit.default_timer()
        stats = StatsFile('stats.txt')
        goal, expanded, max_depth, dot = algorithm.search(initial_state, dot)
        stop = timeit.default_timer()
        if self.print_configs:
            for node in expanded:
                stats.write_config(node)
        color = goal
        while color:
            dot.node(string_to_grid(color.configuration), style='filled', fillcolor='lightgreen')
            color = color.parent
        if len(expanded) < 20000:
            dot.render('expanded_nodes.gv', view=True)
            open('expanded_nodes.txt', 'w').close()
        else:
            with open('expanded_nodes.txt', 'w') as f:
                print(dot.source, file=f)
            open('expanded_nodes.gv', 'w').close()
        if goal:
            self.set_status(
                str(round((stop - start) * 1000, 2)) + " ms, search depth: " + str(
                    max_depth) + ", expanded nodes: " + str(len(expanded)))

            stats.write_stat("\nRuntime: " + str((stop - start) * 1000) + " ms")
            stats.write_stat("Number of expanded nodes: " + str(len(expanded)))
            stats.write_stat("Search depth: " + str(max_depth))
            stats.write_stat("Cost: " + str(goal.movement_cost))

            self.path_to_goal = goal
            self.play_btn.setEnabled(True)
            self.play_btn.setFocus(Qt.ShortcutFocusReason)
            self.play_btn.setText("Play ( " + str(goal.movement_cost) + " steps )")
        else:
            self.accumulative_warning()
            msg = QMessageBox()
            msg.setWindowTitle("Oh no!")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Could not solve.")
            msg.setDetailedText("Time: " + str(round((stop - start) * 1000, 2)) + " ms\nSearch depth: " + str(
                max_depth) + "\nExpanded nodes: " + str(len(expanded)))
            msg.exec_()

    def set_status(self, status):
        self.statusbar.showMessage(status)
        self.statusbar.setStatusTip(status)

    def play_path_to_goal(self):
        prev_status = self.statusbar.currentMessage()
        self.disable_play_btn()
        goal = self.path_to_goal
        tmp_config = self.custom_config.text()

        sequence = []
        while goal:
            sequence.append(goal.configuration)
            goal = goal.parent

        for config in reversed(sequence):
            sleep(self.play_speed)
            self.custom_config.setText(config)
            self.set_grid()
            self.custom_config.setText(tmp_config)
            QtCore.QCoreApplication.processEvents()

        # The worst yet perfect solution for the stuck hovering effect.
        self.play_btn.setEnabled(True)
        self.play_btn.setEnabled(False)

        self.custom_config.setText(tmp_config)
        self.set_status(prev_status)

    def accumulative_warning(self):
        if "unsolvable" in self.statusbar.currentMessage():
            self.set_status("Warning: configuration is on unsolvability spree!")
        elif "spree" in self.statusbar.currentMessage():
            self.set_status("Warning: configuration is on rampage!")
        elif "rampage" in self.statusbar.currentMessage():
            self.set_status("Warning: configuration is unstoppable!")
        elif "unstoppable" in self.statusbar.currentMessage():
            self.set_status("Warning: configuration is dominating!")
        elif "dominating" in self.statusbar.currentMessage():
            self.set_status("Warning: configuration is GODLIKE!")
        else:
            self.set_status("Warning: configuration is BEYOND GODLIKE!!!")

    @staticmethod
    def valid_grid(config):
        if len(config) < 9:
            return False
        for i in range(9):
            if not (str(i) in config):
                return False
        return True

    @staticmethod
    def solvable(config):
        # Count inversions in given 8 puzzle
        inv_count = 0
        for i in range(len(config)):
            for j in range(i + 1, len(config)):
                if config[i] != '0' and config[j] != '0' and config[i] > config[j]:
                    inv_count += 1
        return inv_count % 2 == 0

    @staticmethod
    def num_img(num):
        if num in "12345678":
            return str("<html><head/><body><p><img src=\"./imgs/" + num + ".png\"/></p></body></html>")
        else:
            return str("")

    @staticmethod
    def identify_algorithm(index):
        if index == 0:
            return DFS()
        elif index == 1:
            return BFS()
        elif index == 2:
            return AStar(EuclideanHeuristic())
        else:
            return AStar(ManhattanHeuristic())

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QWidget
from PyQt5.QtWidgets import QCheckBox, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtGui import QIcon

class Communicate(QObject):
    generationPass = pyqtSignal() #Сигнал для открытия окна генераций

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.statusBar()

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        editMenu = menubar.addMenu('&Edit')
        viewMenu = menubar.addMenu('&View')
        toolsMenu = menubar.addMenu('&Tools')
        helpMenu = menubar.addMenu('&Help')

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        newAction = QAction('New', self)
        newAction.setShortcut('Ctrl+N')

        saveAction = QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')

        fileMenu.addAction(newAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)

        #--------Edit---------
        addGroupAction = QAction('Add Group',self)
        editGroupAction = QAction('Edit Group', self)
        delGroupAction = QAction('Delete Group', self)

        editMenu.addAction(addGroupAction)
        editMenu.addAction(editGroupAction)
        editMenu.addAction(delGroupAction)


        # --------View---------

        languageAction = QAction('Change Language', self)
        toolbarAction = QAction('Show Toolbar', self)

        viewMenu.addAction(languageAction)
        viewMenu.addAction(toolbarAction)

        # --------Tools---------
        generatePassAction = QAction('Generate Passwoed', self)
        optionsAction = QAction('Options',self)

        toolsMenu.addAction(generatePassAction)
        toolsMenu.addAction(optionsAction)

        generatePassAction.triggered.connect(self.generateShow) #открываем окно генераций

        # --------Help---------
        helpAction = QAction('Help Contents',self)
        donateAction = QAction('Donate',self)
        aboutPtogAction = QAction('About APass', self)

        helpAction.setShortcut('F1')

        helpMenu.addAction(helpAction)
        helpMenu.addAction(donateAction)
        helpMenu.addAction(aboutPtogAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('SPass')
        self.show()

    def generateShow(self):
        generate_s = QWidget(self, Qt.Window)
        generate_s.setWindowModality(Qt.WindowModal)
        generate_s.setGeometry(200, 200, 400, 200)
        generate_s.setWindowTitle('Generation Password')

        app = QtWidgets.QApplication([])

        window = QtWidgets.QWidget(self, Qt.Window)
        window.setWindowModality(Qt.WindowModal)
        window.setLayout(QtWidgets.QVBoxLayout())

        buttons = []
        for i in range(10):
            but = QtWidgets.QCheckBox(f'button {i}')
            but.clicked.connect(lambda event, i=i: print(f'button {i}'))
            window.layout().addWidget(but)
            buttons.append(but)

        window.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())
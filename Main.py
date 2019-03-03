#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import test2

from PyQt5 import QtCore
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

        generatePassAction.triggered.connect(test2.genPassword) #открываем окно генераций

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

        # upper_case = QCheckBox('Upper-case (A, B, C...)')
        # lower_case = QCheckBox('Upper-case (a, b, c...)')
        # digits = QCheckBox('Digits (0, 1, 2...)')
        # special = QCheckBox('Special (!, $, %...')
        # brackets = QCheckBox('Brackets ([, ]')
        #
        # layout = QVBoxLayout()
        # layout2 = QVBoxLayout()
        # layout3 = QVBoxLayout()
        # layout.addWidget(upper_case)
        # layout2.addWidget(lower_case)
        # layout3.addAction(digits)
        #
        #
        # generate_s.setLayout(layout, layout2, layout3) #отображение чекбоксов и др (без QVBoxLayout не работает


        upper_case = QCheckBox('Upper-case (A, B, C...)', generate_s) #geberate_s Написан, чтобы чекбокс отображался
        upper_case.resize(200, 50)
        lower_case = QCheckBox('Lower-case (a, b, c...)', generate_s)
        lower_case.resize(200, 100)
        digits = QCheckBox('Digits (0, 1, 2...)', generate_s)
        digits.resize(200,150)
        special = QCheckBox('Special (!, $, %...)', generate_s)
        special.resize(200, 200)
        brackets = QCheckBox('Brackets ([, ], {, }, (, ), <, >)', generate_s)
        brackets.resize(200, 250)

        generate_s.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())
#!/usr/bin/python
# -*- coding: utf-8 -*-

# gridlayout1.py

import sys
from PyQt4 import QtGui, QtCore


class Calculator(QtGui.QWidget):
  
    def __init__(self):
        super(Calculator, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('grid layout')
        
        names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/',
            '4', '5', '6', '*', '1', '2', '3', '-',
            '0', '.', '=', '+']

        grid = QtGui.QGridLayout()

        j = 0
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
                (1, 0), (1, 1), (1, 2), (1, 3),
                (2, 0), (2, 1), (2, 2), (2, 3),
                (3, 0), (3, 1), (3, 2), (3, 3 ),
                (4, 0), (4, 1), (4, 2), (4, 3)]

        for i in names:
            button = QtGui.QPushButton(i)
            if  j == 2:
                grid.addWidget(QtGui.QLabel(''), 0, 2)
            else:
                self.connect(button, QtCore.SIGNAL('clicked()'), self.buttonClicked)
                grid.addWidget(button, pos[j][0] + 1, pos[j][1] + 1)
            j = j + 1

        # Add the text box for the numbers on the Grid
        self.numbers = QtGui.QLineEdit()
        grid.addWidget(self.numbers, 0, 1, 1, 4)
        
        self.setLayout(grid)

    def buttonClicked(self):
        sender = self.sender()
        self.numbers.setText(sender.text())
        

app = QtGui.QApplication(sys.argv)
ex = Calculator()
ex.show()
sys.exit(app.exec_())
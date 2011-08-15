#!/usr/bin/python
# -*- coding: utf-8 -*-

# gridlayout1.py

import sys
from PyQt4 import QtGui, QtCore

class Calculator(QtGui.QWidget):
    
    previous = ''
    current = ''
    operator = ''
  
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
        # If the pushed button contains a numeric value, append it to the current value
        if str(sender.text()).isdigit():
            self.current += sender.text()
            self.numbers.setText(self.current)
        else:
            if sender.text() == '=':
                return self.calculate()
            elif sender.text() == "Close" or sender.text() == 'Cls' or sender.text == 'Bck':
                return None
                #self.command(sender.text())
            self.operator = sender.text()
            self.numbers.setText('')
            self.previous = self.current
            self.current = ''
    
    def calculate(self):
        if self.operator == '+':
            result = int(self.previous) + int(self.current)
        elif self.operator == '-':
            result = int(self.previous) - int(self.current)
        elif self.operator == '*':
            result = int(self.previous) * int(self.current)
        elif self.operator == '/':
            result = int(self.previous) - int(self.current)
        
        self.numbers.setText(str(result))


app = QtGui.QApplication(sys.argv)
ex = Calculator()
ex.show()
sys.exit(app.exec_())
#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
# from PyQt5.QtWidgets import *


class MainWindow(QFrame):

    style = '''
        QFrame{
            border-image: url(bear.jpg);
        }
    '''

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setStyleSheet(self.style)
        self.resize(800, 600)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())

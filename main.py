#!/usr/bin/python
# -*- coding: utf-8 -*-

from qframer.qt.QtCore import *
from qframer.qt.QtGui import *
from qframer import FSplashScreen

from gui import MainWindow
from gui.uiconfig import windowsoptions


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    if windowsoptions['splashflag']:
        splash = FSplashScreen(1, windowsoptions['splashimg'])
        mainwindow = MainWindow()
        mainwindow.show()
        splash.finish(mainwindow)
    else:
        mainwindow = MainWindow()
        mainwindow.show()
    sys.exit(app.exec_())

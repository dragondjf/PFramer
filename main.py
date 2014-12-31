#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
os.environ['QT_API'] = "PySide"
from qframer.qt.QtCore import *
from qframer.qt.QtGui import *
from qframer import FSplashScreen

from gui import MainWindow
from gui.uiconfig import windowsoptions

from qframer.qt import QtCore

print('using %s(%s)' % (os.environ['QT_API'], QtCore.__version__))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    if windowsoptions['splashflag']:
        splash = FSplashScreen(1, windowsoptions['splashimg'])
        mainwindow = MainWindow()
        mainwindow.show()
        splash.finish(mainwindow)
    else:
        mainwindow = MainWindow()
        mainwindow.show()

    mainwindow.guimanger.globals = globals()
    mainwindow.guimanger.locals = locals()

    exitCode = app.exec_()
    sys.exit(exitCode)

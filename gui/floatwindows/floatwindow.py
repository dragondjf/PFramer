#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class FloatWindow(QDockWidget):
    def __init__(self, childwidget, name="", parent=None):
        super(FloatWindow, self).__init__(name, parent)
        self.parent = parent
        self.name = name
        self.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.setWidget(childwidget)
        # menubar = self.parent.menuBar()
        # if hasattr(menubar, '%smenu' % "View"):
        #     if name == "Device" and sys.platform == "darwin":
        #         return
        #     getattr(menubar, '%smenu' % "View").addAction(self.toggleViewAction())

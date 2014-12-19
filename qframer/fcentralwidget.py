#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
try:
    from qt.QtCore import *
    from qt.QtGui import *
except ImportError:
    from PySide.QtCore import *
    from PySide.QtGui import *

from .ftitlebar import FTitleBar


class FCentralWidget(QFrame):

    def __init__(self, parent=None):
        super(FCentralWidget, self).__init__(parent)
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        mainlayout = QVBoxLayout()
        mainlayout.setContentsMargins(0, 0, 0, 0)
        mainlayout.setSpacing(0)
        self.setLayout(mainlayout)

    def addTitleBar(self, titleBar):
        self.titlebar = titleBar
        self.addWidget(titleBar)

    def getTitleBar(self):
        if hasattr(self, 'titlebar'):
            return self.titlebar
        else:
            return None

    def addWidget(self, widget):
        self.layout().addWidget(widget)

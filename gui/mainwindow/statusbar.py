#!/usr/bin/python
# -*- coding: utf-8 -*-

from qframer.qt.QtCore import *
from qframer.qt.QtGui import *
from qframer import FStatusBar
from qframer import collectView, views

class StatusBar(FStatusBar):

    viewID = "StatusBar"

    @collectView
    def __init__(self, parent=None):
        super(StatusBar, self).__init__(parent)
        self.datatimelabel.setObjectName("datatimelabel")

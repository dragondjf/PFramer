#!/usr/bin/python
# -*- coding: utf-8 -*-

from qframer.qt.QtCore import *
from qframer.qt.QtGui import *
from qframer import FFloatWidget


class FloatPage(FFloatWidget):

    def __init__(self, parent=None):
        super(FloatPage, self).__init__(parent)
        self.setObjectName("FloatWidget")
        self.isShowed = False

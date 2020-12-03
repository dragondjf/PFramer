#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from qframer import FFloatWidget


class FloatPage(FFloatWidget):

    def __init__(self, parent=None):
        super(FloatPage, self).__init__(parent)
        self.setObjectName("FloatWidget")
        self.isShowed = False

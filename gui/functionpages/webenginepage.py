#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from qframer import collectView
from qframer import FWebEnginePage


class WebEnginePage(FWebEnginePage):

    viewID = "WebEnginePage"

    @collectView
    def __init__(self, parent=None):
        super(WebEnginePage, self).__init__(parent)
        self.setObjectName("WebEnginePage")
        self.parent = parent
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        url = QUrl("http://www.baidu.com")
        self.load(url)

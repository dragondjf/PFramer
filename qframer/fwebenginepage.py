#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import *
from PySide2.QtNetwork import *


class FWebEnginePage(QWebEngineView):

    def __init__(self, parent=None):
        super(FWebEnginePage, self).__init__(parent)
        self.load("www.baidu.com")


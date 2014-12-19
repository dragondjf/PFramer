#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from qframer.qt.QtCore import *
from qframer.qt.QtGui import *
from qframer import views, collectView

from qframer import FWebkitBasePage


class WebKitPage(FWebkitBasePage):

    viewID = "WebKitPage"

    @collectView
    def __init__(self, parent=None):
        super(WebKitPage, self).__init__(parent)
        self.setObjectName("WebKitPage")
        self.parent = parent
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        url = QUrl("http://www.baidu.com")
        self.view.load(url)

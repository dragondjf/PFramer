#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from datetime import datetime


class FStatusBar(QStatusBar):

    def __init__(self, parent=None):
        super(FStatusBar, self).__init__(parent)
        self.parent = parent
        self.initStatusbar()
        # self.initUI()
        # self.startTimer(1000)

    def startTimer(self, interval):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updateDataLabel)
        self.timer.start()

    def initStatusbar(self):
        statusbarSettings = {
            'initmessage': u'Ready',
            'minimumHeight': 30,
            'visual': True,
        }
        self.showMessage(statusbarSettings['initmessage'])
        self.setMinimumHeight(statusbarSettings['minimumHeight'])
        self.setVisible(statusbarSettings['visual'])

    def initUI(self):
        self.datatimelabel = QLabel(self)
        self.datatimelabel.setText(
            datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
        self.datatimelabel.show()
        self.addPermanentWidget(self.datatimelabel)

    def updateDataLabel(self):
        self.datatimelabel.setText(
            datetime.today().strftime("%Y-%m-%d %H:%M:%S"))

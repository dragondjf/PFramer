#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from qframer import views, collectView
from qframer.animationwidget import FAnimationFrame


class ExitFrame(QFrame):

    style = '''
        QFrame#ExitPage{
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 82, 112, 255), stop:0.5 rgba(0, 211, 197, 255), stop:1 rgba(0, 82, 112, 255));
        }
    '''

    def __init__(self, parent=None):
        super(ExitFrame, self).__init__(parent)
        self.parent = parent
        self.setObjectName("ExitPage")
        self.initUI()
        self.setStyleSheet(self.style)

    def initUI(self):
        self.setFixedHeight(200)

        self.enterLayout = QHBoxLayout()
        self.pbEnter = QPushButton(u'确定', self)
        self.pbCancel = QPushButton(u'取消', self)
        self.pbEnter.setFixedSize(120, 40)
        self.pbCancel.setFixedSize(120, 40)
        self.enterLayout.addStretch()
        self.enterLayout.addWidget(self.pbEnter)
        self.enterLayout.addWidget(self.pbCancel)

        mainLayout = QVBoxLayout()
        mainLayout.addStretch()
        mainLayout.addLayout(self.enterLayout)
        self.setLayout(mainLayout)

        self.pbEnter.clicked.connect(self.parent.exited)
        self.pbCancel.clicked.connect(self.parent.hide)


class ExitPage(FAnimationFrame):

    style = '''
        QFrame{
            background-color: lightgray;
        }
        QFrame#Exit{
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 82, 112, 255), stop:0.5 rgba(0, 211, 197, 255), stop:1 rgba(0, 82, 112, 255));
        }
    '''

    exited = Signal()

    def __init__(self, parent=None):
        super(ExitPage, self).__init__(parent)
        self.initUI()
        self.setStyleSheet(self.style)
        self.graphicsOpacityEffect = QGraphicsOpacityEffect(self)
        self.graphicsOpacityEffect.setOpacity(0.8)
        self.setGraphicsEffect(self.graphicsOpacityEffect)

    def initUI(self):
        mainLayout = QVBoxLayout()

        self.exitFrame = ExitFrame(self)
        mainLayout.addSpacing(self.blankSpacingHeight() * 0.9)
        mainLayout.addWidget(self.exitFrame)
        mainLayout.addStretch()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

    def blankSpacingHeight(self):
        return (self.h - self.exitFrame.height())/ 2

#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from qframer import views, collectView


class RPCEditPage(QFrame):

    viewID = "RPCEditPage"

    ListWidgetWidth_desktop = 200
    ListWidgetWidth_phone = 400

    @collectView
    def __init__(self, parent=None):
        super(RPCEditPage, self).__init__(parent)
        self.parent = parent
        self.initData()
        self.initUI()
        self.initConnect()
        self.setDesktopMode()

    def initData(self):
        self.currentRPCName = None

    def initUI(self):
        self.rpcListWidget = QListWidget(self)
        self.rpcListWidget.setFocusPolicy(Qt.NoFocus)

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.rpcListWidget)
        mainLayout.addStretch()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        self.rpcWidgets = {}
        for i in range(100):
            name  = "RPC_%d" % i
            self.rpcListWidget.addItem(name)
            self.rpcWidgets.update({name: BaseRPCEditFrame})

    def setDesktopMode(self):
        self.rpcListWidget.setFixedWidth(self.ListWidgetWidth_desktop)

    def initConnect(self):
        views['MainWindow'].titleBar().modeed.connect(self.changeMode)
        self.rpcListWidget.currentTextChanged.connect(self.updateRPCEditWidget)

        # self.rpcListWidget.setCurrentRow(0)
        self.t = QTimer()
        self.t.timeout.connect(self.initFirstRPC)
        self.t.setSingleShot(True)
        self.t.start(500)

    def initFirstRPC(self):
        self.rpcListWidget.setCurrentRow(4)

    def changeMode(self, flag):
        if flag:
            self.rpcListWidget.setFixedWidth(self.ListWidgetWidth_phone)
        else:
            self.rpcListWidget.setFixedWidth(self.ListWidgetWidth_desktop)

        self.updateRPCEditWidget(self.currentRPCName)

    def updateRPCEditWidget(self, rpcName):
        self.currentRPCName = rpcName
        if hasattr(self, 'rpcWidget') and self.rpcWidget:
            self.rpcWidget.hide()
            del self.rpcWidget
        self.rpcWidget = self.rpcWidgets[rpcName](QLabel(rpcName), self)
        self.rpcWidget.animationShow()


class BaseRPCEditFrame(QFrame):

    style = '''
        QFrame{
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 82, 112, 255), stop:0.5 rgba(0, 211, 197, 255), stop:1 rgba(0, 82, 112, 255));
        }
    '''

    def __init__(self, rpcWidget, parent=None):
        super(BaseRPCEditFrame, self).__init__(parent)
        self.parent = parent
        self.rpcWidget = rpcWidget
        self._initShowAnimation()
        self._initHideAnimation()
        self._initUI()
        self._initConnect()

    def _initUI(self):
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.rpcWidget)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        self.setStyleSheet(self.style)

    def _initConnect(self):
        pass

    @property
    def startX(self):
        return self.parent.width()

    @property
    def endX(self):
        if views['MainWindow'].isDesktopMode():
            return 0
        else:
            return self.parent.ListWidgetWidth_desktop

    @property
    def startRect(self):
        startX = self.parent.width()
        startRect = QRect(self.startX, 0, self.w, self.h)
        return startRect

    @property
    def endRect(self):
        endRect = QRect(self.endX, 0, self.w, self.h)
        return endRect

    @property
    def h(self):
        return self.parent.height()

    @property
    def w(self):
        if views['MainWindow'].isDesktopMode():
            width = self.parent.width()
        else:
            width = self.parent.width() - self.parent.ListWidgetWidth_desktop
        return width

    def _initShowAnimation(self):
        self.showanimation = QPropertyAnimation(self, 'geometry')
        self.showanimation.setStartValue(self.startRect)
        self.showanimation.setEndValue(self.endRect)
        self.showanimation.setDuration(200)
        self.showanimation.setEasingCurve(QEasingCurve.OutCubic)

    def _initHideAnimation(self):
        self.hideanimation = QPropertyAnimation(self, 'geometry')
        self.hideanimation.setStartValue(self.endRect)
        self.hideanimation.setEndValue(self.startRect)
        self.hideanimation.setDuration(200)
        self.hideanimation.setEasingCurve(QEasingCurve.OutCubic)
        self.hideanimation.finished.connect(self.hide)

    def animationShow(self):
        self.show()
        self.showanimation.start()

    def animationHide(self):
        self.hideanimation.start()

    def mouseDoubleClickEvent(self, event):
        self.animationHide()
        super(BaseRPCEditFrame, self).mouseDoubleClickEvent(event)

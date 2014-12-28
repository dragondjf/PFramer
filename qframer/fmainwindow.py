#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json

try:
    from .qt.QtCore import *
    from .qt.QtGui import *
except ImportError:
    from PySide.QtCore import *
    from PySide.QtGui import *

from .ftitlebar import FTitleBar
from .fmenubar import FMenuBar
from .fstatusbar import FStatusBar
from .fcentralwidget import FCentralWidget
from .futil import setSkinForApp


class FMainWindow(QMainWindow):

    sizeChanged = Signal()

    def __init__(self):
        super(FMainWindow, self).__init__()
        self._initFlags()
        self._initWindowFlags()
        self._initMainWindow()
        self._initCenterWindow()

        self._initTitleBar()
        self._initTitlebarConnect()
        
        self._initToolbars()
        self._initStatusbar()

    def _initFlags(self):
        self._framelessflag = True # 无系统边框标志
        self._customTitlebarFlag = True # 自定义标题栏标志
        self._menubarFlag = False
        self._maximizedflag = False  # 初始化时窗口最大化标志
        self._lockflag = False # 锁定标志
        self._pinflag = False # 置顶标志
        self._modeflag = False # 手机(True)或桌面模式(False)

        desktopWidth = QDesktopWidget().availableGeometry().width()
        desktopHeight = QDesktopWidget().availableGeometry().height()
        self.default_size = QSize(desktopWidth * 0.8, desktopHeight * 0.8)
        self.phone_size = QSize(400, desktopHeight * 0.8)
        self.oldPosition = QPoint(0, 0)

    def _initWindowFlags(self, flag=True):
        framelessflag = flag
        if framelessflag:
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)  # 无边框， 带系统菜单， 可以最小化
        else:
            self.setWindowFlags(Qt.CustomizeWindowHint)
        self._framelessflag = framelessflag

    def _initMainWindow(self):
        self.showNormal()
        self.moveCenter()
        self.oldPosition = self.pos()

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.layout().setContentsMargins(0, 0, 0, 0)

    def _initCenterWindow(self):
        centeralwindow = FCentralWidget(self)
        self.setCentralWidget(centeralwindow)

    def addCoreWidget(self, widget):
        if isinstance(self.centralWidget(), FCentralWidget):
            self.centralWidget().addWidget(widget)

    def _initTitleBar(self, flag=True):
        self._customTitlebarFlag = flag
        if self._customTitlebarFlag:
            self._titleBar = FTitleBar()
            self.centralWidget().addTitleBar(self._titleBar)

    def titleBar(self):
        if self._customTitlebarFlag:
            return self._titleBar

    def _initTitlebarConnect(self):
        if self.isFtitleBarExisted():
            self._titleBar.locked.connect(self.setLocked)
            self._titleBar.modeed.connect(self.setMode)
            self._titleBar.pined.connect(self.setPined)
            self._titleBar.minimized.connect(self.showMinimized)
            self._titleBar.maximized.connect(self.swithMaxNormal)

    def isFtitleBarExisted(self):
        if self._customTitlebarFlag:
            if hasattr(self, 'titleBar') and isinstance(self._titleBar, FTitleBar):
                return True
        return False

    def _initToolbars(self):
        pass

    def _initStatusbar(self):
        statusbar = FStatusBar(self)
        self.setStatusBar(statusbar)

    def setWindowIcon(self, icon):
        if not isinstance(icon, QIcon):
            qicon = QIcon(icon)
        else:
            qicon = icon
        super(FMainWindow, self).setWindowIcon(qicon)
        if self.isFtitleBarExisted():
            self._titleBar.setLogo(qicon)

    def setWindowTitle(self, title):
        super(FMainWindow, self).setWindowTitle(title)
        if self.isFtitleBarExisted():
            self._titleBar.setTitle(title)

    def setMode(self, flag):
        self._modeflag = flag
        if flag:
            self.resize(self.phone_size.width(), self.height())
        else:
            self.resize(self.default_size)

    def getModeFlag(self):
        return self._modeflag

    def setPined(self, flag):
        self._pinflag = flag
        if flag:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.windowFlags() & (~Qt.WindowStaysOnTopHint))
        self.show()

    def setLocked(self, flag):
        self._lockflag = flag

    def isLocked(self):
        return self._lockflag

    def moveCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def swithMaxNormal(self, flag):
        self._maximizedflag = flag
        if self._maximizedflag:
            self.showMaximized()
        else:
            self.showNormal()

    def showMaximized(self):
        self.resize(QDesktopWidget().availableGeometry().size())
        self.moveCenter()

    def showNormal(self):
        self.resize(self.default_size)
        self.move(self.oldPosition)        

    def isMaximized(self):
        return self._maximizedflag

    def resizeEvent(self, event):
        super(FMainWindow, self).resizeEvent(event)
        self.default_size = event.oldSize()
        self.sizeChanged.emit()

    def mousePressEvent(self, event):
        self.setFocus()
        # 鼠标点击事件
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - \
                self.frameGeometry().topLeft()
            event.accept()

    def mouseReleaseEvent(self, event):
        # 鼠标释放事件
        if hasattr(self, "dragPosition"):
            del self.dragPosition

    def mouseMoveEvent(self, event):
        self.oldPosition = self.pos()
        # 鼠标移动事件
        if self.isMaximized():
            event.ignore()
        else:
            if not self.isLocked():
                if hasattr(self, "dragPosition"):
                    if event.buttons() == Qt.LeftButton:
                        self.move(event.globalPos() - self.dragPosition)
                        event.accept()

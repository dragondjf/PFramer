#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json

from qframer.qt.QtCore import *
from qframer.qt.QtGui import *
from qframer import views, collectView
from qframer import FMainWindow
from qframer import setSkinForApp
import qframer.dialogs as dialogs

from .menubar import MenuBar
from .statusbar import StatusBar

from gui.uiconfig import windowsoptions
from gui.menus import SettingsMenu, SkinMenu
from gui.floatwindows import LogWindow, HistoryWindow, FloatWindow
from gui.functionpages import RPCEditPage
from .guimanger import GuiManger


class MainWindow(FMainWindow):

    viewID = "MainWindow"

    @collectView
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.setskin()
        self.guimanger = GuiManger()

    def initUI(self):
        mainwindow = windowsoptions['mainwindow']
        self.initSize()

        self.setWindowIcon(mainwindow['icon'])
        self.setWindowTitle(mainwindow['title'])

        self.initTitleBar()
        self.addCoreWidget(RPCEditPage(self))

        self.initDockwindow()

        self.statusBar().datatimelabel.setObjectName("datatimelabel")

    def initSize(self):
        mainwindow = windowsoptions['mainwindow']
        desktopWidth = QDesktopWidget().availableGeometry().width()
        desktopHeight = QDesktopWidget().availableGeometry().height()
        self.resize(desktopWidth * mainwindow['size'][0], desktopHeight * mainwindow['size'][1])
        self.moveCenter()

    def initTitleBar(self):
        if self.isFtitleBarExisted():
            self.titleBar().setObjectName("FTitleBar")
            self.titleBar().titleLabel.setObjectName("TitleLabel")
            self.titleBar().closeButton.setObjectName("close")
            self.settingsMenu = SettingsMenu(self)
            self.titleBar().settingDownButton.setMenu(self.settingsMenu)
            self.skinMenu = SkinMenu(self)
            self.skinMenu.setFixedWidth(100)
            self.titleBar().skinButton.setMenu(self.skinMenu)
            self.initTitleBarMenuConnect()

    def initTitleBarMenuConnect(self):
        self.titleBar().settingMenuShowed.connect(self.titleBar().settingDownButton.showMenu)
        self.titleBar().skinMenuShowed.connect(self.titleBar().skinButton.showMenu)
        self.skinMenu.skinIDSin.connect(self.setskin)

    def initDockwindow(self):
        # Log
        self.logwindow = LogWindow(self)
        self.logfloatwindow = FloatWindow(self.logwindow, self.tr("Log"), self)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.logfloatwindow)

        # History
        self.historywindow = HistoryWindow(self)
        self.historyfloatwindow = FloatWindow(self.historywindow, self.tr("Histroy"), self)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.historyfloatwindow)

        self.logfloatwindow.setFixedHeight(194)
        self.historyfloatwindow.setFixedHeight(194)

        self.tabifyDockWidget(self.logfloatwindow, self.historyfloatwindow)

        self.tabbar = self.findChildren(QTabBar)
        self.tabbar[0].setCurrentIndex(0)

    def setskin(self, skinID="BB"):
        setSkinForApp('gui/skin/qss/%s.qss' % skinID)  # 设置主窗口样式

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_F11:
            if self.isFtitleBarExisted():
                self.titleBar().maxButton.clicked.emit()
        elif event.key() == Qt.Key_F9:
            pass
        elif event.key() == Qt.Key_F8:
            bar = self.statusBar()
            bar.setVisible(not bar.isVisible())

    # def closeEvent(self, evt):
    #     flag, exitflag = dialogs.exit(windowsoptions['exitdialog'])
    #     if flag:
    #         for item in exitflag:
    #             if item == 'minRadio' and exitflag[item]:
    #                 self.showMinimized()
    #                 evt.ignore()
    #             elif item == 'exitRadio' and exitflag[item]:
    #                 evt.accept()
    #             elif item == 'exitsaveRadio' and exitflag[item]:
    #                 evt.accept()
    #                 self.saveoptions()
    #                 if not os.path.exists("options"):
    #                     os.mkdir("options")
    #                 with open("options\windowsoptions.json", 'w') as f:
    #                     json.dump(windowsoptions, f, indent=4)
    #     else:
    #         evt.ignore()

    def saveoptions(self):
        from gui.uiconfig import windowsoptions
        windowsoptions['mainwindow']['maximizedflag'] = self.isMaximized()

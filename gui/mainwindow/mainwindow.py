#!/usr/bin/python
# -*- coding: utf-8 -*-

from qframer.qt.QtCore import *
from qframer.qt.QtGui import *
from qframer import views, collectView
from qframer import FMainWindow
from qframer import FSuspensionWidget
from qframer import setSkinForApp

from gui.uiconfig import windowsoptions
from gui.menus import SettingsMenu, SkinMenu
from gui.floatwindows import LogWindow, HistoryWindow
from gui.floatwindows import InitHistoryWindow, FloatWindow
from gui.functionpages import FloatPage, ScrollWidget, TablePage
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

        self.initMenus()

        self.initTitleBar()
        self.setCentralWidget(TablePage(self))

        self.initDockwindow()

        self.initSizeGrip()

        self.setSystemTrayMenu(self.settingsMenu)

        self.suspensionWidget = FSuspensionWidget(
            'gui/skin/images/PFramer.png', self)
        self.suspensionWidget.setContextMenu(self.settingsMenu)
        self.suspensionWidget.move(self.frameGeometry().topRight()
                                   + QPoint(20, 20))

        self.floatWidget = FloatPage(self)

    def initSize(self):
        mainwindow = windowsoptions['mainwindow']
        desktopWidth = QDesktopWidget().availableGeometry().width()
        desktopHeight = QDesktopWidget().availableGeometry().height()
        self.resize(
            desktopWidth * mainwindow['size'][0],
            desktopHeight * mainwindow['size'][1])
        self.moveCenter()

    def initMenus(self):
        self.settingsMenu = SettingsMenu(self)
        self.skinMenu = SkinMenu(self)
        self.skinMenu.setFixedWidth(100)

    def initTitleBar(self):
        if self.isFtitleBarExisted():
            self.titleBar().closeButton.setObjectName("close")
            self.titleBar().settingDownButton.setMenu(self.settingsMenu)
            self.titleBar().skinButton.setMenu(self.skinMenu)
            self.initTitleBarMenuConnect()

    def initTitleBarMenuConnect(self):
        self.titleBar().settingMenuShowed.connect(
            self.titleBar().settingDownButton.showMenu)
        self.titleBar().skinMenuShowed.connect(
            self.titleBar().skinButton.showMenu)
        self.skinMenu.skinIDSin.connect(self.setskin)

    def initDockwindow(self):
        self.dockwindows = []
        # Log
        self.logwindow = LogWindow(self)
        self.logfloatwindow = FloatWindow(self.logwindow, self.tr("Log"), self)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.logfloatwindow)

        # History
        self.historywindow = HistoryWindow(self)
        self.historyfloatwindow = FloatWindow(
            self.historywindow, self.tr("Histroy"), self)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.historyfloatwindow)

        # Init History
        self.initHistorywindow = InitHistoryWindow(parent=self)
        self.initHistoryFloatwindow = FloatWindow(
            self.initHistorywindow, self.tr("Init"), self)
        self.addDockWidget(
            Qt.BottomDockWidgetArea, self.initHistoryFloatwindow)

        self.logfloatwindow.setFixedHeight(194)
        self.historyfloatwindow.setFixedHeight(194)
        self.initHistoryFloatwindow.setFixedHeight(194)

        self.dockwindows.append(self.logfloatwindow)
        self.dockwindows.append(self.historyfloatwindow)
        self.dockwindows.append(self.initHistoryFloatwindow)
        for dock in self.dockwindows:
            dock.hide()

        self.tabifyDockWidget(self.logfloatwindow, self.historyfloatwindow)
        self.tabifyDockWidget(
            self.historyfloatwindow, self.initHistoryFloatwindow)

        self.tabbar = self.findChildren(QTabBar)
        self.tabbar[0].setCurrentIndex(0)

    def initSizeGrip(self):
        self.sizeGrip = QSizeGrip(self)
        self.sizeGrip.hide()

    def setskin(self, skinID="BB"):
        setSkinForApp('gui/skin/qss/%s.qss' % skinID)  # 设置主窗口样式

    def hideEvent(self, event):
        super(MainWindow, self).hideEvent(event)
        if hasattr(self, 'floatWidget') and self.floatWidget:
            if self.floatWidget.titleBar.isPined():
                self.floatWidget.show()
            else:
                self.floatWidget.hide()

    def showEvent(self, event):
        super(MainWindow, self).showEvent(event)
        if hasattr(self, 'floatWidget') and self.floatWidget.isShowed:
            self.floatWidget.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.titleBar().closeButton.click()
        elif event.key() == Qt.Key_F11:
            if self.isFtitleBarExisted():
                self.titleBar().maxButton.clicked.emit()
        elif event.key() == Qt.Key_F9:
            pass
        elif event.key() == Qt.Key_F8:
            bar = self.statusBar()
            bar.setVisible(not bar.isVisible())
            self.sizeGrip.setVisible(not bar.isVisible())
        elif event.key() == Qt.Key_F12:
            self.guimanger.actionObjectView()
        else:
            super(MainWindow, self).keyPressEvent(event)

    def resizeEvent(self, event):
        super(MainWindow, self).resizeEvent(event)
        self.sizeGrip.move(
            self.size().width() - 100, self.size().height() - 30)

    def mouseMoveEvent(self, event):
        super(MainWindow, self).mouseMoveEvent(event)
        if hasattr(self, 'floatWidget') and self.floatWidget:
            if not self.floatWidget.isLocked():
                self.floatWidget.setGeometry(self.floatWidget.endRect)

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

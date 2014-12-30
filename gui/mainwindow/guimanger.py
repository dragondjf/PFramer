#!/usr/bin/python
# -*- coding: utf-8 -*-

from qframer.qt.QtCore import *
from qframer.qt.QtGui import *

from gui.functionpages import LoginPage, AboutPage, ExitPage
from qframer import views, collectView

from log import logger


class GuiManger(QObject):

    """docstring for GuiManger"""

    def __init__(self, parent=None):
        super(GuiManger, self).__init__()
        self.parent = parent
        self.menuActionConnect()
        self.settingMenuActionConnect()
        self.createControllers()
        views['MainWindow'].titleBar().closed.connect(self.actionExit)

        # from .rpcapplication import rpcApp

        # for key, p in rpcApp.plugins.items():
        #     print(key, p.__dict__)

    def menuActionConnect(self):
        if hasattr(views['MainWindow'].menuBar(), 'qactions'):
            for name, action in views['MainWindow'].menuBar().qactions.items():
                if hasattr(self, 'action%s' % name):
                    action.triggered.connect(
                        getattr(self, 'action%s' % name)
                    )
                else:
                    action.triggered.connect(
                        getattr(self, 'actionNotImplement')
                    )

    def settingMenuActionConnect(self):
        if views['MainWindow'].isFtitleBarExisted():
            for name, action in views['MainWindow'].settingsMenu.qactions.items():
                    if hasattr(self, 'action%s' % name):
                        action.triggered.connect(
                            getattr(self, 'action%s' % name)
                        )
                    else:
                        action.triggered.connect(
                            getattr(self, 'actionNotImplement')
                        )

    def createControllers(self):
        pass

    def actionLogin(self):
        if hasattr(self, 'loginPage'):
            self.loginPage.hide()
            self.loginPage.deleteLater()
        self.loginPage = LoginPage(views['MainWindow'])
        self.loginPage.animationShow()

    def actionSuspension(self):
        sw = views['MainWindow'].suspensionWidget
        sw.setVisible(not sw.isVisible())
        if sw.isVisible():
            self.sender().setText('Hide suspension window')
        else:
            self.sender().setText('Show suspension window')

    def actionAndroidDeveloper(self):
        logger.info("Android guide")

    def actionIOSDeveloper(self):
        logger.info("IOS guide")

    def actionFordDeveloper(self):
        url = "https://developer.ford.com"
        QDesktopServices.openUrl(QUrl(url))

    def actionAbout(self):
        if hasattr(self, 'aboutPage'):
            self.aboutPage.hide()
            self.aboutPage.deleteLater()
        self.aboutPage = AboutPage(views['MainWindow'])
        self.aboutPage.animationShow()

    def actionExit(self):
        if hasattr(self, 'exitPage'):
            self.exitPage.hide()
            self.exitPage.deleteLater()
        self.exitPage = ExitPage(views['MainWindow'])
        self.exitPage.exited.connect(self.close)
        self.exitPage.animationShow()

    def actionNotImplement(self):
        logger.info("actionNotImplement")

    def close(self):
        views['MainWindow'].close()

#!/usr/bin/python
# -*- coding: utf-8 -*-

from qframer.qt.QtCore import *
from qframer.qt.QtGui import *
from qframer import views
from gui.functionpages import LoginPage, AboutPage, ExitPage
from database import signal_DB
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
        views['MainWindow'].floatWidget.titleBar.closed.connect(self.updateFloatMenu)
        # from .rpcapplication import rpcApp

        # for key, p in rpcApp.plugins.items():
        #     print(key, p.__dict__)

        rpcs = [{
            'type': 'show %d' % i,
            'data': {"show": 'dfdfdfdf', 'text': [i, i, i]}
        } for i in range(10)]

        signal_DB.uu_initAddBatch.emit(rpcs)

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

    def actionFloat(self):
        sw = views['MainWindow'].floatWidget
        if sw.isVisible():
            self.sender().setText('Show float window')
            sw.animationHide()
        else:
            self.sender().setText('Hide float window')
            sw.animationShow()
            sw.isShowed = True

    def updateFloatMenu(self):
        action = views['MainWindow'].settingsMenu.getActionByName('Float')
        if action:
            action.setText('Show float window')

    def actionDock(self):
        dockwindows = views['MainWindow'].dockwindows
        for dock in dockwindows:
            dock.setVisible(not dock.isVisible())

        if dockwindows[0].isVisible():
            self.sender().setText('Hide dock window')
        else:
            self.sender().setText('Show dock window')

    def actionAndroidDeveloper(self):
        logger.info("Android guide")

    def actionIOSDeveloper(self):
        logger.info("IOS guide")

    def actionFordDeveloper(self):
        url = "https://developer.ford.com"
        QDesktopServices.openUrl(QUrl(url))

    def actionObjectView(self):
        from qframer import FGlobalSearchWidget
        if hasattr(self, 'searchBar'):
            self.searchBar.hide()
            self.searchBar.deleteLater()
        self.searchBar = FGlobalSearchWidget(views['MainWindow'])
        self.searchBar.searchEdit.setPlaceholderText(self.tr("Search object"))
        self.searchBar.animationShow()
        self.searchBar.setFocus()
        self.searchBar.searchEdit.returnPressed.connect(self.browserObj)

    def browserObj(self):
        from objbrowser import browse
        objstr = self.sender().text()

        def getRootObj(objstr):
            if objstr in self.locals:
                return self.locals[objstr]
            elif objstr in self.globals:
                return self.globals[objstr]
            else:
                return None

        if '.' not in objstr:
            obj = getRootObj(objstr)
            if obj:
                browse(obj)
            else:
                print("root obj not found")
        else:
            objlist = objstr.split('.')
            ret = getRootObj(objlist[0])
            if ret:
                try:
                    for attr in objlist[1:]:
                        ret = getattr(ret, attr)
                    browse(ret)
                except Exception as e:
                    print(e)
            else:
                print("root obj not found")

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
        app = QApplication.instance()
        app.closeAllWindows()
        app.quit()

#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from qframer.qt.QtCore import *
from qframer.qt.QtGui import *
from qframer import views, collectView
from qframer.animationwidget import FAnimationFrame


class IconLineEdit(QLineEdit):


    def __init__(self, iconPath=None, parent=None):
        super(IconLineEdit, self).__init__(parent)

        style = '''QLabel{
            background-color: transparent;
            border-image:url(%s)
        }''' % iconPath

        self.iconLabel = QLabel(self)
        self.iconLabel.setStyleSheet(style)


    def resizeEvent(self, event):
        space = 3
        self.iconLabel.setFixedSize(self.height() - space, self.height() - space * 2)
        self.iconLabel.move(self.width() - self.height() - space, space)




class LoginPage(FAnimationFrame):

    style = '''
        QFrame{
            background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:1, fx:0.5, fy:0.5, stop:0 rgba(119, 255, 255, 255), stop:1 rgba(32, 127, 155, 255));
        }
        QFrame#LoginBgFrame{
            border: 100px solid;
            border-image: url(gui/skin/images/imac.png);
            background-color: transparent;
        }

        QFrame#LoginFrame{
            position: relative;
            padding: 24px 23px 20px;
            background-color: #edeff1;
            border-radius: 6px;
        }

    '''

    def __init__(self, parent=None):
        super(LoginPage, self).__init__(parent)
        self.initUI()

    def initSetData(self):
        pass

    def initUI(self):
        self.loginBgFrame = QFrame()
        self.loginBgFrame.setObjectName("LoginBgFrame")

        self.loginFrame = QFrame()
        self.loginFrame.setObjectName("LoginFrame")

        self.userLineEdit = IconLineEdit(":/icons/light/appbar.user.tie.png")
        self.userLineEdit.setFixedHeight(36)
        self.userLineEdit.setPlaceholderText(self.tr("Enter your name"))
        self.passwordLineEdit = IconLineEdit(":/icons/light/appbar.lock.png")
        self.passwordLineEdit.setFixedHeight(36)
        self.passwordLineEdit.setPlaceholderText(self.tr("Enter your password"))

        self.loginButton = QPushButton(self.tr("Login"))
        self.loginButton.setFixedHeight(36)

        loginLayout = QVBoxLayout()
        loginLayout.addSpacing(20)
        loginLayout.addWidget(self.userLineEdit)
        loginLayout.addWidget(self.passwordLineEdit)
        loginLayout.addWidget(self.loginButton)
        loginLayout.addStretch()
        loginLayout.setSpacing(10)
        loginLayout.setContentsMargins(30, 0, 30, 30)
        self.loginFrame.setLayout(loginLayout)

        loginBgLayout = QVBoxLayout()
        loginBgLayout.addWidget(self.loginFrame)
        loginBgLayout.setContentsMargins(20, 0, 20, 180)
        self.loginBgFrame.setLayout(loginBgLayout)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.loginBgFrame)
        mainLayout.setContentsMargins(180, 40, 180, 80)
        self.setLayout(mainLayout)
        self.setStyleSheet(self.style)

        # self.userLabel = QLabel(self.userLineEdit)
        # self.userLabel.setObjectName("userLabel")
        # # self.userPixmap = QPixmap(":/icons/light/appbar.user.tie.png")
        # self.userLabel.setFixedSize(30, 30)
        # self.userLabel.move(295, 3)

        # self.passwordLabel = QLabel(self.passwordLineEdit)
        # self.passwordLabel.setObjectName("passwordLabel")
        # # self.passwordPixmap = QPixmap(":/icons/light/appbar.lock.png")
        # self.passwordLabel.setFixedSize(30, 30)
        # self.passwordLabel.move(295, 3)

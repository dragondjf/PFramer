#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from qframer.qt.QtCore import *
from qframer.qt.QtGui import *
from qframer import views, collectView
from qframer.animationwidget import FAnimationFrame

from dataBase import login_DB


class LoginPage(FAnimationFrame):

    languageList = ["EN-US", "ZH-CN"]
    ttsTypeList = ["TEXT", "SAPI_PHONEMES", "LHPLUS_PHONEMES", "PRE_RECORDED", "SILENCE"]

    style = '''
        QFrame{
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 82, 112, 255), stop:0.5 rgba(0, 211, 197, 255), stop:1 rgba(0, 82, 112, 255));
        }
    '''

    def __init__(self, parent=None):
        super(LoginPage, self).__init__(parent)
        self.initUI()

    def initSetData(self):
        initData = login_DB.loginDict
        print(initData, "----")

    def initUI(self):
        # --------------appname----appid----------------

        self.appName = QLabel(self)
        self.appName.setText(self.tr("App name:"))

        self.appNameLineEdit = QLineEdit(self)

        self.appID = QLabel(self)
        self.appID.setText(self.tr("App ID:"))

        self.appIDLineEdit = QLineEdit(self)

        # ----------app synonym 1 and 2------------------------

        self.appSynonym1 = QLabel(self)
        self.appSynonym1.setText(self.tr("App synonym 1:"))

        self.appSynonym1LineEdit = QLineEdit(self)

        self.appSynonym2 = QLabel(self)
        self.appSynonym2.setText(self.tr("App synonym 2:"))

        self.appSynonym2LineEdit = QLineEdit(self)

        # ----------ip---port------------------------

        self.ip = QLabel(self)
        self.ip.setText(self.tr("IP:"))

        self.ipLineEdit = QLineEdit(self)

        self.port = QLabel(self)
        self.port.setText(self.tr("Port:"))

        self.portLineEdit = QLineEdit(self)

        # ----------Language base and HMI----------------

        self.language = QLabel(self)
        self.language.setText(self.tr("Language:"))

        self.languageComboBox = QComboBox()
        for item in self.languageList:
            self.languageComboBox.addItem(item)

        self.languageHMI = QLabel(self)
        self.languageHMI.setText(self.tr("HMI language:"))

        self.languageHMIComboBox = QComboBox()
        for item in self.languageList:
            self.languageHMIComboBox.addItem(item)

        # ----------Media-----Auto reconnect----------

        self.mediaCheckbox = QCheckBox(self.tr("Media"))

        self.autoReconnectCheckbox = QCheckBox(self.tr("Auto reconnect"))

        # ----------TTS-----TTS text type reconnect----------

        self.ttsText = QLabel(self)
        self.ttsText.setText(self.tr("TTS Text:"))

        self.ttsTextLineEdit = QLineEdit(self)

        self.ttsTextType = QLabel(self)
        self.ttsTextType.setText(self.tr("TTS Text Type:"))

        self.ttsTextComboBox = QComboBox()
        for item in self.ttsTypeList:
            self.ttsTextComboBox.addItem(item)

        # ----------ESN---Set app icon-----------------

        self.esn = QLabel(self)
        self.esn.setText(self.tr("ESN:"))

        self.esnLineEdit = QLineEdit(self)

        self.setIconCheckbox = QCheckBox(self.tr("Set app icon after registration"))

        # -----------Button connect and set Init------

        self.connectButton = QPushButton(self.tr("Connect"))
        self.setButton =  QPushButton(self.tr("InitConfig"))

        # -----------------Layout------------------

        mainlayout = QGridLayout()
        mainlayout.addWidget(self.appName, 0, 0)
        mainlayout.addWidget(self.appNameLineEdit, 0, 1)
        mainlayout.addWidget(self.appID, 0, 2)
        mainlayout.addWidget(self.appIDLineEdit, 0, 3)

        mainlayout.addWidget(self.appSynonym1, 1, 0)
        mainlayout.addWidget(self.appSynonym1LineEdit, 1, 1)
        mainlayout.addWidget(self.appSynonym2, 1, 2)
        mainlayout.addWidget(self.appSynonym2LineEdit, 1, 3)

        mainlayout.addWidget(self.ip, 3, 0)
        mainlayout.addWidget(self.ipLineEdit, 3, 1)
        mainlayout.addWidget(self.port, 3, 2)
        mainlayout.addWidget(self.portLineEdit, 3, 3)

        mainlayout.addWidget(self.language, 4, 0)
        mainlayout.addWidget(self.languageComboBox, 4, 1)
        mainlayout.addWidget(self.languageHMI, 4, 2)
        mainlayout.addWidget(self.languageHMIComboBox, 4, 3)

        mainlayout.addWidget(self.mediaCheckbox, 5, 1)
        mainlayout.addWidget(self.autoReconnectCheckbox, 5, 3)

        mainlayout.addWidget(self.ttsText, 6, 0)
        mainlayout.addWidget(self.ttsTextLineEdit, 6, 1)
        mainlayout.addWidget(self.ttsTextType, 6, 2)
        mainlayout.addWidget(self.ttsTextComboBox, 6, 3)

        mainlayout.addWidget(self.esn, 7, 0)
        mainlayout.addWidget(self.esnLineEdit, 7, 1)
        mainlayout.addWidget(self.setIconCheckbox, 7, 3)

        okLayout = QHBoxLayout()
        okLayout.addStretch()
        okLayout.addWidget(self.connectButton)
        okLayout.addSpacing(75)
        okLayout.addWidget(self.setButton)
        okLayout.addSpacing(80)

        mainlayout.addLayout(okLayout, 8, 0, 1, 4)

        self.setLayout(mainlayout)

        # self.setStyleSheet(self.style)

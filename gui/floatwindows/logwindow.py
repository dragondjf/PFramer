#!/usr/bin/python
# -*- coding: utf-8 -*-
#=============================================================================
# Copyright (c) 2013, Ford Motor Company All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer. Redistributions in binary
# form must reproduce the above copyright notice, this list of conditions and
# the following disclaimer in the documentation and/or other materials provided
# with the distribution. Neither the name of the Ford Motor Company nor the
# names of its contributors may be used to endorse or promote products derived
# from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#=============================================================================


import sys
import os
import logging
from log import logger
from qframer.qt.QtCore import *
from qframer.qt.QtGui import *
import json
from dataBase import signal_DB
import time
# from jsonTree import JsonTreeWidget


class LogWindow(QTableWidget):
    #render the log window
    def __init__(self, parent=None, rows=0, cloumns=4):
        super(LogWindow, self).__init__(rows, cloumns, parent)
        self.parent = parent
        self.setEditTriggers(self.NoEditTriggers)
        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.SingleSelection)
        self.setFocusPolicy(Qt.NoFocus)
        self.verticalHeader().setVisible(False)

        headerview = QHeaderView(Qt.Horizontal, self)
        self.setHorizontalHeader(headerview)

        self.cellDoubleClicked.connect(self.showDetail)

        self.setHorizontalHeaderLabels(['Corr ID', 'Name', 'Type', 'Data'])
        self.setColumnWidth(0, 60)
        self.setColumnWidth(1, 170)
        self.setColumnWidth(2, 80)
        self.setColumnWidth(3, 470)

        signal_DB.su_logsin.connect(self.addLog)

        t = {u'function': u'RegisterAppInterface', u'type': u'request', u'correlation_id': 65529, u'data': {u'vrSynonyms': [u'djf'], u'appName': u'djf', u'languageDesired': u'EN-US', u'syncMsgVersion': {u'majorVersion': 1, u'minorVersion': 0}, u'ttsName': [{u'text': u'Sync Proxy Tester', u'type': u'TEXT'}], u'isMediaApplication': True, u'appID': u'584421907', u'hmiDisplayLanguageDesired': u'EN-US', u'ngnMediaScreenAppName': u'djf'}, u'app_id': 65538}
        t = {u'function': u'RegisterAppInterface', u'type': u'request', u'correlation_id': 65529, u'data': {u'vrSynonyms': [u'djf']}}
        t = {"function" : "Speak","data" : {"ttsChunks" : [{"text" : "huan1ying2使用百度地图 , 请在手机端打开百度地图","type" : "TEXT",'a':[1,2,3,4]}]},"correlation_id" : 6,"type" : "request"}

        for i in xrange(20):
            self.addLog(t)

        self.column3_x = 0
        for i in xrange(3):
            self.column3_x +=  self.columnWidth(i)

        # self.installEventFilter(self)
        self.horizontalHeader().setEnabled(False)

    def clearAllRows(self):
        for i in xrange(self.rowCount()):
            self.removeRow(0)

    # add log for request/reponse/notification message
    def addLog(self, params):
        message = []
        try:
            if "correlation_id" in params:
                message.append(str(params["correlation_id"]))
            else:
                message.append("")
            message.append(params["function"])
            message.append(params["type"])
            message.append(json.dumps(params["data"]))
            color = "white"
            if params["type"] == "Response":
                if params["data"]["success"] is False:
                    color = "red"
                else:
                    color = "yellow"
            self.addItem(message, color)
        except:
            pass

    # show message for debug info
    def showMessage(self, message):
        self.addItem(['Debug', 'Info', message], color="gray")

    def addItem(self, message, color="white"):
        request = json.loads(message[3])
        message[3] = json.dumps(request, ensure_ascii=False)
        self.insertRow(0)
        for col in xrange(self.columnCount()):
            if col == 0:
                if message[col] == 'None':
                    message[col] = ""
            newItem = QTableWidgetItem(message[col])

            if col in [0, 1, 2]:
                newItem.setTextAlignment(Qt.AlignCenter)
            # if col < 2:
            #     newItem.setFlags(0)
            if u'response' in message:
                messageDict = json.loads(message[3])
                if u'resultCode' in messageDict and  messageDict[u'success'] is True:
                    newItem.setForeground(QBrush(QColor("#22DDB8")))
                elif u'resultCode' in messageDict and messageDict[u'success'] is False:
                    newItem.setForeground(QBrush(QColor("#FF6699")))
            elif message[2] == u"notification":
                newItem.setForeground(QBrush(QColor("yellow")))
            else:
                newItem.setForeground(QBrush(QColor("black")))
            self.setItem(0, col, newItem)        # request = json.loads(message[2])

    def showDetail(self, row, column):
        if column == 3:
            data = json.loads(self.item(row, column).text())
            jsondata = json.dumps(data, ensure_ascii=False, indent=4)
            tabledetail = TableItemDetailWidget(jsondata, row, 3, self)
            tabledetail.showDetail()

    def resizeEvent(self, event):
        if event.size().width() > 568:
            logwidth = event.size().width() - self.column3_x
            self.setColumnWidth(3, logwidth)
        super(LogWindow, self).resizeEvent(event)


def fommat(d):
    for key in d:
        if isinstance(d[key], list):
            d.update({key: list2dict(d[key])})
        elif isinstance(d[key], dict):
            fommat(d[key])
    return d


def list2dict(l):
    l = [(l.index(i), i) for i in l]
    return dict(l)


class TableItemDetailWidget(QFrame):

    style = '''
        QFrame#TableItemDetailWidget{
            color: white;
            background-color:rgb(47, 54, 65);
            font-size: 12px;
            font-family: "Verdana";
            border: none;

        }
        QLabel#titlebar{
            background-image: url(gui/skin/PNG/bg_dock.png);
            border: none;
        }

    '''

    def __init__(self, jsondata, row, column, parent=None):
        super(TableItemDetailWidget, self).__init__(parent)
        self.parent = parent
        self.startX = 0
        self.row = row
        for i in xrange(column):
            self.startX += self.parent.columnWidth(i)

        self.setObjectName("TableItemDetailWidget")
        self.setWindowFlags(Qt.Popup)
        self.setFixedSize(self.parent.columnWidth(3), 220)
        detailShow = DetailShow(jsondata, self)
        detailShow.setFixedSize(self.width(), 200)

        self.titleLabel =QLabel("Data", self)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setObjectName("titlebar")
        self.titleLabel.setFixedSize(self.parent.columnWidth(3), 20)
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(self.titleLabel)
        mainlayout.addWidget(detailShow)
        mainlayout.setSpacing(0)
        mainlayout.setContentsMargins(0,0,0,0)
        self.setLayout(mainlayout)
        self.installEventFilter(self)

        self.setStyleSheet(self.style)

        self.show()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            self.close()
            return  True
        else:
            return super(TableItemDetailWidget, self).eventFilter(obj, event)

    def showDetail(self):
        self.jsonshowPosX = self.parent.mapToGlobal(QPoint(self.startX, 0)).x()
        self.jsonshowPosY = self.parent.mapToGlobal(QPoint(self.startX, self.parent.rowViewportPosition(self.row))).y()\
         - self.height()  + self.parent.horizontalHeader().height()
        self.move(self.jsonshowPosX, self.jsonshowPosY)
        super(TableItemDetailWidget, self).show()

    def resizeEvent(self, event):
        self.titleLabel.setFixedWidth(self.width())


class DetailShow(QTextEdit):
    style = '''
        QTextEdit{
            color: white;
            background-color:rgb(47, 54, 65);
            font-size: 12px;
            font-family: "Verdana";
            border: none;
        }
        QScrollBar:vertical {
            border: 1px solid #252A31;
            width: 10px;
            margin: 15px 0 15px 0;
            background: #31394E;
        }
        QScrollBar::handle:vertical {
            background: #5B677A;
            min-height: 20px;
        }

        QScrollBar::add-line:vertical {
            background: #252A31;
            height: 20px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }

        QScrollBar::sub-line:vertical {
            background: #252A31;
            height: 20px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }

        /*QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
            width: 3px;
            height: 3px;
            background: #31394E;
        }*/

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }


        QScrollBar:horizontal {
            border: 1px solid #252A31;
            background: #5B677A;
            height: 10px;
            margin: 0px 15px 0 15px;
        }
        QScrollBar::handle:horizontal {
            background: #31394E;
            min-width: 20px;
        }
        QScrollBar::add-line:horizontal {
            background: #252A31;
            width: 20px;
            subcontrol-position: right;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:horizontal {
            background: #252A31;
            width: 20px;
            subcontrol-position: left;
            subcontrol-origin: margin;
        }
        /*QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
            width: 3px;
            height: 3px;
            background: #31394E;
        }*/
        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
            background: none;
        }
    '''
    def __init__(self, jsondata, parent=None):
        super(DetailShow, self).__init__(parent)
        self.parent = parent
        self.setText(jsondata)
        self.setReadOnly(True)
        self.setStyleSheet(self.style)
        self.installEventFilter(self)
        self.setFocus()

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            pass
        else:
            super(DetailShow, self).mousePressEvent(event)

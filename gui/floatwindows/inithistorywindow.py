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
from database import signal_DB
import time

from qframer import FDragRowsTableWidget


class InitHistoryWindow(FDragRowsTableWidget):
    # render the log window

    def __init__(self, rows=0, cloumns=2, parent=None):
        super(InitHistoryWindow, self).__init__(rows, cloumns, parent)
        self.parent = parent
        self.setHorizontalHeaderLabels(['Type', 'Data'])
        self.setColumnWidth(0, 120)
        self.setColumnWidth(1, 320)

        self.initData()
        self.initContextMenu()
        self.initConnect()

    def initData(self):
        self.index = None
        self.editRow = None

    def initConnect(self):
        self.cellDoubleClicked.connect(self.updateItem)
        signal_DB.uu_initAdd.connect(self.addItem)
        signal_DB.uu_initAddBatch.connect(self.addItems)

    def clearAllRows(self):
        for i in xrange(self.rowCount()):
            self.removeRow(0)

    def addItem(self, message, color="white"):
        self.insertRow(0)
        for col in xrange(self.columnCount()):
            if col == 0:
                newItem = QTableWidgetItem(message['type'])
            else:
                data = json.dumps(message['data'])
                newItem = QTableWidgetItem(data)
            newItem.setTextAlignment(Qt.AlignCenter)
            newItem.setForeground(QBrush(QColor(color)))
            self.setItem(0, col, newItem)

    def addItems(self, rpcs):
        import copy
        orderRpcs = copy.deepcopy(rpcs)
        orderRpcs.reverse()
        for m in orderRpcs:
            self.addItem(m)

    def getRPCs(self):
        data = []
        for row in range(self.rowCount()):
            rpc = self.getDataFromRow(row)
            data.append(rpc)
        return data

    def getDataFromRow(self, row):
        rpc = {}
        for col in range(self.columnCount()):
            item = self.item(row, col)
            if col == 0:
                rpcType = item.text()
                rpc['type'] = rpcType
            elif col == 1:
                rpcData = item.text()
                rpc['data'] = json.loads(rpcData)
        return rpc

    def initContextMenu(self):
        self.menu = QMenu()
        self.editIcon = QIcon(":/icons/dark/appbar.edit.png")
        self.deleteIcon = QIcon(":/icons/dark/appbar.delete.png")
        self.editAction = QAction(self.editIcon, 'Edit', self)
        self.deleteAction = QAction(self.deleteIcon, 'Delete', self)
        self.menu.addAction(self.editAction)
        self.menu.addAction(self.deleteAction)

        self.editAction.triggered.connect(self.editItem)
        self.deleteAction.triggered.connect(self.deleteItem)

    def contextMenuEvent(self, event):
        self.index = self.indexAt(event.pos())
        self.menu.popup(QCursor.pos())

    def updateItem(self, row, col):
        rpc = self.getDataFromRow(row)
        print(rpc)
        signal_DB.uu_initEdit.emit(rpc)

    def editItem(self):
        if self.index is not None:
            self.updateItem(self.index.row(), self.index.column())

    def deleteItem(self):
        if self.index is not None:
            self.removeRow(self.index.row())

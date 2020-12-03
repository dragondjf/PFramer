#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from qframer import FDragRowsTableWidget
from database import signal_DB


class InitHistoryWindow(FDragRowsTableWidget):
    # render the log window

    col_1_width = 120
    col_2_width = 320

    def __init__(self, rows=0, cloumns=2, parent=None):
        super(InitHistoryWindow, self).__init__(rows, cloumns, parent)
        self.parent = parent
        self.setHorizontalHeaderLabels(['Type', 'Data'])
        self.setColumnWidth(0, self.col_1_width)
        self.setColumnWidth(1, self.col_2_width)

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
        for i in range(self.rowCount()):
            self.removeRow(0)

    def addItem(self, message, color="white"):
        self.insertRow(0)
        for col in range(self.columnCount()):
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
        signal_DB.uu_initEdit.emit(rpc)

    def editItem(self):
        if self.index is not None:
            self.updateItem(self.index.row(), self.index.column())

    def deleteItem(self):
        if self.index is not None:
            self.removeRow(self.index.row())

    def resizeEvent(self, event):
        self.setColumnWidth(1, self.width() - self.col_1_width
                            - self.verticalScrollBar().width())

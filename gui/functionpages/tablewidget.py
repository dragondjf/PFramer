#!/usr/bin/python
# -*- coding: utf-8 -*-

from qframer.qt.QtCore import *
from qframer.qt.QtGui import *



class TablePage(QTableWidget):

    style = '''
        QTableWidget#DTableWidget{
        border: none;
        color: white;
        background-color: transparent;
        selection-color: transparent;
        selection-background-color:transparent;
    }

    QTableWidget:disabled{
        border: none;
        background-color: gray;
    }
    '''

    viewRowChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super(TablePage, self).__init__(parent)
        self.setObjectName("DTableWidget")
        self.setShowGrid(True)
        self.horizontalHeader().hide()
        self.verticalHeader().hide()
        self.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.SelectionMode(QAbstractItemView.NoSelection)
        self.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFrameShape(QFrame.NoFrame)
        self.setMouseTracking(True)
        
        self.setColumnCount(10)
        self.setRowCount(50)

        for i in range(self.rowCount()):
           self.setRowHeight(i, 100)

        self.setSpan(0, 0, 1, self.columnCount())

        self.setSpan(4, 0, 1, self.columnCount())


        self.setSpan(8, 0, 1, self.columnCount())


        self.setSpan(10, 0, 1, self.columnCount())

        self.setStyleSheet(self.style)

        self.initConnect()

        self.scrollToRow(3)
    
    def initConnect(self):
        self.verticalScrollBar().valueChanged.connect(self.changeSilderValue)

    def changeSilderValue(self, value):
        self.viewRowChanged.emit(value)
        print value

    def scrollToRow(self, row):
        self.verticalScrollBar().setValue(row)

    def wheelEvent(self, event):
        value = self.verticalScrollBar().value()
        miniimun = self.verticalScrollBar().minimum()
        maximum = self.verticalScrollBar().maximum()

        if event.angleDelta().y() > 0:
            if value >= miniimun:
                self.verticalScrollBar().setValue(value - 1)
        else:
            if value < maximum:
                self.verticalScrollBar().setValue(value + 1)

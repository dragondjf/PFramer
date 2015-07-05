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

    def __init__(self, parent=None):
        super(TablePage, self).__init__(parent)
        self.setObjectName("DTableWidget")
        self.setShowGrid(False)
        self.horizontalHeader().hide()
        self.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.SelectionMode(QAbstractItemView.NoSelection)
        self.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFrameShape(QFrame.NoFrame)
        self.setMouseTracking(True)
        self.verticalScrollBar().hide()
        self.setColumnCount(10)
        self.setRowCount(50)

        for i in range(self.rowCount()):
           self.setRowHeight(i, 100)

        self.setSpan(0, 0, 1, self.columnCount())

        self.setSpan(4, 0, 1, self.columnCount())


        self.setSpan(8, 0, 1, self.columnCount())


        self.setSpan(10, 0, 1, self.columnCount())

        # self.scrollTo(10)
        self.setCurrentCell(20, 0)

        self.setStyleSheet(self.style)

        self.initConnect()

    
    def initConnect(self):
        self.cellEntered.connect(self.changeHover)

    def changeHover(self, row, column):
        print(row, column)



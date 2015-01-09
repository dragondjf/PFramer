#!/usr/bin/python
# -*- coding: utf-8 -*-

from qframer.qt.QtCore import *
from qframer.qt.QtGui import *


class HistoryWindow(QTableWidget):
    # render the log window

    def __init__(self, parent=None, rows=0, cloumns=4):
        super(HistoryWindow, self).__init__(rows, cloumns, parent)
        self.parent = parent
        self.setEditTriggers(self.NoEditTriggers)
        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.SingleSelection)
        self.setFocusPolicy(Qt.NoFocus)
        self.verticalHeader().setVisible(False)

        headerview = QHeaderView(Qt.Horizontal, self)
        self.setHorizontalHeader(headerview)

        # self.cellDoubleClicked.connect(self.showDetail)

        self.setHorizontalHeaderLabels(['Corr ID', 'Name', 'Type', 'Data'])
        self.setColumnWidth(0, 60)
        self.setColumnWidth(1, 170)
        self.setColumnWidth(2, 80)
        self.setColumnWidth(3, 470)

        self.column3_x = 0
        for i in range(3):
            self.column3_x += self.columnWidth(i)

    def clearAllRows(self):
        for i in range(self.rowCount()):
            self.removeRow(0)

    def resizeEvent(self, event):
        if event.size().width() > 568:
            logwidth = event.size().width() - self.column3_x
            self.setColumnWidth(3, logwidth)
        super(HistoryWindow, self).resizeEvent(event)

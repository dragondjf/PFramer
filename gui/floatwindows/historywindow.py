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


class HistoryWindow(QTableWidget):
    #render the log window
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
            self.column3_x +=  self.columnWidth(i)

    def clearAllRows(self):
        for i in range(self.rowCount()):
            self.removeRow(0)

    def resizeEvent(self, event):
        if event.size().width() > 568:
            logwidth = event.size().width() - self.column3_x
            self.setColumnWidth(3, logwidth)
        super(HistoryWindow, self).resizeEvent(event)


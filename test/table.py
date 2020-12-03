#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class LabelWidget(QFrame):

    def __init__(self, parent=None):
        super(LabelWidget, self).__init__(parent)
        self.setStyleSheet("background-color: green")

    def mousePressEvent(self,event):
        print("LabelWidget mousePressEvent")
        super(LabelWidget, self).mousePressEvent(event)

class TextEdit(QTextEdit):
    
    def __init__(self, parent=None):
        super(TextEdit, self).__init__(parent)
        self.setStyleSheet("background-color: red")

    def mousePressEvent(self,event):
        print("TextEdit mousePressEvent")
        super(TextEdit, self).mousePressEvent(event)


class MainWindow(QTableWidget):
    """docstring for MainWindow"""
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setRowCount(10)
        self.setColumnCount(10)
        for i in xrange(self.rowCount()):
            self.setRowHeight(i, 50)
        for i in xrange(self.columnCount()):
            self.setColumnWidth(i, 50)

        self.cellClicked.connect(self.handleCellClicked)
        self.cellPressed.connect(self.handleCellPressed)
        self.itemPressed.connect(self.handleItemPressed)
        self.itemClicked.connect(self.handleItemClicked)

        item = QTableWidgetItem("item")
        self.setItem(0, 0, item)

        label = QLabel("QLabel");
        self.setCellWidget(0, 1, label)

        edit = QTextEdit("QTextEdit");
        edit.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        # edit.setAttribute(Qt.WA_NoMousePropagation, True)
        edit.setReadOnly(True)
        edit.setFocusPolicy(Qt.NoFocus)
        self.setCellWidget(0, 2, edit)

        labelWidget = LabelWidget()
        self.setCellWidget(0, 3, labelWidget)

        textWidget = TextEdit()
        textWidget.setText("sddddddd")
        textWidget.setFocusPolicy(Qt.NoFocus)
        textWidget.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        textWidget.setReadOnly(True)
        self.setCellWidget(0, 4, textWidget)

        buttonWidget = QPushButton("button")
        self.setCellWidget(0, 5, buttonWidget)

        for i in range(6):
            item = QTableWidgetItem("item%d"%i)
            self.setItem(0, i, item)


    def initUI(self):
        pass

    def handleCellClicked(self, row, column):
        print("handleCellClicked", row, column)

    def handleCellPressed(self, row, column):
        print("handleCellPressed", row, column)

    def handleItemClicked(self, item):
        print("handleItemClicked", item)

    def handleItemPressed(self, item):
        print("handleItemPressed", item)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())

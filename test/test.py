#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
# from PySide2.QtWidgets import *


class MainWindow(QFrame):

    style = '''
        QFrame{
            border-image: url(bear.jpg);
        }
    '''

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_QuitOnClose, True)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        # self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setStyleSheet(self.style)
        # self.setTransBackground(True)
        self.resize(800, 600)

    @pyqtSlot(bool)
    def setTransBackground(self, transBackground):
        palette = self.palette()
        if transBackground:
            palette.setBrush(QPalette.Base, Qt.transparent)
        else:
            palette.setBrush(QPalette.Base, Qt.white)
        self.setPalette(palette)

    def moveCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.setFocus()
        # 鼠标点击事件
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - \
                self.frameGeometry().topLeft()
            event.accept()

    def mouseReleaseEvent(self, event):
        # 鼠标释放事件
        if hasattr(self, "dragPosition"):
            del self.dragPosition

    def mouseMoveEvent(self, event):        
        if hasattr(self, "dragPosition"):
            if event.buttons() == Qt.LeftButton:
                self.move(event.globalPos() - self.dragPosition)
                event.accept()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())

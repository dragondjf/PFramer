#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.pardir)
from qframer.qt.QtCore import *
from qframer.qt.QtGui import *
from qframer.qt import QtCore

print('using %s(%s)' % (os.environ['QT_API'], QtCore.__version__))

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setMaximumSize(QDesktopWidget().availableGeometry().size())
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.CustomizeWindowHint)  # 无边框， 带系统菜单， 可以最小化
        self.setMaximumSize(QDesktopWidget().availableGeometry().size())

    def swithMaxNormal(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_F11:
            self.swithMaxNormal()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    styleoptions = {
        'title': u'退出设置',
        'windowicon': "../skin/images/ov-orange-green.png",
        'minsize': (400, 300),
        'size': (400, 300),
        'logo_title': u'dssssssss',
        'logo_img_url': "../skin/images/ov-orange-green.png"
    }
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())

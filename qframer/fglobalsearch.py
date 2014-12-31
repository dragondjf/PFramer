#!/usr/bin/python
# -*- coding: utf-8 -*-

from .qt.QtCore import *
from .qt.QtGui import *


class FGlobalSearchWidget(QFrame):

    style = '''
        QFrame#FGlobalSearchWidget{
            border: 10px solid rgb(40, 47, 63);
            background-color: rgb(40, 47, 63);
        }
        QLineEdit#search{
            border: 2px solid rgb(69, 187, 217);
            font: 30px;
            color: black;
        }
    '''

    def __init__(self, parent=None):
        super(FGlobalSearchWidget, self).__init__(parent)
        self.parent = parent
        self.setObjectName("FGlobalSearchWidget")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.ToolTip)
        self.initData()
        self.initUI()
        self._initShowAnimation()
        self._initHideAnimation()

    def initData(self):
        self._currentPos = QPoint(0, 0)

    def initUI(self):
        self.setFixedSize(600, 60)
        self.searchEdit = QLineEdit(self)
        self.searchEdit.setObjectName("search")
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.searchEdit)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)

        desktopWidth = QDesktopWidget().availableGeometry().width()
        self.move((desktopWidth - self.width())/2, 50)

        self.setStyleSheet(self.style)

    def _initShowAnimation(self):
        self.showanimation = QPropertyAnimation(self, 'windowOpacity')
        self.showanimation.setStartValue(0)
        self.showanimation.setEndValue(1)
        self.showanimation.setDuration(1000)
        self.showanimation.setEasingCurve(QEasingCurve.OutCubic)

    def _initHideAnimation(self):
        self.hideanimation = QPropertyAnimation(self, 'windowOpacity')
        self.hideanimation.setStartValue(1)
        self.hideanimation.setEndValue(0)
        self.hideanimation.setDuration(1000)
        self.hideanimation.setEasingCurve(QEasingCurve.OutCubic)
        self.hideanimation.finished.connect(self.hide)

    def animationShow(self):
        self.show()
        self.showanimation.start()

    def animationHide(self):
        self.hideanimation.start()

    def mousePressEvent(self, event):
        # 按住左键可以托动窗口，按下右键关闭程序
        if event.button() == Qt.LeftButton:
            self._currentPos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
        elif event.button() == Qt.RightButton:
            if self._contextMenu:
                self._contextMenu.exec_(QCursor.pos())

    def mouseDoubleClickEvent(self, event):
        self.animationHide()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self._currentPos)
            event.accept()

    def leaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)

    def enterEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

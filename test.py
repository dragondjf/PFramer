# !sr/bin/python
# -*- coding:utf-8 -*-

import sys
from qframer.qt import QtGui
from qframer.qt import QtCore


class ThFrame(QtGui.QFrame):

    def __init__(self, parent=None, windowFlags=QtCore.Qt.Widget):
        super(ThFrame, self).__init__(parent, windowFlags)
        self.initData()
        self.initUI()
        # self.initConnect()

    def initData(self):
        '''dragDirection:0-left,1-right,2-top,3-bottom,4-topleft,5-topright,6-bottomleft,7-bottomright,8-normal
        '''
        self.resizeFrameFlag = True  # 缩放窗口大小标志
        self.dragMoveFrameFlag = True  # 拖动窗口位置
        self.leftMousePress = False
        self.dragDirection = 8
        self.showMaximumFlag = False  # 最大化显示标志

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowSystemMenuHint |
                            QtCore.Qt.WindowMinimizeButtonHint)  # 无边框， 带系统菜单， 可以最小化)

        self.centralWidget = QtGui.QFrame()  # QtGui.QLabel('centralWidget')
        self.centralWidget.setMouseTracking(True)

        self.setMouseTracking(True)
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.centralWidget)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)
        self.rectFrame = self.geometry()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def mousePressEvent(self, e):
        if QtCore.Qt.LeftButton == e.button():
            self.leftMousePress = True
            self.globalStartPosition = e.globalPos()

    def mouseMoveEvent(self, e):
        
        self.dragDirection = self.getDragDirection(
        e.globalX(), e.globalY())
        self.setCursorStyle(self.dragDirection)
        self.resizeFrame(e.globalX(), e.globalY(), self.dragDirection)
        self.globalStartPosition = e.globalPos()

    def mouseReleaseEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.leftMousePress = False
            self.dragDirection = self.getDragDirection(
                e.globalX(), e.globalY())
            self.setCursorStyle(self.dragDirection)

    def resizeFrame(self, globalX, globalY, direction):
        # 计算偏移量
        dX = globalX - self.globalStartPosition.x()
        dY = globalY - self.globalStartPosition.y()
        rectFrame = self.geometry()
        print(dX, dY)
        # 计算新窗口位置
        '''dragDirection:0-left,1-right,2-top,3-bottom,4-topleft,5-topright,6-bottomleft,7-bottomright,8-normal
		'''
        if 0 == direction:
            rectFrame.setLeft(rectFrame.left() + dX)
        elif 1 == direction:
            rectFrame.setRight(rectFrame.right() + dX)
        elif 2 == direction:
            rectFrame.setTop(rectFrame.top() + dY)
        elif 3 == direction:
            rectFrame.setBottom(rectFrame.bottom() + dY)
        elif 4 == direction:
            rectFrame.setLeft(rectFrame.left() + dX)
            rectFrame.setTop(rectFrame.top() + dY)
        elif 5 == direction:
            rectFrame.setRight(rectFrame.right() + dX)
            rectFrame.setTop(rectFrame.top() + dY)
        elif 6 == direction:
            rectFrame.setLeft(rectFrame.left() + dX)
            rectFrame.setBottom(rectFrame.bottom() + dY)
        elif 7 == direction:
            rectFrame.setRight(rectFrame.right() + dX)
            rectFrame.setBottom(rectFrame.bottom() + dY)

        # if rectFrame.width() < self.minimumWidth() or rectFrame.height() < self.minimumHeight():
        #     return

        self.setGeometry(rectFrame)

    def getDragDirection(self, globalX, globalY):
        '''dragDirection:0-left,1-right,2-top,3-bottom,4-topleft,5-topright,6-bottomleft,7-bottomright,8-normal
        '''
        rectFrame = self.geometry()
        left = rectFrame.left()
        right = rectFrame.right()
        top = rectFrame.top()
        bottom = rectFrame.bottom()
        space = 3

        if left <= globalX and globalX <= left + space and top <= globalY and globalY <= top + space:
            return 4

        if left <= globalX and globalX <= left + space and top + space < globalY and globalY < bottom - space:
            return 0

        if left <= globalX and globalX <= left + space and bottom - space <= globalY and globalY <= bottom:
            return 6

        if left + space < globalX and globalX < right - space and top <= globalY and globalY <= top + space:
            return 2

        if left + space < globalX and globalX < right - space and bottom - space <= globalY and globalY <= bottom:
            return 3

        if right - space <= globalX and globalX <= right and top <= globalY and globalY <= top + space:
            return 5

        if right - space <= globalX and globalX <= right and top + space < globalY and globalY < bottom - space:
            return 1

        if right - space <= globalX and globalX <= right and bottom - space <= globalY and globalY <= bottom:
            return 7
        return 8

    def setCursorStyle(self, direction):
        '''dragDirection:0-left,1-right,2-top,3-bottom,4-topleft,5-topright,6-bottomleft,7-bottomright,8-normal
        '''
        if 0 == direction or 1 == direction:
            self.setCursor(QtCore.Qt.SizeHorCursor)
        elif 2 == direction or 3 == direction:
            self.setCursor(QtCore.Qt.SizeVerCursor)
        elif 4 == direction or 7 == direction:
            self.setCursor(QtCore.Qt.SizeFDiagCursor)
        elif 5 == direction or 6 == direction:
            self.setCursor(QtCore.Qt.SizeBDiagCursor)
        else:
            self.setCursor(QtCore.Qt.ArrowCursor)


def main():
    import platform
    if sys.platform == "linux2":
        QtGui.QApplication.addLibraryPath(
            '/usr/lib/%s-linux-gnu/qt5/plugins/' % platform.machine())
    app = QtGui.QApplication(sys.argv)
    window = ThFrame()
    window.setGeometry(100, 100, 800, 600)
    window.setWindowTitle('ThFrame')
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

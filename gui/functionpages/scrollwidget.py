#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ScrollWidget(QScrollArea):


    style = '''
        QScrollArea {
            background-color: transparent;
        }

        QLabel#section1 {
            background-color: rgba(1, 1, 1, 200);
        }
        QLabel#section2 {
            background-color: rgba(10, 10, 10, 200);
        }
        QLabel#section3 {
            background-color: rgba(100, 100, 100, 200);
        }
        QLabel#section4 {
            background-color: rgba(120, 120, 120, 200);
        }
        QLabel#section5 {
            background-color: rgba(140, 140, 140, 200);
        }
        QLabel#section6 {
            background-color: rgba(160, 160, 160, 200);
        }
        QLabel#section7 {
            background-color: rgba(180, 180, 180, 200);
        }
        QLabel#section8 {
            background-color: rgba(200, 200, 200, 200);
        }
    '''


    def __init__(self, parent=None):
        super(ScrollWidget, self).__init__()
        self.parent = parent
        # self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.setWidgetResizable(True)
        self.initUI()
        # self.contentWidget.resize(self.parent.width(), 2000)

        # self.scrollContentsBy(100, 1000)

        verticalScrollBar = self.verticalScrollBar()
        # verticalScrollBar.setMinimum(0)
        # verticalScrollBar.setMaximum(100)
        # verticalScrollBar.setValue(50)



        print(verticalScrollBar.minimum())
        print(verticalScrollBar.maximum())
        print(verticalScrollBar.value())

        self.timer = QTimer()
        self.timer.timeout.connect(self.changeLabelSize)
        self.timer.start(2000)


    def initUI(self):

        self.contentWidget =  QFrame(self)
        self.contentWidget.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding))
        self.labels = []
        for i in range(1, 9):
            sectionLabel = QLabel(str(i), self)
            # sectionLabel.setFixedHeight(100)
            sectionLabel.setObjectName("section%d" % i)
            self.labels.append(sectionLabel)

        mainLayout = QVBoxLayout()
        for label in self.labels:
            mainLayout.addWidget(label)

        self.contentWidget.setLayout(mainLayout)
        self.setWidget(self.contentWidget)
        self.setStyleSheet(self.style)

        print(mainLayout.spacing())

    def changeLabelSize(self):
        print("55555555555")
        for label in self.labels:
            # label.resize(label.width(), label.height() + 100)
            rect = label.geometry()
            rect.adjust(0, rect.y() + 100, 0, 0)
            print(rect)
            label.setGeometry(rect)
        # self.viewport().update()

    def resizeEvent(self, event):
        print(event.size())
        self.contentWidget.resize(self.width(), self.contentWidget.height())

        super(ScrollWidget, self).resizeEvent(event)

    def scrollContentsBy(self, dx, dy):
        print(dx, dy, self.verticalScrollBar().value())
        super(ScrollWidget, self).scrollContentsBy(dx, dy)

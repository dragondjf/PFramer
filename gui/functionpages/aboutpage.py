#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from qframer.qt.QtCore import *
from qframer.qt.QtGui import *
from qframer import views, collectView
from qframer.animationwidget import FAnimationFrame

class AboutPage(FAnimationFrame):

    style = '''
        QFrame{
            /*background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 82, 112, 255), stop:0.5 rgba(0, 211, 197, 255), stop:1 rgba(0, 82, 112, 255));*/
            border-image: url(gui/skin/images/bear.jpg)
        }
    '''

    def __init__(self, parent=None):
        super(AboutPage, self).__init__(parent)

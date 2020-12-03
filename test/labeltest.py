#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class GrowingTextEdit(QTextEdit):

    def __init__(self, *args, **kwargs):
        super(GrowingTextEdit, self).__init__(*args, **kwargs)
        
        self.setAlignment(Qt.AlignCenter)
        self.heightMin = 0
        self.heightMax = 65000
        self.document().contentsChanged.connect(self.sizeChange)    

    def sizeChange(self):
        docHeight = self.document().size().height()
        if self.heightMin <= docHeight <= self.heightMax:
            self.setMinimumHeight(docHeight)

class ElidedLabel(QLabel):

    def __init__(self,parent=None):
        super(ElidedLabel, self).__init__(parent)
        # self.setWordWrap(True)
        self.setAlignment(Qt.AlignCenter)
        self.setFixedWidth(90)

        font = QFont("times", 24)
        self.setFont(font)

        self.fullText = ""
        self.simpleWrapText = ""
        self.fullWrapText = ""
        self.texts = []

    def elideText(self):
        width = self.width()
        texts = []
        fm = self.fontMetrics()
        i = 0
        start = 0
        for i in range(0, len(self.fullText)):
            if fm.width(self.fullText[start:i]) < width -  10:
                i = i + 1;
            else:
                texts.append(self.fullText[start:i-1])
                start = i-1

        texts.append(self.fullText[start:])
        print texts
        self.texts = texts        
        self.fullWrapText = "\n".join(texts)

        if len(texts) >= 2:
            elideText = fm.elidedText("\n".join(texts[1:]), Qt.ElideRight, width - 10)
            # print elideText.encode("utf-8")
            self.simpleWrapText = texts[0] + "\n" + elideText
        else:
            self.simpleWrapText = texts[0]

    def setFullText(self, text):
        self.fullText = text
        self.elideText()

    def showSimpleText(self, text):
        self.setFullText(text)
        self.setText(self.simpleWrapText)
        fm = self.fontMetrics()
        self.setFixedHeight(fm.lineSpacing() * 2)

    def showFullText(self, text):
        self.setFullText(text)
        self.setText(self.fullWrapText)
        # print self.texts, self.fullWrapText
        fm = self.fontMetrics()
        self.setFixedHeight(fm.lineSpacing() * len(self.texts))


class MainWindow(QFrame):

    style = '''
        QFrame{
            background-color: green;
            text-align: center, center;
        }

        QLabel{
            background-color: black;
            color: white;
            border: 1px solid black;
        }
    '''

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_QuitOnClose, True)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.initUI()
        # self.setStyleSheet(self.style)

    def initUI(self):

        self.lineEdit  = QLineEdit(self)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setText("dfdssdfd")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.textEdit = GrowingTextEdit()
        self.textEdit.resize(100, 100)
        self.simpleLabel = QLabel(self)
        self.simpleLabel.setStyleSheet(self.style)
        self.simpleLabel.setWordWrap(True)
        self.simpleLabel.setFixedWidth(200)
        self.fullLabel = ElidedLabel(self)

        mainLayout = QHBoxLayout(self)
        mainLayout.addWidget(self.textEdit)
        mainLayout.addWidget(self.lineEdit)
        mainLayout.addWidget(self.simpleLabel)
        mainLayout.addWidget(self.fullLabel)
        self.setLayout(mainLayout)
        
        self.resize(450, 500)

        self.lineEdit.textChanged.connect(self.handleTextChanged)
        self.lineEdit.setText(u'深航奖励航班班组')

    def handleTextChanged(self, text):
        
        fm = self.simpleLabel.fontMetrics()
        row =  fm.width(text) / self.simpleLabel.width() + 1
        self.simpleLabel.setFixedHeight(row * fm.height() * 2)
        self.simpleLabel.setText(text)
        print row, self.simpleLabel.height()
        self.fullLabel.showFullText(text)







if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())

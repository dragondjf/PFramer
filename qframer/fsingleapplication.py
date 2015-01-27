#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from .qt.QtCore import *
from .qt.QtGui import *
from .qt.QtNetwork import *


class QtSingleApplication(QApplication):

    messageReceived = Signal(unicode)

    def __init__(self, id, *argv):

        super(QtSingleApplication, self).__init__(*argv)
        self._id = id
        self._activationWindow = None
        self._activateOnMessage = False
        self._server = None

        # Is there another instance running?
        self._outSocket = QLocalSocket()
        self._outSocket.connectToServer(self._id)
        self._outSocket.error.connect(self.handleError)
        self._isRunning = self._outSocket.waitForConnected()

        print(self._isRunning, self._outSocket.serverName())

        if self._isRunning:
            # Yes, there is.
            self._outStream = QTextStream(self._outSocket)
            self._outStream.setCodec('UTF-8')
        else:
            # No, there isn't.
            self._outSocket = None
            self._outStream = None
            self._inSocket = None
            self._inStream = None
            self._server = QLocalServer()
            self._server.listen(self._id)
            self._server.newConnection.connect(self._onNewConnection)

    def handleError(self, msg):
        print(msg, '---')

    def server(self):
        return self._server

    def isRunning(self):
        return self._isRunning

    def id(self):
        return self._id

    def activationWindow(self):
        return self._activationWindow

    def setActivationWindow(self, activationWindow, activateOnMessage=True):
        self._activationWindow = activationWindow
        self._activateOnMessage = activateOnMessage

    def activateWindow(self):
        if not self._activationWindow:
            print("No registered ActivationWindow")
            return
        # Unfortunately this *doesn't* do much of any use, as it won't
        # bring the window to the foreground under KDE... sigh.
        self._activationWindow.setWindowState(
            self._activationWindow.windowState() & ~Qt.WindowMinimized)
        self._activationWindow.raise_()
        self._activationWindow.activateWindow()

    def sendMessage(self, msg,  msecs=5000):
        if not self._outStream:
            return False
        self._outStream << msg << '\n'
        if not self._outSocket.waitForBytesWritten(msecs):
            raise RuntimeError(
                "Bytes not written within %ss" % (msecs / 1000.))

    def _onNewConnection(self):
        if self._inSocket:
            self._inSocket.readyRead.disconnect(self._onReadyRead)
        self._inSocket = self._server.nextPendingConnection()
        if not self._inSocket:
            return
        self._inStream = QTextStream(self._inSocket)
        self._inStream.setCodec('UTF-8')
        self._inSocket.readyRead.connect(self._onReadyRead)
        print(self._activateOnMessage, '++++---')
        if self._activateOnMessage:
            self.activateWindow()

    def _onReadyRead(self):
        while True:
            msg = self._inStream.readLine()
            if not msg:
                break
            print("Message received")
            self.messageReceived.emit(msg)


class QSingleApplication(QApplication):

    def singleStart(self, mainWindow):
        self.mainWindow = mainWindow
        # Socket
        self.m_socket = QLocalSocket()
        self.m_socket.connected.connect(self.connectToExistingApp)
        self.m_socket.error.connect(self.startApplication)
        self.m_socket.connectToServer(
            self.applicationName(), QIODevice.WriteOnly)

    def connectToExistingApp(self):
        if len(sys.argv) > 1 and sys.argv[1] is not None:
            self.m_socket.write(sys.argv[1])
            self.m_socket.bytesWritten.connect(self.quit)
        else:
            QMessageBox.warning(
                None, self.tr("Already running"),
                self.tr("The program is already running."))
            # Quit application in 250 ms
            QTimer.singleShot(250, self.quit)

    def startApplication(self):
        self.m_server = QLocalServer()
        if self.m_server.listen(self.applicationName()):
            self.m_server.newConnection.connect(self.getNewConnection)
            self.mainWindow.show()
        else:
            QMessageBox.critical(
                None, self.tr("Error"), self.tr("Error listening the socket."))

    def getNewConnection(self):
        self.new_socket = self.m_server.nextPendingConnection()
        self.new_socket.readyRead.connect(self.readSocket)

    def readSocket(self):
        f = self.new_socket.readLine()
        self.mainWindow.getArgsFromOtherInstance(str(f))
        self.mainWindow.activateWindow()
        self.mainWindow.show()

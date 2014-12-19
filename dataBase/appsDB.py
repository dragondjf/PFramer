# -*- coding: utf-8 -*-
import time
import os

from appData import AppData

class AppsDB(object):
    def __init__(self, parent=None):
        self.initData()
        self.scriptTestRunning = False
        self.preTestRunning = False
        self.scriptTestRecording = False

    def initData(self):
        self.apps = {}
        self.currentApp = None
        self.currentAppID = None
        self.preAppID = None
        self.audioRecordingFilename = None

    def addApp(self, app):
        appID = app['application']['appID']
        appObject = AppData(app)
        self.apps[appID] = appObject

    def delApp(self, app):
        if app["appID"] in self.apps:
            del self.apps[app['appID']]
            if app['appID'] == self.currentAppID:
                self.currentApp = None

    def displayShow(self, show):
        if self.currentApp:
            self.currentApp.displayShow(show)
    
    def displayAlert(self, alert):
        if self.currentApp:
            self.currentApp.displayAlert(alert)

    def displayScrollMessage(self, scrollMessage):
        if self.currentApp:
            self.currentApp.displayScrollMessage(scrollMessage)

    def addCommand(self, command):
        if self.currentApp:
            self.currentApp.addCommand(command)

    def addVRCommand(self, vrcommand):
        if self.currentApp:
            self.currentApp.addVRCommand(vrcommand)

    def addSubmenu(self, submenu):
        if self.currentApp:
            self.currentApp.addSubmenu(submenu)

    def delCommand(self, command):
        if self.currentApp:
            self.currentApp.delCommand(command)

    def delVRCommand(self, vrcommand):
        if self.currentApp:
            self.currentApp.delVRCommand(vrcommand)

    def delSubmenu(self, submenu):
        if self.currentApp:
            self.currentApp.delSubmenu(submenu)

    def addSubscribeButton(self, subscribeButton):
        if self.currentApp:
            self.currentApp.addSubscribeButton(subscribeButton)

    def delSubscribeButton(self, subscribeButton):
        if self.currentApp:
            self.currentApp.delSubscribeButton(subscribeButton)

    def addChoiceSet(self, choiceSet):
        if self.currentApp:
            self.currentApp.addChoiceSet(choiceSet)

    def delChoiceSet(self, choiceSet):
        if self.currentApp:
            self.currentApp.delChoiceSet(choiceSet)

    def displayInteractionChoices(self, interactionChoices):
        if self.currentApp:
            self.currentApp.displayInteractionChoices(interactionChoices)

    def destroyAudioPerform(self):
        if self.currentApp:
            self.currentApp.destroyAudioPerform()

    def initAudoiPerform(self, audioPerform):
        if self.currentApp:
            self.currentApp.initAudoiPerform(audioPerform)

    def destroyAlert(self):
        if self.currentApp:
            self.currentApp.destroyAlert()

    def destroyScrollMessage(self):
        if self.currentApp:
            self.currentApp.destroyScrollMessage()

    def destroyInteractionChoices(self):
        if self.currentApp:
            self.currentApp.destroyInteractionChoices()

    def getApp(self):
        _apps = []
        for a in self.apps:
            _a = self.apps[a]
            _appID = a
            _appName = _a.appName
            _apps.append({"appName":_appName, "appID":_appID})
        return _apps


apps_DB = AppsDB()
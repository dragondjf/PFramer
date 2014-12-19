# -*- coding: utf-8 -*-
import json

from log import logger

class AppData(object):
    def __init__(self, app):
        self.init(app)

    def init(self, app):
        self.appID = app['application']['appID']
        self.appName = app['application']['appName']
        self.isMediaApplication = app['application']['isMediaApplication']
        self.hmiDisplayLanguageDesired = app['application']['hmiDisplayLanguageDesired']
        self.deviceName = app['application']['deviceName']
        self.icon = app['application']['icon']
        if "ngnMediaScreenAppName" in app['application']:
            self.ngnMediaScreenAppName = app['application']['ngnMediaScreenAppName']

        self.initData()

    def initData(self):
        self.commandsList = {}
        self.submenuList = []
        self.vrCommandList = {}
        self.subscribeButtonList = []
        self.interactionChoices = None
        self.choiceSets = {}
        self.show = {}
        self.alert = None
        self.scrollMessage = None

        self.newAlert = None
        self.newScrollMessage = None

        self.speak = False
        self.audioPerform = None
        self.preReportUrl = None

    def addCommand(self, command):
        if "parentID" in command['menuParams']:
            if command['menuParams']['parentID'] in self.commandsList:
                self.commandsList[command['menuParams']['parentID']].append(command)
            else:
                self.commandsList[command['menuParams']['parentID']] = [command]
        else:
            self.submenuList.append(command)
            if "None" in self.commandsList:
                self.commandsList['None'].append(command)
            else:
                self.commandsList['None'] = [command]

    def addVRCommand(self, vrcommand):
        self.vrCommandList[vrcommand['cmdID']] = vrcommand

    def addSubmenu(self, submenu):
        self.submenuList.append(submenu)

    def delCommand(self, command):
        cmdID = command['cmdID']

        for k in self.commandsList:
            comlist = self.commandsList[k]
            c = False
            for com in comlist:
                if com['cmdID'] == cmdID:
                    c = com
                    break
            if c:
                comlist.remove(c)
                break

    def delVRCommand(self, vrcommand):
        try:
            self.vrCommandList.pop(vrcommand['cmdID'])
        except Exception, e:
            logger.warning(e)
        else:
            pass
        finally:
            pass

    def delSubmenu(self, submenu):
        menuID = submenu['menuID']
        for submenu in self.submenuList:
            if "menuID" in submenu:
                if submenu['menuID'] == menuID:
                    self.submenuList.remove(submenu)
                    break
        for submenuID in self.commandsList:
            if menuID == submenuID:
                del self.commandsList[submenuID]
                break

    def addSubscribeButton(self, subscribeButton):
        self.subscribeButtonList.append(subscribeButton['buttonName'])

    def delSubscribeButton(self, subscribeButton):
        if subscribeButton['buttonName'] in self.subscribeButtonList:
            self.subscribeButtonList.remove(subscribeButton['buttonName'])

    def startSpeak(self):
        pass

    def stopSpeak(self):
        pass

    def clearData(self):
        pass

    def displayShow(self, show):
        if self.show is None:
            self.show = show
        else:
            for key in show:
                self.show[key] = show[key]

    def displayAlert(self, alert):
        if self.alert:
            self.newAlert = alert
        else:
            self.alert = alert

    def destroyAlert(self):
        if self.newAlert:
            self.alert = self.newAlert
            self.newAlert = None
        else:
            self.alert = None

    def displayScrollMessage(self, scrollMessage):
        if self.scrollMessage:
            self.newScrollMessage = scrollMessage
        else:
            self.scrollMessage = scrollMessage

    def destroyScrollMessage(self):
        if self.newScrollMessage:
            self.scrollMessage = self.newScrollMessage
            self.newScrollMessage = None
        else:
            self.scrollMessage = None

    def displayInteractionChoices(self, interactionChoices):
        self.interactionChoices = interactionChoices

    def destroyInteractionChoices(self):
        self.interactionChoices = None

    def destroyAudioPerform(self):
        self.audioPerform = None

    def initAudoiPerform(self, audioPerform):
        self.audioPerform = audioPerform

    def addChoiceSet(self, choiceSet):
        self.choiceSets[choiceSet['params']['interactionChoiceSetID']] = choiceSet['params']

    def delChoiceSet(self, choiceSet):
        if choiceSet['params']['interactionChoiceSetID'] in self.choiceSets:
            del self.choiceSets[choiceSet['params']['interactionChoiceSetID']]

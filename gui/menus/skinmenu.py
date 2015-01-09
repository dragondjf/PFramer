#!/usr/bin/python
# -*- coding: utf-8 -*-

from qframer.qt.QtCore import *
from qframer.qt.QtGui import *
from qframer.resources import *
from qframer import FMenu


class SkinMenu(FMenu):

    skinIDSin = Signal(str)

    def __init__(self, parent=None):
        super(SkinMenu, self).__init__(parent)
        self.parent = parent
        self.menuItems = [
            {
                'name': self.tr('BW'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'BW',
                "checkable": True
            },
            {
                'name': self.tr('BB'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'BB',
                "checkable": True
            },
            {
                'name': self.tr('GB'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'GB',
                "checkable": True
            },
            {
                'name': self.tr('GG'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'GG',
                "checkable": True
            },
            {
                'name': self.tr('GBG'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'GBG',
                "checkable": True
            },
            {
                'name': self.tr('GGG'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'GGG',
                "checkable": True
            },
            {
                'name': self.tr('Blank'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'Blank',
                "checkable": True
            },
        ]
        self.creatMenus(self.menuItems)

        self.skinNames = [item['name'] for item in self.menuItems]
        self.initConnect()
        getattr(self, '%sAction' % self.skinNames[1]).setChecked(True)

    def initConnect(self):
        for key, action in self.qactions.items():
            action.triggered.connect(self.updateChecked)

    def updateChecked(self):
        for key, action in self.qactions.items():
            if self.sender() is action:
                action.setChecked(True)
                self.skinIDSin.emit(key)
            else:
                action.setChecked(False)

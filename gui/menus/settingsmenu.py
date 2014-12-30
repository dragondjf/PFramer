#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from qframer.resources import *
from qframer import views
from qframer import FMenu

class SettingsMenu(FMenu):

    """docstring for SettingsMenu"""

    def __init__(self, parent=None):
        super(SettingsMenu, self).__init__(parent)
        self.parent = parent
        self.menuItems = [
            {
                'name': self.tr('Login'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'Login',
            },
            {
                'name': self.tr('Show suspension window'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'Suspension',
            },
            {
                'name': self.tr('Language'),
                'trigger': 'Language',
                'type': 'submenu',
                'actions': [
                    {
                        'name': 'English',
                        'icon': u'',
                        'shortcut': u'',
                        'trigger': 'English',
                        "checkable": True
                    },
                    {
                        'name': 'Chinese',
                        'icon': u'',
                        'shortcut': u'',
                        'trigger': 'Chinese',
                        "checkable": True
                    },
                ]
            },
            {
                'name': self.tr('Document'),
                'trigger': 'Document',
                'type': 'submenu',
                'actions': [
                    {
                        'name': 'Android developer guide',
                        'icon': u'',
                        'shortcut': u'',
                        'trigger': 'AndroidDeveloper',
                        "checkable": False
                    },
                    {
                        'name': 'iOS developer guide',
                        'icon': u'',
                        'shortcut': u'',
                        'trigger': 'IOSDeveloper',
                        "checkable": False
                    },
                    {
                        'name': 'Ford developer center',
                        'icon': u'',
                        'shortcut': u'',
                        'trigger': 'FordDeveloper',
                        "checkable": False
                    },
                ]
            },
            {
                'name': self.tr('ObjectView'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'ObjectView',
            },
            {
                'name': self.tr('About'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'About',
            },
            {
                'name': self.tr('Exit'),
                'icon': u'',
                'shortcut': u'',
                'trigger': 'Exit',
            },
        ]
        self.creatMenus(self.menuItems)
        self.initConnect()
        getattr(self, '%sAction' % 'English').setChecked(True)

    def initConnect(self):
        for item in ['English', 'Chinese']:
            getattr(self, '%sAction' % item).triggered.connect(self.updateChecked)

    def updateChecked(self):
        for item in ['English', 'Chinese']:
            action = getattr(self, '%sAction' % item)
            if self.sender() is action:
                action.setChecked(True)
            else:
                action.setChecked(False)

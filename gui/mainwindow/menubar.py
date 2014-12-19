#!/usr/bin/python
# -*- coding: utf-8 -*-

from qframer.qt.QtCore import *
from qframer.qt.QtGui import *
from qframer import FMenuBar
from qframer import collectView, views

class MenuBar(FMenuBar):

    viewID = "MenuBar"

    @collectView
    def __init__(self, parent=None):
        super(MenuBar, self).__init__(parent)
        self.menuItems = {
            'menus': [
                {
                    'name': self.tr('File'),
                    'trigger': 'File',
                    'actions': [
                        {
                            'name': self.tr('Settings'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'Settings',
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
                            'name': self.tr('Exit'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'Exit',
                        },
                    ]
                },
                {
                    'name': self.tr('Screen'),
                    'trigger': 'Screen',
                    'actions': [
                        {
                            'name': self.tr('MFD3'),

                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'MFD3',
                            "checkable": True
                        },
                        {
                            'name': self.tr('MFD4'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'MFD4',
                            "checkable": True
                        },
                    ]
                },
                {
                    'name': self.tr('Device'),
                    'trigger': 'Device',
                    'actions': [
                        # {
                        #     'name': self.tr('Enable Bluetooth'),
                        #     'icon': u'',
                        #     'shortcut': u'',
                        #     'trigger': 'EnableBluetooth',
                        # },
                        {
                            'name': self.tr('Search Devices'),

                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'SearchDevices',
                        },
                    ]
                },
                {
                    'name': self.tr('View'),
                    'trigger': 'View',
                    'actions': [
                    ]
                },
                {
                    'name': self.tr('Report'),
                    'trigger': 'Test Rig',
                    'actions': [
                        {
                            'name': self.tr('Report'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'TestRigAll',
                        },
                        {
                            'name': self.tr('Start'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'TestRig',
                        }
                    ]
                },
                {
                    'name': self.tr(' Help '),
                    'trigger': 'Help',
                    'actions': [
                        {
                            'name': self.tr('About ALE'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'About',
                        },
                        {
                            'name': self.tr('Feedback to us'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'Feedbackus',
                        },
                    ]
                }
            ]
        }
        self.creatMenus(self.menuItems)

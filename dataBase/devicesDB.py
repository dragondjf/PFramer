# -*- coding: utf-8 -*-

class DevicesDB(object):
    def __init__(self, parent=None):
        self.devices = {}
        self.currentDevice = None

    def updateDevice(self, devices):
		for dev in devices:
			self.devices[dev['id']] = dev

    def setCurrentDevice(self, deviceID):
        pass


devices_DB = DevicesDB()
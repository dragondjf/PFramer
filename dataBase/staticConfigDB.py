# -*- coding: utf-8 -*-
#=============================================================================
# Copyright (c) 2013, Ford Motor Company All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer. Redistributions in binary
# form must reproduce the above copyright notice, this list of conditions and
# the following disclaimer in the documentation and/or other materials provided
# with the distribution. Neither the name of the Ford Motor Company nor the
# names of its contributors may be used to endorse or promote products derived
# from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#=============================================================================


class StaticConfig(object):
    sdlLanguagesList = [
        'EN-US',
        'ES-MX',
        'FR-CA',
        'DE-DE',
        'ES-ES',
        'EN-GB',
        'RU-RU',
        'TR-TR',
        'PL-PL',
        'FR-FR',
        'IT-IT',
        'SV-SE',
        'PT-PT',
        'NL-NL',
        'ZH-TW',
        'JA-JP',
        'AR-SA',
        'KO-KR',
        'PT-BR',
        'CS-CZ',
        'DA-DK',
        'NO-NO'
    ]

    hmiUILanguage = 'EN-US'

    hmiTTSVRLanguage = 'EN-US'

    resultCode = {
        "SUCCESS": 0,
        "UNSUPPORTED_REQUEST": 1,
        "UNSUPPORTED_RESOURCE": 2,
        "DISALLOWED": 3,
        "REJECTED": 4,
        "ABORTED": 5,
        "IGNORED": 6,
        "RETRY": 7,
        "IN_USE": 8,
        "DATA_NOT_AVAILABLE": 9,
        "TIMED_OUT": 10,
        "INVALID_DATA": 11,
        "CHAR_LIMIT_EXCEEDED": 12,
        "INVALID_ID": 13,
        "DUPLICATE_NAME": 14,
        "APPLICATION_NOT_REGISTERED": 15,
        "WRONG_LANGUAGE": 16,
        "OUT_OF_MEMORY": 17,
        "TOO_MANY_PENDING_REQUESTS": 18,
        "NO_APPS_REGISTERED": 19,
        "NO_DEVICES_CONNECTED": 20,
        "WARNINGS": 21,
        "GENERIC_ERROR": 22,
        "USER_DISALLOWED": 23
    }

    vehicleType = {
        "make": "Ford",
        "model": "Fiesta",
        "modelYear": "2013",
        "trim": "SE"
    }

    vehicleData = {
        'speed': 80.0,
        'rpm': 5000,
        'fuelLevel': 0.2,
        'fuelLevel_State': "UNKNOWN",
        'instantFuelConsumption': 2.2,
        'tirePressure': "UNKNOWN",
        'beltStatus': {
            'driverBeltDeployed': "NOT_SUPPORTED",
            'passengerBeltDeployed': "NOT_SUPPORTED",
            'passengerBuckleBelted': "NOT_SUPPORTED",
            'driverBuckleBelted': "NOT_SUPPORTED",
            'leftRow2BuckleBelted': "NOT_SUPPORTED",
            'passengerChildDetected': "NOT_SUPPORTED",
            'rightRow2BuckleBelted': "NOT_SUPPORTED",
            'middleRow2BuckleBelted': "NOT_SUPPORTED",
            'middleRow3BuckleBelted': "NOT_SUPPORTED",
            'leftRow3BuckleBelted': "NOT_SUPPORTED",
            'rightRow3BuckleBelted': "NOT_SUPPORTED",
            'leftRearInflatableBelted': "NOT_SUPPORTED",
            'rightRearInflatableBelted': "NOT_SUPPORTED",
            'middleRow1BeltDeployed': "NOT_SUPPORTED",
            'middleRow1BuckleBelted': "NOT_SUPPORTED"
        },
        'bodyInformation': {
            'parkBrakeActive': False,
            'ignitionStableStatus': "MISSING_FROM_TRANSMITTER",
            'ignitionStatus': "UNKNOWN"
        },
        'deviceStatus': {
            'voiceRecOn': False,
            'btIconOn': False,
            'callActive': False,
            'phoneRoaming': False,
            'textMsgAvailable': False,
            'battLevelStatus': "NOT_PROVIDED",
            'stereoAudioOutputMuted': False,
            'monoAudioOutputMuted': False,
            'signalLevelStatus': "NOT_PROVIDED",
            'primaryAudioSource': "NO_SOURCE_SELECTED",
            'eCallEventActive': False
        },
        'driverBraking': "NOT_SUPPORTED",
        'wiperStatus': "NO_DATA_EXISTS",
        'headLampStatus': {
            "lowBeamsOn": False,
            "highBeamsOn": False
        },
        'engineTorque': 2.5,
        'accPedalPosition': 0.5,
        'steeringWheelAngle': 1.2,
        'myKey': {
            "e911Override": "NO_DATA_EXISTS"
        },
        'avgFuelEconomy': 0.1,
        'batteryVoltage': 12.5,
        'externalTemperature': 40.0,
        'vin': '52-452-52-752',
        'prndl': 'PARK',
        'batteryPackVoltage': 12.5,
        'batteryPackCurrent': 7.0,
        'batteryPackTemperature': 30,
        'engineTorque': 650,
        'tripOdometer': 0,
        'genericbinary': '165165650',
        'satRadioESN': "165165650",
        'rainSensor': 165165650,
        'gps': {
            'longitudeDegrees': 423293,
            'latitudeDegrees': -830464,
            'utcYear': 2013,
            'utcMonth': 2,
            'utcDay': 14,
            'utcHours': 13,
            'utcMinutes': 16,
            'utcSeconds': 54,
            'compassDirection': 'SOUTHWEST',
            'pdop': 15,
            'hdop': 5,
            'vdop': 30,
            'actual': False,
            'satellites': 8,
            'dimension': '2D',
            'altitude': 7,
            'heading': 173,
            'speed': 2
        }
    }

    capabilities = [
        {
            "name": "PRESET_0",
            "shortPressAvailable": True,
            "longPressAvailable": True,
            "upDownAvailable": True
        }, {
            "name": "PRESET_1",
            "shortPressAvailable": True,
            "longPressAvailable": True,
            "upDownAvailable": True
        }, {
            "name": "PRESET_2",
            "shortPressAvailable": True,
            "longPressAvailable": True,
            "upDownAvailable": True
        }, {
            "name": "PRESET_3",
            "shortPressAvailable": True,
            "longPressAvailable": True,
            "upDownAvailable": True
        }, {
            "name": "PRESET_4",
            "shortPressAvailable": True,
            "longPressAvailable": True,
            "upDownAvailable": True
        }, {
            "name": "PRESET_5",
            "shortPressAvailable": True,
            "longPressAvailable": True,
            "upDownAvailable": True
        }, {
            "name": "PRESET_6",
            "shortPressAvailable": True,
            "longPressAvailable": True,
            "upDownAvailable": True
        }, {
            "name": "PRESET_7",
            "shortPressAvailable": True,
            "longPressAvailable": True,
            "upDownAvailable": True
        }, {
            "name": "PRESET_8",
            "shortPressAvailable": True,
            "longPressAvailable": True,
            "upDownAvailable": True
        }, {
            "name": "PRESET_9",
            "shortPressAvailable": True,
            "longPressAvailable": True,
            "upDownAvailable": True
        }, {
            "name": "OK",
            "shortPressAvailable": True,
            "longPressAvailable": True,
            "upDownAvailable": True
        }, {
            "name": "SEEKLEFT",
            "shortPressAvailable": True,
            "longPressAvailable": True,
            "upDownAvailable": True
        }, {
            "name": "SEEKRIGHT",
            "shortPressAvailable": True,
            "longPressAvailable": True,
            "upDownAvailable": True
        }, {
            "name": "TUNEUP",
            "shortPressAvailable": True,
            "longPressAvailable": True,
            "upDownAvailable": True
        }, {
            "name": "TUNEDOWN",
            "shortPressAvailable": True,
            "longPressAvailable": True,
            "upDownAvailable": True
        }
    ]
    def __init__(self):
        super(StaticConfig, self).__init__()

staticConfig_DB = StaticConfig()
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

from signalDB import signal_DB
from logDB import log_DB
from devicesDB import devices_DB
from appsDB import apps_DB
from staticConfigDB import staticConfig_DB

from loginDB import login_DB

from log import logger


getProtocol = [
    "alert",
    "show",
    "scrollMessage",
    "command",
    "audioRecord",
    "interaction",
    "mediaClock",
    "device",
    "choiceSet",
    "log",
    "getVehicleData"
]


# speak getVehicleData倾向于protocolHandler直接处理掉
# log 倾向于直接传递数据 
def getData(getid):
    if getid == "alert":
        logger.info("alert")
    elif getid == "app":
        return getApp()
    elif getid == "show":
        logger.info("show")
    elif getid == "scrollMessage":
        logger.info("scrollMessage")
    elif getid == "command":
        logger.info("command")
    elif getid == "speak":
        logger.info("speak")
    elif getid == "audioRecord":
        logger.info("audioRecord")
    elif getid == "interaction":
        logger.info("interaction")
    elif getid == "mediaClock":
        logger.info("mediaClock")
    elif getid == "device":
        logger.info("device")
    elif getid == "choiceSet":
        logger.info("choiceSet")
    elif getid == "log":
        logger.info("log")
    elif getid == "getVehicleData":
        logger.info("getVehicleData")
    else:
        logger.info("error")

def getApp():
    apps = []
    for app in apps_DB.apps:
        apps.append({"appID": app, "appName": apps_DB.apps[app].appName})

    return apps
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

import time


class LogDB(object):
    allLogList = {}

    def __init__(self):
        super(LogDB, self).__init__()

    def addLog(self, log):
        self._addLog(log, self.allLogList)

    def _addLog(self, log, logs):
        _time = time.time()
        _type = log['type']
        _correlation_id = log['correlation_id']
        _app_id = log["app_id"]
        if _correlation_id is None:
            _logobj = {
                "time": _time,
                "function": log["function"],
                "data": log["data"],
                "type": _type,
                "app_id": _app_id
            }
        else:
            _logobj = {
            "time": _time,
            "function": log["function"],
            "data": log["data"],
            "type": _type,
            "correlation_id": _correlation_id,
            "app_id": _app_id
            }
        if _app_id not in logs:
            logs[_app_id] = {
                "start": _time,
                "response": {},
                "requestList_notificationList": [],
                "stop": _time
            }
        if _type == "response":
            logs[_app_id][_type][_correlation_id] = _logobj
        else:
            logs[_app_id]["requestList_notificationList"].append(_logobj)

        # if _type == "notification":
        #     logs[_app_id][_type].append(_logobj)
        # else:
        #     logs[_app_id][_type][_correlation_id] = _logobj

        if _type == "request" and log["function"] == "RegisterAppInterface":
            logs[_app_id]['appID'] = _app_id
            if "appName" in log['data']:
                logs[_app_id]['appName'] = log["data"]["appName"]
            else:
                logs[_app_id]['appName'] = ""

            if "ttsName" in log['data']:
                logs[_app_id]['ttsName'] = log["data"]["ttsName"]
            else:
                logs[_app_id]['ttsName'] = ""

            if "vrSynonyms" in log['data']:
                logs[_app_id]['vrSynonyms'] = log["data"]["vrSynonyms"]
            else:
                logs[_app_id]['vrSynonyms'] = ""

            if "ngnMediaScreenAppName" in log['data']:
                logs[_app_id]['ngnMediaScreenAppName'] = log["data"]["ngnMediaScreenAppName"]
            else:
                logs[_app_id]['ngnMediaScreenAppName'] = ""

        logs[_app_id]["stop"] = _time


log_DB = LogDB()
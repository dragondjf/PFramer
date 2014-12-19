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

import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from logging import RootLogger
import traceback
from settings import domain, __version__, isPublished


class ALERootLogger(RootLogger):

    def __init__(self, level):
        super(ALERootLogger, self).__init__(level)

    def error(self, msg, *args, **kwargs):
        _t = traceback.format_exc()
        if _t == "None\n":
            msg = msg
        else:
            msg = _t[:-1]
        super(ALERootLogger, self).error(msg, *args, **kwargs)
        if isPublished:
            self.senderror(msg)

    @classmethod
    def senderror(cls, msg):
        print(msg, "---by jack.zh")

def handle_exception(exc_type, exc_value, exc_traceback):
    info = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    ALERootLogger.senderror(repr("Uncaught exception %s" % info))

logging.root = ALERootLogger(logging.WARNING)
logging.root.setLevel(logging.DEBUG)
logging.root.propagate = 0
#log write in file
logpath = os.sep.join([os.getcwd(), 'log', 'main.log'])
fh = RotatingFileHandler(logpath, maxBytes=10 * 1024 * 1024, backupCount=100)
fh.setLevel(logging.ERROR)
#log write in console
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
#log formatter
formatter = logging.Formatter('%(asctime)s %(levelname)8s [%(pathname)s%(lineno)06s] %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logging.root.addHandler(fh)

if isPublished:
    pass
else:
    logging.root.addHandler(ch)

logger = logging.root
logger.propagate = 0

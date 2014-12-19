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

"""
py2app/py2exe build script for ALE
    
Will automatically ensure that all build prerequisites are available
via ez_setup

Usage (Mac OS X):
python setupmac.py py2app

Command Line Run:
./distmac/ALE.app/Contents/MacOS/ALE
    
"""

#import ez_setup
#ez_setup.use_setuptools()

import sys
from setuptools import setup
# from util import publish_set
import shutil

main = 'main.py'
#inc = ["sip", "PySide.QtCore","PySide.QtGui"]
inc = []
res = 'gui/skin'

exc = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
       'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
       'Tkconstants', 'Tkinter']

extra_options = dict(
                     setup_requires=['py2app'],
                     app=[main],
                     options=dict(py2app=dict(argv_emulation=True,
                                              optimize=1,
                                              includes=inc,
                                              resources=res,
                                              excludes=exc,
                                              iconfile='gui/skin/icon.icns'
                                              ))
                     )

setup(  
  name="ALE",
  **extra_options
  )

# # shutil.copytree("config", "dist/ALE.app/Contents/Resources/config")

# import email
# emailpath = email.__path__[0]
# shutil.copytree(emailpath, "dist/ALE.app/Contents/Resources/lib/python2.7/email")

# publish_set()

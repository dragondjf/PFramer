

"""
py2app/py2exe build script for ALE
    
Will automatically ensure that all build prerequisites are available
via ez_setup

Usage (Mac OS X):
python setupmac.py py2app

Command Line Run:
./distmac/ALE.app/Contents/MacOS/ALE
    
"""

import sys
from setuptools import setup
import shutil

main = 'main.py'
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
                                              iconfile='gui/skin/images/AppClient.icns'
                                              ))
                     )

setup(  
  name="AppClient",
  **extra_options
  )


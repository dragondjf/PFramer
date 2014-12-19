#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
setattr(sys, 'SELECT_QT_BINDING', 'pyside')
from python_qt_binding.binding_helper import loadUi, QT_BINDING, QT_BINDING_MODULES, QT_BINDING_VERSION  # @UnusedImport

# register all binding modules as sub modules of this package (python_qt_binding) for easy importing
for module_name, module in QT_BINDING_MODULES.items():
    sys.modules[__name__ + '.' + module_name] = module
    setattr(sys.modules[__name__], module_name, module)
    del module_name
    del module

del sys

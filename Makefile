
USES_PYSIDE = True

ifeq ($(shell uname), Linux)

else
pyside_rcc = "/c/Python27/Lib/site-packages/PySide/pyside-rcc.exe"
pyqt4_rcc = "/c/Python27/Lib/site-packages/PyQt4/pyrcc4.exe"

ifeq ($(USES_PYSIDE), True)
	RCC = $(pyside_rcc)
else
	RCC = $(pyqt4_rcc)
endif

endif

all:
	@echo "noop for debbuild", $(USES_PYSIDE)

rcc:
	$(RCC) ./gui/skin/icon.qrc -o ./gui/resources/qrc_icons_py27.py

.PHONY: all

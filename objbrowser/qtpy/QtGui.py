# -*- coding: utf-8 -*-
#
# Copyright © 2014-2015 Colin Duquesnoy
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)

"""
Provides QtGui classes and functions.
.. warning:: Only PyQt4/PySide QtGui classes compatible with PyQt5.QtGui are
    exposed here. Therefore, you need to treat/use this package as if it were
    the ``PyQt5.QtGui`` module.
"""

from objbrowser.qtpy import PYQT5, PYQT4, PYSIDE, PythonQtError


if PYQT5:
    from PyQt5.QtGui import *
elif PYQT4:
    from PyQt4.Qt import QKeySequence, QTextCursor
    from PyQt4.QtGui import (QAbstractTextDocumentLayout, QActionEvent, QBitmap,
                             QBrush, QClipboard, QCloseEvent, QColor,
                             QConicalGradient, QContextMenuEvent, QCursor,
                             QDesktopServices, QDoubleValidator, QDrag,
                             QDragEnterEvent, QDragLeaveEvent, QDragMoveEvent,
                             QDropEvent, QFileOpenEvent, QFocusEvent, QFont,
                             QFontDatabase, QFontInfo, QFontMetrics,
                             QFontMetricsF, QGlyphRun, QGradient, QHelpEvent,
                             QHideEvent, QHoverEvent, QIcon, QIconDragEvent,
                             QIconEngine, QImage, QImageIOHandler, QImageReader,
                             QImageWriter, QInputEvent, QInputMethodEvent,
                             QKeyEvent, QLinearGradient,
                             QMatrix2x2, QMatrix2x3, QMatrix2x4, QMatrix3x2,
                             QMatrix3x3, QMatrix3x4, QMatrix4x2, QMatrix4x3,
                             QMatrix4x4, QMouseEvent, QMoveEvent, QMovie,
                             QPaintDevice, QPaintEngine, QPaintEngineState,
                             QPaintEvent, QPainter, QPainterPath,
                             QPainterPathStroker, QPalette, QPen, QPicture,
                             QPictureIO, QPixmap, QPixmapCache, QPolygon,
                             QPolygonF, QQuaternion, QRadialGradient, QRawFont,
                             QRegExpValidator, QRegion, QResizeEvent,
                             QSessionManager, QShortcutEvent, QShowEvent,
                             QStandardItem, QStandardItemModel, QStaticText,
                             QStatusTipEvent, QSyntaxHighlighter, QTabletEvent,
                             QTextBlock, QTextBlockFormat, QTextBlockGroup,
                             QTextBlockUserData, QTextCharFormat,
                             QTextDocument, QTextDocumentFragment,
                             QTextDocumentWriter, QTextFormat, QTextFragment,
                             QTextFrame, QTextFrameFormat, QTextImageFormat,
                             QTextInlineObject, QTextItem, QTextLayout,
                             QTextLength, QTextLine, QTextList, QTextListFormat,
                             QTextObject, QTextObjectInterface, QTextOption,
                             QTextTable, QTextTableCell, QTextTableCellFormat,
                             QTextTableFormat, QTouchEvent, QTransform,
                             QValidator, QVector2D, QVector3D, QVector4D,
                             QWhatsThisClickedEvent, QWheelEvent,
                             QWindowStateChangeEvent, qAlpha, qBlue,
                             qFuzzyCompare, qGray, qGreen, qIsGray, qRed, qRgb,
                             qRgba, QIntValidator)
elif PYSIDE:
    from PySide2.QtGui import *
else:
    raise PythonQtError('No Qt bindings could be found')

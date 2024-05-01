"""
Initialise the QDarkGrayStyleSheet module when used with python.

This modules provides a function to transparently load the stylesheets
with the correct rc file.
"""

import logging
import platform

from PyQt5 import QtCore

from qdarkgraystyle import compile_qrc, pyqt5_style_rc

__version__ = "2.0.0"


def _logger():
    return logging.getLogger("qdarkgraystyle")


def load_stylesheet():
    """
    Loads the stylesheet for use in a pyqt5 application.
    :return the stylesheet string
    """

    # Smart import of the rc file
    f = QtCore.QFile(":qdarkgraystyle/style.qss")

    if not f.exists():
        _logger().error("Unable to load stylesheet, file not found in resources")
        return ""

    f.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)

    ts = QtCore.QTextStream(f)
    stylesheet = ts.readAll()

    if platform.system().lower() == "darwin":
        mac_fix = """
        QDockWidget::title
        {
            background-color: #31363b;
            text-align: center;
            height: 12px;
        }
        """
        stylesheet += mac_fix

    return stylesheet

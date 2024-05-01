"""
A simple example of use.

Load an ui made in QtDesigner and apply the DarkStyleSheet.


Requirements:
    - Python 3
    - PyQt5

.. note.. :: qdarkgraystyle does not have to be installed to run
    the example

"""

import logging
import sys
import unittest

from .example.ui import example_pyqt5_ui as example_ui
from PyQt5 import QtCore, QtWidgets

import qdarkgraystyle


class TestPyQt5(unittest.TestCase):

    def test_create_main_window(self):
        """
        Application entry point
        """
        logging.basicConfig(level=logging.DEBUG)
        # create the application and the main window
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()

        # setup ui
        ui = example_ui.Ui_MainWindow()
        ui.setupUi(window)

        # setup stylesheet
        app.setStyleSheet(qdarkgraystyle.load_stylesheet())

        # auto quit after 2s when testing
        QtCore.QTimer.singleShot(2000, app.exit)

        # run
        window.show()
        app.exec_()

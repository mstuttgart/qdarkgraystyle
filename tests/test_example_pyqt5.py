#!/usr/bin/env python
#
# The MIT License (MIT)
#
# Copyright (c) <2013-2014> <Colin Duquesnoy>
# Copyright (c) <2017-2018> <Michell Stuttgart>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
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
import unittest
import sys
import os

from PyQt5 import QtWidgets, QtCore

import qdarkgraystyle
from example.ui import example_pyqt5_ui as example_ui


class TestPyQt5(unittest.TestCase):

    def setUp(self):
        super(TestPyQt5, self).setUp()

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

        # auto quit after 2s when testing on travis-ci
        QtCore.QTimer.singleShot(2000, app.exit)

        # run
        window.show()
        app.exec_()

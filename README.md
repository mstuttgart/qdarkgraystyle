<h2 align="center">
    <br>
  <a href="https://pypi.org/project/qdarkgraystyle/">
    <img src="https://github.com/mstuttgart/qdarkgraystyle/assets/8174740/100633c4-1c13-4cee-9fc2-5ae54a3dd647" width="20%">
  </a>
  <br>
    Darkgrey Stylesheet for PyQt5
</h2>

<p align="center">

  <a href="https://github.com/mstuttgart/qdarkgraystyle/actions?query=workflow%3A%22Github+CI%22">
    <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/mstuttgart/qdarkgraystyle/test.yml?&color=d1dbcb&labelColor=323232&branch=develop&style=for-the-badge">
  </a>

  <a href="https://pypi.org/project/qdarkgraystyle">
    <img src="https://img.shields.io/pypi/dm/qdarkgraystyle?&color=d1dbcb&labelColor=323232&style=for-the-badge" alt="Downloads">
  </a>

  <a href="https://pypi.org/project/qdarkgraystyle">
    <img src="https://img.shields.io/pypi/v/qdarkgraystyle?style=for-the-badge&color=d1dbcb&labelColor=323232" alt="Ratings">
  </a>

  <a href="https://pypi.org/project/qdarkgraystyle/">
    <img src="https://img.shields.io/pypi/pyversions/qdarkgraystyle?style=for-the-badge&color=d1dbcb&labelColor=323232" alt="Version">
  </a>

</p>

<p align="center">
  <a href="#about">About</a> |
  <a href="#install">Install</a> |
  <a href="#how-to-use">How to Use</a> |
  <a href="#contribute">Contribute</a> |
  <a href="#credits">Credits</a>
</p>

# About

A dark gray stylesheet for PyQt5 applications. This theme is a gray variation of [QDarkStyleSheet](https://github.com/ColinDuquesnoy/QDarkStyleSheet) theme.

# Install

Install **qdarkgraystyle** package using using *pip*

> pip install qdarkgraystyle

This package work on **PyQt5 >=5.6**.

# How to Use

Here is an example using PyQt5.

```python
import sys
import qdarkgraystyle
from PyQt5 import QtWidgets

# create the application and the main window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

# setup stylesheet
app.setStyleSheet(qdarkgraystyle.load_stylesheet())

# run
window.show()
app.exec_()
```

There is an example included in the *example* folder.

> python3 setup.py test

You can run the script without installing `qdarkgraystyle`. You only need to have
PyQt5 installed on your system.

# Contribute

See this *guideline* [here](https://github.com/mstuttgart/qdarkgraystyle/blob/develop/CONTRIBUTING.md).

# Credits
This package is totally based on [QDarkStyleSheet](https://github.com/ColinDuquesnoy/QDarkStyleSheet)  theme created by [Colin Duquesnoy](https://github.com/ColinDuquesnoy).

Copyright (C) 2017-2024 by Michell Stuttgart

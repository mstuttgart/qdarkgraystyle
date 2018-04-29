# QDarkGray Stylesheet

[![Build Status](https://img.shields.io/travis/mstuttgart/qdarkgray-stylesheet/master.png?style=flat-square)](https://travis-ci.org/mstuttgart/qdarkgray-stylesheet)
[![Latest PyPI version](https://img.shields.io/pypi/v/qdarkgraystyle.svg?style=flat-square)](https://pypi.python.org/pypi/qdarkgraystyle)
[![Python versions](https://img.shields.io/pypi/pyversions/qdarkgraystyle.svg?style=flat-square)](https://pypi.python.org/pypi/qdarkgraystyle)
[![License: MIT](https://img.shields.io/pypi/l/qdarkgraystyle.svg?style=flat-square)](https://opensource.org/licenses/MIT)


A dark gray stylesheet for PyQt5 applications. This theme is a gray variation of [QDarkStyleSheet](https://github.com/ColinDuquesnoy/QDarkStyleSheet) theme.

## Installation

Install **qdarkgraystyle** package using the *setup* script or using *pip*:

```
pip install qdarkgraystyle
```

To use `qdarkgraystyle` with PySide or PyQt and with Python2. Please install the old version `0.0.3` :

```
pip install qdarkgraystyle==0.0.3
```

## Usage

Here is an example using PyQt5:

```python

    import sys
    import qdarkgraystyle
    from PyQt5 import QtGui
    
    
    # create the application and the main window
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    
    # setup stylesheet
    app.setStyleSheet(qdarkgraystyle.load_stylesheet())
    
    # run
    window.show()
    app.exec_()

```

There is an example included in the *example* folder.
You can run the script without installing `qdarkgraystyle`. You only need to have PyQt5 installed on your system.

## Contribute

- Issue Tracker: https://github.com/mstuttgart/qdarkgray-stylesheet/issues
- Source Code: https://github.com/mstuttgart/qdarkgray-stylesheet

## Snapshots

Here are a few snapshots:

![https://github.com/mstuttgart/qdarkgray-stylesheet/blob/master/screenshots/screen-01.png](https://github.com/mstuttgart/qdarkgray-stylesheet/blob/master/screenshots/screen-01.png)
![https://github.com/mstuttgart/qdarkgray-stylesheet/blob/master/screenshots/screen-03.png](https://github.com/mstuttgart/qdarkgray-stylesheet/blob/master/screenshots/screen-03.png)


## Contributing

1. Fork it: [https://github.com/mstuttgart/qdarkgray-stylesheet/fork](https://github.com/mstuttgart/qdarkgray-stylesheet/fork)
2. Create your feature branch:
 > git checkout -b feature/fooBar
3. Commit your changes: 
 > git commit -am 'Add some fooBar'
4. Push to the branch:
 > git push origin feature/fooBar
5. Create a new Pull Request

## Credits

This package is totally based on [QDarkStyleSheet](https://github.com/ColinDuquesnoy/QDarkStyleSheet) theme created by [Colin Duquesnoy](https://github.com/ColinDuquesnoy).

Copyright (C) 2017-2018 by Michell Stuttgart Faria

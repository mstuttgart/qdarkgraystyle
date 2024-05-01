# QDarkGray Stylesheet

A dark gray stylesheet for PyQt5 applications. This theme is a gray variation of `QDarkStyleSheet <https://github.com/ColinDuquesnoy/QDarkStyleSheet>`_ theme.

## Installation

Install **qdarkgraystyle** package using using *pip*

> pip install qdarkgraystyle

## Usage

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

## Contribute

- Issue Tracker: https://github.com/mstuttgart/qdarkgraystyle/issues
- Source Code: https://github.com/mstuttgart/qdarkgraystyle

## Snapshots

Here are a few snapshots:

* `Screenshot 1 <https://github.com/mstuttgart/qdarkgraystyle/blob/master/screenshots/screen-01.png>`_
* `Screenshot 2 <https://github.com/mstuttgart/qdarkgraystyle/blob/master/screenshots/screen-02.png>`_
* `Screenshot 3 <https://github.com/mstuttgart/qdarkgraystyle/blob/master/screenshots/screen-03.png>`_

## Contributing

1. Fork it (https://github.com/mstuttgart/qdarkgraystyle/fork)
2. Create your feature branch (``git checkout -b feature/fooBar``)
3. Commit your changes (``git commit -am 'Add some fooBar'``)
4. Push to the branch (``git push origin feature/fooBar``)
5. Create a new Pull Request

## Credits
This package is totally based on `QDarkStyleSheet <https://github.com/ColinDuquesnoy/QDarkStyleSheet>`_ theme created by `Colin Duquesnoy <https://github.com/ColinDuquesnoy>`_.

Copyright (C) 2017-2024 by Michell Stuttgart

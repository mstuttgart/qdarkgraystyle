QDarkStylesheet
==================

[![Build Status](https://travis-ci.org/mstuttgart/QDarkStyleSheet.png?branch=master)](https://travis-ci.org/ColinDuquesnoy/QDarkStyleSheet)
[![Number of PyPI downloads](https://img.shields.io/pypi/dm/QDarkStyle.svg)](https://pypi.python.org/pypi/QDarkStyle)
[![Latest PyPI version](https://img.shields.io/pypi/v/QDarkStyle.svg)](https://pypi.python.org/pypi/QDarkStyle)

A dark stylesheet for Qt applications (Qt4, Qt5, PySide, PyQt4 and PyQt5).


License
===========

This project is licensed under the MIT license.


Installation
==============

Python
-----------

Install ``qdarkstyle`` package using the *setup* script or using *pip*:

```bash
python setup.py install
```

or

```bash
pip install qdarkstyle
```

C++
---------

1) Download/clone the project and copy the following files to your application directory (keep the existing directory hierarchy):

 - **qdarkstyle/style.qss**
 - **qdarkstyle/style.qrc**
 - **qdarkstyle/rc/** (the whole directory)

2) Add **qdarkstyle/style.qrc** to your **.pro file**

3) Load the stylesheet:

```cpp
QFile f(":qdarkstyle/style.qss");
if (!f.exists())
{
    printf("Unable to set stylesheet, file not found\n");
}
else
{
    f.open(QFile::ReadOnly | QFile::Text);
    QTextStream ts(&f);
    qApp->setStyleSheet(ts.readAll());
}

```



Usage
============

Here is an example using PySide:


```Python
import sys
import qdarkstyle
from PySide import QtGui


# create the application and the main window
app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()

# setup stylesheet
app.setStyleSheet(qdarkstyle.load_stylesheet())

# run
window.show()
app.exec_()
```

To use PyQt4 instead of PySide, you just need to replace

```Python
app.setStyleSheet(qdarkstyle.load_stylesheet())
```

by

```Python
app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
```

and
```
from PySide import QtGui
```

by

```
from PyQt4 import QtGui
```

To use PyQt5, you need to use ``load_stylesheet_pyqt5`` instead of
``load_stylesheet``.

_There is an example included in the *example* folder.
You can run the script without installing qdarkstyle. You only need to have
PySide (or PyQt4 or PyQt5) installed on your system._


Issues:
-------

  - Maintainer: michellstutggart@gmail.com
  - Homepage: https://github.com/ColinDuquesnoy/QDarkStyleSheet

Snapshots
---------

Here are a few snapshots:

![alt text](/screenshots/QDarkStyle example 1.png "QDarkStyle example 1")
![alt text](/screenshots/QDarkStyle example 2.png "QDarkStyle example 2")

Copyright
----------
This package is totally based on `QDarkStyleSheet 
<https://github.com/ColinDuquesnoy/QDarkStyleSheet>`_ made by `Colin 
Duquesnoy <https://github.com/ColinDuquesnoy>`_.
QDarkGray Stylesheet
====================

.. image:: https://travis-ci.org/mstuttgart/qdarkgray-stylesheet.svg?branch=master?style=flat-square
    :target: https://travis-ci.org/mstuttgart/qdarkgray-stylesheet

.. image:: https://github.com/mstuttgart/qdarkgraystyle.svg?style=flat-square
    :target: https://github.com/mstuttgart/qdarkgraystyle

.. image:: https://github.com/mstuttgart/qdarkgraystyle.svg?style=flat-square
    :target: https://github.com/mstuttgart/qdarkgraystyle

.. image:: https://github.com/mstuttgart/qdarkgraystyle.svg?style=flat-square
    :target: https://github.com/mstuttgart/qdarkgraystyle

.. image:: https://github.com/mstuttgart/qdarkgraystyle.svg?style=flat-square
    :target: https://github.com/mstuttgart/qdarkgraystyle/blob/master/LICENSE

A dark stylesheet for Qt applications (Qt4, Qt5, PySide, PyQt4 and PyQt5).

Installation
============

Python
-----------

Install `qdarkgraystyle` package using the *setup* script or using *pip*:

```bash
python setup.py install
```

or

```bash
pip install qdarkgraystyle
```

C++
---------

1) Download/clone the project and copy the following files to your application directory (keep the existing directory hierarchy):

 - **qdarkgraystyle/style.qss**
 - **qdarkgraystyle/style.qrc**
 - **qdarkgraystyle/rc/** (the whole directory)

2) Add **qdarkgraystyle/style.qrc** to your **.pro file**

3) Load the stylesheet:

```cpp
QFile f(":qdarkgraystyle/style.qss");
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


```python
import sys
import qdarkgraystyle
from PySide import QtGui


# create the application and the main window
app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()

# setup stylesheet
app.setStyleSheet(qdarkgraystyle.load_stylesheet())

# run
window.show()
app.exec_()
```

To use PyQt4 instead of PySide, you just need to replace

```python
app.setStyleSheet(qdarkgraystyle.load_stylesheet())
```

by

```python
app.setStyleSheet(qdarkgraystyle.load_stylesheet(pyside=False))
```

and
```python
from PySide import QtGui
```

by

```python
from PyQt4 import QtGui
```

To use PyQt5, you need to use `load_stylesheet_pyqt5` instead of
`load_stylesheet`.

_There is an example included in the *example* folder.
You can run the script without installing `qdarkgraystyle`. You only need to have
PySide (or PyQt4 or PyQt5) installed on your system._

Contribute
==========

- Issue Tracker: https://github.com/mstuttgart/qdarkgray-stylesheet/issues
- Source Code: https://github.com/mstuttgart/qdarkgray-stylesheet

Snapshots
=========

Here are a few snapshots:

.. image:: screenshots/screen-01.png
    :target: https://github.com/mstuttgart/qdarkgray-stylesheet/screenshots/screen-01.png

.. image:: screenshots/screen-02.png
    :target: https://github.com/mstuttgart/qdarkgray-stylesheet/screenshots/screen-02.png

.. image:: screenshots/screen-03.png
    :target: https://github.com/mstuttgart/qdarkgray-stylesheet/screenshots/screen-03.png

Credits
=======
This package is totally based on `QDarkStyleSheet <https://github.com/ColinDuquesnoy/QDarkStyleSheet>`_ theme created by `Colin Duquesnoy <https://github.com/ColinDuquesnoy>`_.

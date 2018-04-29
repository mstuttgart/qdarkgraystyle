#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
QDarkGreyStyle is a dark gray stylesheet for python qt applications
"""
import os
import sys
from setuptools import setup, find_packages
from qdarkgraystyle import __version__

if sys.argv[-1] == 'publish':
    os.system("git tag -a %s -m 'version %s'" % (__version__,  __version__))
    os.system('git push --tags')
    os.system('python setup.py sdist bdist_wheel upload -r pypi')
    sys.exit()

setup(
    name='qdarkgraystyle',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/mstuttgart/qdarkgray-stylesheet',
    license='MIT License',
    author='Michell Stuttgart',
    author_email='michellstut@gmail.com',
    description='A dark gray stylesheet for PyQt/PySide applications',
    long_description=open('README.rst', 'r').read(),
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: X11 Applications :: Qt',
          'Environment :: Win32 (MS Windows)',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
          'Operating System :: MacOS',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries :: Application '
          'Frameworks',
    ],
)

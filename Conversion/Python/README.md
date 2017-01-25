Scripts for dealing with eagle files
===============

The general goal is to pull out descriptions and PROD_ID fields form the eagle libs and modify the KiCad libs to contain them.

Contents:

* EagleLibInfo.py -- This program deals with testing detection of certain elements from the libraries (read-only on the libs)

*note: update pip and install lxml of the right version, such as lxml-3.7.2-cp27-cp27m-win32.whl*
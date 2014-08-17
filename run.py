#!/usr/bin/python
# -*- coding: utf-8 -*-
import gui, sys
from PySide        import QtGui, QtCore
from PySide.QtGui  import QApplication, QLineEdit
from PySide.QtCore import QSettings, Qt


import h5py.h5ac
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = gui.Ui_MainWindow()
    main_win.show()
    app.exec_()
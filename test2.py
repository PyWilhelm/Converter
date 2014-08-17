##############################################################################
#
# A simple example of some of the features of the XlsxWriter Python module.
#
# Copyright 2013-2014, John McNamara, jmcnamara@cpan.org
#
from gui.gui_design import Ui_Dialog
import sys
from PyQt4 import QtCore, QtGui
app = QtGui.QApplication(sys.argv)
win = Ui_Dialog()
win_ = QtGui.QMainWindow()
win.setupUi(win_)
win.retranslateUi(win_)
win_.show()
sys.exit(app.exec_())
##############################################################################
#
# A simple example of some of the features of the XlsxWriter Python module.
#
# Copyright 2013-2014, John McNamara, jmcnamara@cpan.org
#
from gui.templateGUI import Ui_Dialog
import sys
from PyQt4 import QtCore, QtGui
app = QtGui.QApplication(sys.argv)
win = Ui_Dialog()
win.show()
sys.exit(app.exec_())
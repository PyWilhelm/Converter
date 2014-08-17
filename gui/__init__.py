# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Aug 17 21:28:43 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PySide        import QtGui, QtCore
from PySide.QtGui  import QApplication, QLineEdit
from PySide.QtCore import QSettings, Qt
from gui import converterGUI, templateGUI

def _fromUtf8(s):
    return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi()
        self.retranslateUi()
        
    def setupUi(self):
        self.setObjectName(_fromUtf8("MainWindow"))
        self.setFixedSize(444, 347)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.converter_btn = OpenDialogButton(self.centralwidget, 'converter')
        self.converter_btn.setGeometry(QtCore.QRect(90, 60, 261, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Heading"))
        font.setPointSize(20)
        self.converter_btn.setFont(font)
        self.converter_btn.setObjectName(_fromUtf8("converter_btn"))
        self.tempalte_btn = OpenDialogButton(self.centralwidget, 'template')
        self.tempalte_btn.setGeometry(QtCore.QRect(90, 180, 261, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Heading"))
        font.setPointSize(20)
        self.tempalte_btn.setFont(font)
        self.tempalte_btn.setObjectName(_fromUtf8("tempalte_btn"))
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("MainWindow", "Converter Tools", None))
        self.converter_btn.setText(_translate("MainWindow", "Cycle Converter", None))
        self.tempalte_btn.setText(_translate("MainWindow", "Template Maker", None))

class OpenDialogButton(QtGui.QPushButton):
    def __init__(self, parent, dialog_type):
        super(OpenDialogButton, self).__init__(parent)
        self.type = dialog_type
        
    def mousePressEvent(self, event):
        if self.type == 'converter':
            print 'converter'
            dialog = converterGUI.Ui_Dialog()
            dialog.setModal(True)
            dialog.show()
            dialog.exec_()
        elif self.type == 'template':
            dialog = templateGUI.Ui_Dialog()
            dialog.show()
            dialog.exec_()
            dialog.exec_()
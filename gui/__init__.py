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
        self.setFixedSize(440, 400)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.converter_btn = OpenDialogButton(self.centralwidget, 'converter')
        self.converter_btn.setGeometry(QtCore.QRect(90, 60, 260, 90))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Heading"))
        font.setPointSize(20)
        self.converter_btn.setFont(font)
        self.converter_btn.setObjectName(_fromUtf8("converter_btn")) 
        self.tempalte_btn = OpenDialogButton(self.centralwidget, 'template')
        self.tempalte_btn.setGeometry(QtCore.QRect(90, 180, 260, 90))
        self.tempalte_btn.setFont(font)
        self.tempalte_btn.setObjectName(_fromUtf8("tempalte_btn"))
        self.exit_btn = OpenDialogButton(self.centralwidget, 'exit')
        self.exit_btn.setGeometry(QtCore.QRect(220, 300, 130, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Heading"))
        font.setPointSize(15)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName(_fromUtf8("tempalte_btn"))
        
        self.setCentralWidget(self.centralwidget)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("MainWindow", "Converter Tools", None))
        self.converter_btn.setText(_translate("MainWindow", "Cycle Converter", None))
        self.tempalte_btn.setText(_translate("MainWindow", "Template Maker", None))
        self.exit_btn.setText(_translate("MainWindow", "EXIT", None))

class OpenDialogButton(QtGui.QPushButton):
    def __init__(self, parent, dialog_type):
        super(OpenDialogButton, self).__init__(parent)
        self.type = dialog_type
        #self.setStyleSheet('border-radius:10px;color:black;border-style:inset;border-width: 2px;')
        self.setStyleSheet('QPushButton{border-radius:10px;color:black;border-style:inset;border:2px gray;border-style: outset;}\
                            QPushButton:hover{background-color:white; color: black;}\
                            QPushButton:pressed{border-style:inset;}')
        
    def mouseReleaseEvent(self, event):
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
        elif self.type == 'exit':
            exit(0)
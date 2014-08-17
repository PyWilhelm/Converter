# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sun Aug 17 00:55:34 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(699, 537)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 641, 511))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.converter = QtGui.QWidget()
        self.converter.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.converter.setObjectName(_fromUtf8("converter"))
        self.label = QtGui.QLabel(self.converter)
        self.label.setGeometry(QtCore.QRect(30, 40, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.converter)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.converter)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.inputfile_input = QtGui.QLineEdit(self.converter)
        self.inputfile_input.setGeometry(QtCore.QRect(140, 40, 331, 20))
        self.inputfile_input.setObjectName(_fromUtf8("inputfile_input"))
        self.format = QtGui.QComboBox(self.converter)
        self.format.setGeometry(QtCore.QRect(140, 140, 141, 22))
        self.format.setObjectName(_fromUtf8("format"))
        self.outputfile_input = QtGui.QLineEdit(self.converter)
        self.outputfile_input.setGeometry(QtCore.QRect(140, 190, 331, 20))
        self.outputfile_input.setObjectName(_fromUtf8("outputfile_input"))
        self.inputfile_btn = OpenFileButton(self.converter, self.inputfile_input)
        self.inputfile_btn.setGeometry(QtCore.QRect(500, 40, 51, 18))
        self.inputfile_btn.setObjectName(_fromUtf8("inputfile_btn"))
        self.outputfile_btn = QtGui.QToolButton(self.converter)
        self.outputfile_btn.setGeometry(QtCore.QRect(500, 190, 51, 18))
        self.outputfile_btn.setObjectName(_fromUtf8("outputfile_btn"))
        self.label_4 = QtGui.QLabel(self.converter)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.schemafile_input = QtGui.QLineEdit(self.converter)
        self.schemafile_input.setGeometry(QtCore.QRect(140, 90, 331, 20))
        self.schemafile_input.setObjectName(_fromUtf8("schemafile_input"))
        self.schemafile_btn = QtGui.QToolButton(self.converter)
        self.schemafile_btn.setGeometry(QtCore.QRect(500, 90, 51, 18))
        self.schemafile_btn.setObjectName(_fromUtf8("schemafile_btn"))
        self.scrollArea = QtGui.QScrollArea(self.converter)
        self.scrollArea.setGeometry(QtCore.QRect(40, 290, 551, 171))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 549, 169))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.buttonBox = QtGui.QDialogButtonBox(self.converter)
        self.buttonBox.setGeometry(QtCore.QRect(190, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget.addTab(self.converter, _fromUtf8(""))
        self.templategen = QtGui.QWidget()
        self.templategen.setObjectName(_fromUtf8("templategen"))
        self.label_5 = QtGui.QLabel(self.templategen)
        self.label_5.setGeometry(QtCore.QRect(40, 140, 91, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.scrollArea_2 = QtGui.QScrollArea(self.templategen)
        self.scrollArea_2.setGeometry(QtCore.QRect(50, 240, 551, 171))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 549, 169))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_6 = QtGui.QLabel(self.templategen)
        self.label_6.setGeometry(QtCore.QRect(40, 40, 81, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.schemafile_input2 = QtGui.QLineEdit(self.templategen)
        self.schemafile_input2.setGeometry(QtCore.QRect(150, 40, 331, 20))
        self.schemafile_input2.setObjectName(_fromUtf8("schemafile_input2"))
        self.outputfile_input2 = QtGui.QLineEdit(self.templategen)
        self.outputfile_input2.setGeometry(QtCore.QRect(150, 140, 331, 20))
        self.outputfile_input2.setObjectName(_fromUtf8("outputfile_input2"))
        self.label_7 = QtGui.QLabel(self.templategen)
        self.label_7.setGeometry(QtCore.QRect(40, 90, 91, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.schemafile_btn2 = QtGui.QToolButton(self.templategen)
        self.schemafile_btn2.setGeometry(QtCore.QRect(520, 40, 51, 18))
        self.schemafile_btn2.setObjectName(_fromUtf8("schemafile_btn2"))
        self.buttonBox_2 = QtGui.QDialogButtonBox(self.templategen)
        self.buttonBox_2.setGeometry(QtCore.QRect(220, 190, 341, 32))
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName(_fromUtf8("buttonBox_2"))
        self.format2 = QtGui.QComboBox(self.templategen)
        self.format2.setGeometry(QtCore.QRect(150, 90, 141, 22))
        self.format2.setObjectName(_fromUtf8("format2"))
        self.outputfile_btn2 = QtGui.QToolButton(self.templategen)
        self.outputfile_btn2.setGeometry(QtCore.QRect(520, 140, 51, 18))
        self.outputfile_btn2.setObjectName(_fromUtf8("outputfile_btn2"))
        self.tabWidget.addTab(self.templategen, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "input file", None))
        self.label_2.setText(_translate("Dialog", "target format", None))
        self.label_3.setText(_translate("Dialog", "output file", None))
        self.inputfile_btn.setText(_translate("Dialog", "...", None))
        self.outputfile_btn.setText(_translate("Dialog", "...", None))
        self.label_4.setText(_translate("Dialog", "schema file", None))
        self.schemafile_btn.setText(_translate("Dialog", "...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.converter), _translate("Dialog", "Converter", None))
        self.label_5.setText(_translate("Dialog", "output file", None))
        self.label_6.setText(_translate("Dialog", "schema file", None))
        self.label_7.setText(_translate("Dialog", "target format", None))
        self.schemafile_btn2.setText(_translate("Dialog", "...", None))
        self.outputfile_btn2.setText(_translate("Dialog", "...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.templategen), _translate("Dialog", "Template Generator", None))

class OpenFileButton(QtGui.QToolButton):
    def __init__(self, parent=None, binding=None):
        super(OpenFileButton,self).__init__(parent)
        self.binding = binding
        
    def mousePressEvent(self,event):
        if event.button() == QtCore.Qt.LeftButton:
            filename = QtGui.QFileDialog.getOpenFileName(self, 'Open input file')
            if self.binding != None:
                self.binding.setText(filename)

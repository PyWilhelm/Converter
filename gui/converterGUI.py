# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sun Aug 17 00:55:34 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!
import os, multiprocessing, converter, subprocess
from PySide        import QtGui, QtCore
from PySide.QtGui  import QApplication, QLineEdit
from PySide.QtCore import QSettings, Qt
from PySide import QtWebKit

def _fromUtf8(s):
    return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(QtGui.QWizard):
    
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.font = QtGui.QFont()
        self.font.setFamily(_fromUtf8("Sitka Heading"))
        self.font.setPointSize(13)
        self.font_text = QtGui.QFont()
        self.font_text.setFamily(_fromUtf8("Sitka Heading"))
        self.font_text.setPointSize(11)
        self.setFont(self.font)
        self.queue = multiprocessing.Queue()
        self.page1 = QtGui.QWizardPage(self)
        self.page2 = QtGui.QWizardPage(self)
        #self.setButtonLayout([QtGui.QWizard.BackButton, QtGui.QWizard.NextButton, 
        #                      QtGui.QWizard.FinishButton, QtGui.QWizard.CancelButton])
        self.setupUi()
        self.retranslateUi()
        
    def validateCurrentPage(self):
        error_message = ''
        input_path = str(self.input_el.text())
        schema_path = str(self.schema_el.text())
        output_path = str(self.output_el.text())
        if input_path == '':
            error_message += 'input file not given<p>'
        if schema_path == '':
            error_message += 'schema file not given<p>'
        if output_path == '':
            error_message += 'output file not given<p>'
        if os.path.exists(input_path) == False:
            error_message += 'input file not existed<p>'
        if os.path.exists(schema_path) == False:
            error_message += 'schema file not existed<p>'
        if error_message != '':
            mb = QtGui.QMessageBox(QtGui.QMessageBox.Critical, 'Error', '<font size=5 color=red > %s </font>' %error_message, 
                              buttons=QtGui.QMessageBox.Ok)
            mb.show()
            mb.exec_()
            return False
        else:
            syn, sem = converter.converter_file(self.queue, input_path, schema_path, output_path)
            self.viewer.setContent((str(syn) + str(sem)).replace('ä', '&auml;'))
            return True
        
    def setupUi(self):
        self.setObjectName(_fromUtf8("Dialog"))
        self.setFixedSize(800, 600)
        
        
        self.gridLayoutWidget = QtGui.QWidget(self.page1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 70, 550, 350))
        font = self.font
        font_text = self.font_text
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        #self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        
        self.schema_el = QtGui.QLineEdit(self.gridLayoutWidget)
        self.schema_el.setFont(font_text)
        self.schema_el.setObjectName(_fromUtf8("schema_el"))
        self.gridLayout.addWidget(self.schema_el, 1, 2, 1, 1)
        
        self.schema_btn = OpenFileButton(self.gridLayoutWidget,self.schema_el, True)
        self.schema_btn.setFont(font)
        self.schema_btn.setObjectName(_fromUtf8("schema_btn"))
        self.gridLayout.addWidget(self.schema_btn, 1, 3, 1, 1)

        self.input_el = QtGui.QLineEdit(self.gridLayoutWidget)
        self.input_el.setFont(font_text)
        self.input_el.setObjectName(_fromUtf8("input_el"))
        self.gridLayout.addWidget(self.input_el, 0, 2, 1, 1)
        
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        self.input_btn = OpenFileButton(self.gridLayoutWidget, self.input_el)
        self.input_btn.setFont(font)
        self.input_btn.setObjectName(_fromUtf8("input_btn"))
        self.gridLayout.addWidget(self.input_btn, 0, 3, 1, 1)
        

        
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        
        self.output_el = QtGui.QLineEdit(self.gridLayoutWidget)
        self.output_el.setFont(font_text)
        self.output_el.setObjectName(_fromUtf8("output_el"))
        self.gridLayout.addWidget(self.output_el, 3, 2, 1, 1)
        
        self.format_cb = SelectCB(self.gridLayoutWidget, self.output_el)
        self.format_cb.setFont(font)
        self.format_cb.setObjectName(_fromUtf8("format_cb"))
        self.format_cb.addItems(['XLSX (*.xlsx)', 'XLS (*.xls)', 'Mat (*.mat)', 'SDF (*.sdf)'])
        self.gridLayout.addWidget(self.format_cb, 2, 2, 1, 1)
        
        self.output_btn = SaveFileButton(self.gridLayoutWidget, self.output_el, self.format_cb)
        self.output_btn.setFont(font)
        self.output_btn.setObjectName(_fromUtf8("output_btn"))
        self.gridLayout.addWidget(self.output_btn, 3, 3, 1, 1)
        

        
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.addPage(self.page1)
        
        
        self.gridLayoutWidget2 = QtGui.QWidget(self.page2)
        self.gridLayoutWidget2.setGeometry(QtCore.QRect(90, 70, 550, 350))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Heading"))
        font.setPointSize(11)
        self.gridLayoutWidget2.setFont(font)
        self.gridLayoutWidget2.setObjectName(_fromUtf8("gridLayoutWidget2"))
        self.gridLayout2 = QtGui.QGridLayout(self.gridLayoutWidget2)
        #self.gridLayout2.setMargin(0)
        self.gridLayout2.setObjectName(_fromUtf8("gridLayout2"))
        
        self.label_info = QtGui.QLabel(self.gridLayoutWidget2)
        self.label_info.setFont(font)
        self.label_info.setObjectName(_fromUtf8("label_info"))
        self.gridLayout2.addWidget(self.label_info, 0, 0, 1, 1)
        
        self.viewer = QtWebKit.QWebView(self.gridLayoutWidget2)
        self.viewer.setFont(font)
        self.viewer.setObjectName(_fromUtf8("viewer"))
        self.gridLayout2.addWidget(self.viewer, 1, 0, 1, 1)
        
        self.openfolder_btn = OpenExplorerButton(self.gridLayoutWidget2, self.output_el)
        self.openfolder_btn.setFont(font)
        self.openfolder_btn.setObjectName(_fromUtf8("openfolder_btn"))
        self.gridLayout2.addWidget(self.openfolder_btn, 2, 0, 1, 1)
        
        
        self.addPage(self.page2)
        self.retranslateUi()
    
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("MainWindow", "Cycle Converter", None))
        self.schema_btn.setText(_translate("MainWindow", "...", None))
        self.label.setText(_translate("MainWindow", "Input File", None))
        self.input_btn.setText(_translate("MainWindow", "...", None))
        self.label_3.setText(_translate("MainWindow", "Target Format", None))
        self.label_4.setText(_translate("MainWindow", "Output File", None))
        self.output_btn.setText(_translate("MainWindow", "...", None))
        self.label_2.setText(_translate("MainWindow", "Schema File", None))
        self.label_info.setText(_translate("MainWindow", "Convert Information: ", None))
    

class OpenFileButton(QtGui.QToolButton):
    def __init__(self, parent, binding, schema=False):
        super(OpenFileButton,self).__init__(parent)
        self.binding = binding
        self.schema = schema
        
    def mousePressEvent(self,event):
        if event.button() == QtCore.Qt.LeftButton:
            filter = 'XLSX (*.xlsx);;XLS (*.xls);;Mat (*.mat);;SDF (*.sdf)' if not self.schema else 'SDF (*.sdf)'
            filename = QtGui.QFileDialog.getOpenFileName(self, 'Open input file', 
                                                         filter=filter)
            if self.binding != None:
                self.binding.setText(filename[0])
                
class SaveFileButton(QtGui.QToolButton):
    def __init__(self, parent, binding, format_controller):
        super(SaveFileButton,self).__init__(parent)
        self.binding = binding
        self.format_controller = format_controller
        
        
    def mousePressEvent(self,event):
        if event.button() == QtCore.Qt.LeftButton:
            filter = self.format_controller.currentText()
            if filter not in ['Mat (*.mat)','SDF (*.sdf)','XLSX (*.xlsx)','XLS (*.xls)']:
                QtGui.QErrorMessage()
            filename = QtGui.QFileDialog.getSaveFileName(self, 'Save file as...', filter=filter)
            if self.binding != None:
                self.binding.setText(filename[0])
                
class OpenExplorerButton(QtGui.QPushButton):
    def __init__(self, parent, binding):
        super(OpenExplorerButton, self).__init__(parent)
        self.binding = binding
        self.setText('Open Output Folder')
        
    def mousePressEvent(self, event):
        folder = os.path.dirname(str(self.binding.text()))
        folder = folder.replace('/', os.sep)
        print 'explorer "%s"' % folder
        os.popen(r'explorer "%s"' %folder)
        
class SelectCB(QtGui.QComboBox):
    def __init__(self, parent, binding):
        super(SelectCB, self).__init__(parent)
        self.index = -1
        self.binding = binding
        self.currentIndexChanged.connect(self.run)

    def run(self, *args, **kwargs):
        if self.index != self.currentIndex():
            self.binding.setText('')

        




    
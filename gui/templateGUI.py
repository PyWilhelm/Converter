# -*- coding: utf-8 -*-

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
        self.pages = []
        #self.pages.append(QtGui.QWizardPage(self))
        #self.setButtonLayout([QtGui.QWizard.BackButton, QtGui.QWizard.NextButton, 
        #                      QtGui.QWizard.FinishButton, QtGui.QWizard.CancelButton])
        self.setupUi()
        self.retranslateUi()
        
    def validateCurrentPage(self):
        error_message = ''
        schema_path = str(self.schema_el.text())
        output_path = str(self.output_el.text())
        if schema_path == '':
            error_message += 'schema file not given<p>'
        if output_path == '':
            error_message += 'output file not given<p>'
        if schema_path != '' and os.path.exists(schema_path) == False:
            error_message += 'schema file not existed<p>'
        if error_message != '':
            mb = QtGui.QMessageBox(QtGui.QMessageBox.Critical, 'Error', '<font size=5 color=red > %s </font>' %error_message, 
                              buttons=QtGui.QMessageBox.Ok)
            mb.show()
            mb.exec_()
            return False
        else:
            print self.pages
            if self.currentId() == self.pages[0]:
                if len(self.pages) == 2:
                    final_page = self.page(self.pages[1])
                    self.removePage(self.pages[1])
                else:
                    final_page = self.page(self.pages[2])
                    self.removePage(self.pages[1])
                    self.removePage(self.pages[2])
                self.pages = self.pages[0:1]
                page = QtGui.QWizardPage(self)
                
                muster_list, sdf_ext_schema = converter.template_get_muster_list(schema_path)
                self.sdf_ext_schema = sdf_ext_schema
                formLayoutWidget = QtGui.QWidget(page)
                formLayoutWidget.setGeometry(QtCore.QRect(90, 70, 550, 350))
                formLayoutWidget.setFont(self.font)
                formLayout = QtGui.QFormLayout(formLayoutWidget)
                #formLayout.setMargin(0)
                label = QtGui.QLabel(formLayoutWidget)
                label.setFont(self.font)
                label.setText('Setting Component Number')
                formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, label)
                splitter = QtGui.QSpacerItem(288, 40, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
                formLayout.setItem(1, QtGui.QFormLayout.LabelRole, splitter)
                for i, component_name in enumerate(muster_list):
                    print component_name
                    label = QtGui.QLabel(formLayoutWidget)
                    label.setFont(self.font)
                    label.setText(component_name.upper())
                    formLayout.setWidget(2*i+2, QtGui.QFormLayout.LabelRole, label)
                    spinBox = QtGui.QSpinBox(formLayoutWidget)
                    spinBox.setMinimum(1)
                    spinBox.setMaximum(10)
                    formLayout.setWidget(2*i+2, QtGui.QFormLayout.FieldRole, spinBox)
                    
                    splitter = QtGui.QSpacerItem(288, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
                    formLayout.setItem(2*i+3, QtGui.QFormLayout.LabelRole, splitter)

                self.pages.append(self.addPage(page))
                self.pages.append(self.addPage(final_page))
                print 'end'
            elif self.currentId() == self.pages[1]:
                muster_list = []
                for c in self.page(self.currentId()).children():
                    for cc in c.children():
                        if isinstance(cc, QtGui.QSpinBox):
                            muster_list.append(cc.value())
                try:
                    converter.template_generate(self.sdf_ext_schema, str(self.output_el.text()), muster_list)
                except:
                    mb = QtGui.QMessageBox(QtGui.QMessageBox.Critical, 
                                                       'Error', 
                                                       '<font size=5 color=red > File cannot be written. Please close the File </font>', 
                                                       buttons=QtGui.QMessageBox.Ok)
                    mb.show()
                    mb.exec_()
                    return False
            return True
        
        
    def setupUi(self):
        self.setObjectName(_fromUtf8("Dialog"))
        self.setFixedSize(800, 600)
        font = self.font
        font_text = self.font_text
        page = QtGui.QWizardPage(self)
        self.centralwidget = QtGui.QWidget(page)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 70, 550, 350))

        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        #self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        
        self.schema_el = QtGui.QLineEdit(self.gridLayoutWidget)
        self.schema_el.setFont(font_text)
        self.schema_el.setObjectName(_fromUtf8("schema_el"))
        self.gridLayout.addWidget(self.schema_el, 0, 2, 1, 1)
        
        self.schema_btn = OpenFileButton(self.gridLayoutWidget,self.schema_el, True)
        self.schema_btn.setFont(font)
        self.schema_btn.setObjectName(_fromUtf8("schema_btn"))
        self.gridLayout.addWidget(self.schema_btn, 0, 3, 1, 1)
        
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        
        self.output_el = QtGui.QLineEdit(self.gridLayoutWidget)
        self.output_el.setFont(font_text)
        self.output_el.setObjectName(_fromUtf8("output_el"))
        self.gridLayout.addWidget(self.output_el, 2, 2, 1, 1)
        
        self.format_cb = SelectCB(self.gridLayoutWidget, self.output_el)
        self.format_cb.setFont(font)
        self.format_cb.setObjectName(_fromUtf8("format_cb"))
        self.format_cb.addItems(['XLSX (*.xlsx)', 'XLS (*.xls)', 'Mat (*.mat)', 'SDF (*.sdf)'])
        self.gridLayout.addWidget(self.format_cb, 1, 2, 1, 1)
        
        self.output_btn = SaveFileButton(self.gridLayoutWidget, self.output_el, self.format_cb)
        self.output_btn.setFont(font)
        self.output_btn.setObjectName(_fromUtf8("output_btn"))
        self.gridLayout.addWidget(self.output_btn, 2, 3, 1, 1)
        

        
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        
        self.pages.append(self.addPage(page))
        
        page = QtGui.QWizardPage(self)
        self.centralwidget2 = QtGui.QWidget(page)
        self.centralwidget2.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget2 = QtGui.QWidget(self.centralwidget2)
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
        
        
        self.pages.append(self.addPage(page))
        self.retranslateUi()
    
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("MainWindow", "Template Maker", None))
        self.schema_btn.setText(_translate("MainWindow", "...", None))
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
            print filename
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
            print filename
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
        print 'explorer /select "%s"' % folder
        os.popen(r'explorer "%s"' %folder)
        
class SelectCB(QtGui.QComboBox):
    def __init__(self, parent, binding):
        super(SelectCB, self).__init__(parent)
        self.index = -1
        self.binding = binding
        self.currentIndexChanged.connect(self.run)

    def run(self, *args, **kwargs):
        print 'currentIndexChanged', self.currentIndex()
        if self.index != self.currentIndex():
            self.binding.setText('')

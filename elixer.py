# Creator Kiran.R
# Project Code Elixer
import os
from FileManager import *
from Gloable import *
from modules.constants import *
from modules.functions import *
from modules.loops import *
from modules.variable import *
from PyQt4 import QtCore, QtGui

class moduleMix:
    class_gloable = ""
    class_ui = ""
    class_filemgr = ""
    class_const = ""
    class_function = ""
    class_loops = ""
    class_variable = ""


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

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(1200, 640)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMaximumSize(QtCore.QSize(1200, 640))
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 81, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 81, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Load = QtGui.QPushButton(self.centralwidget)
        self.Load.setGeometry(QtCore.QRect(580, 0, 61, 41))
        self.Load.setObjectName(_fromUtf8("Load"))
        self.FilePath = QtGui.QLabel(self.centralwidget)
        self.FilePath.setGeometry(QtCore.QRect(100, 0, 411, 17))
        self.FilePath.setObjectName(_fromUtf8("FilePath"))
        self.FolderPath = QtGui.QLabel(self.centralwidget)
        self.FolderPath.setGeometry(QtCore.QRect(100, 20, 431, 17))
        self.FolderPath.setObjectName(_fromUtf8("FolderPath"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 60, 81, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 40, 671, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.VarUsedCombo = QtGui.QComboBox(self.centralwidget)
        self.VarUsedCombo.setGeometry(QtCore.QRect(80, 80, 131, 25))
        self.VarUsedCombo.setObjectName(_fromUtf8("VarUsedCombo"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(223, 50, 20, 171))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 61, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 170, 51, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 80, 51, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.VarUnusedCombo = QtGui.QComboBox(self.centralwidget)
        self.VarUnusedCombo.setGeometry(QtCore.QRect(80, 110, 131, 25))
        self.VarUnusedCombo.setObjectName(_fromUtf8("VarUnusedCombo"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 110, 121, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.VarMemory = QtGui.QLineEdit(self.centralwidget)
        self.VarMemory.setGeometry(QtCore.QRect(80, 140, 131, 21))
        self.VarMemory.setObjectName(_fromUtf8("VarMemory"))
        self.VarCount = QtGui.QLineEdit(self.centralwidget)
        self.VarCount.setGeometry(QtCore.QRect(80, 170, 131, 21))
        self.VarCount.setObjectName(_fromUtf8("VarCount"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(300, 60, 81, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(440, 50, 20, 171))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(-10, 210, 671, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.FunctionCombo = QtGui.QComboBox(self.centralwidget)
        self.FunctionCombo.setGeometry(QtCore.QRect(250, 80, 191, 25))
        self.FunctionCombo.setObjectName(_fromUtf8("FunctionCombo"))
        self.FunctionCalls = QtGui.QLineEdit(self.centralwidget)
        self.FunctionCalls.setGeometry(QtCore.QRect(310, 110, 131, 21))
        self.FunctionCalls.setObjectName(_fromUtf8("FunctionCalls"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(250, 110, 51, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.RecursiveCalls = QtGui.QLineEdit(self.centralwidget)
        self.RecursiveCalls.setGeometry(QtCore.QRect(320, 140, 121, 21))
        self.RecursiveCalls.setObjectName(_fromUtf8("RecursiveCalls"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(250, 140, 71, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(510, 60, 81, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.ConstantMemory = QtGui.QLineEdit(self.centralwidget)
        self.ConstantMemory.setGeometry(QtCore.QRect(520, 180, 101, 21))
        self.ConstantMemory.setObjectName(_fromUtf8("ConstantMemory"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(460, 180, 71, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(260, 230, 121, 20))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(-20, 480, 681, 20))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(40, 500, 141, 20))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.TotalMemory = QtGui.QLineEdit(self.centralwidget)
        self.TotalMemory.setGeometry(QtCore.QRect(180, 500, 131, 21))
        self.TotalMemory.setObjectName(_fromUtf8("TotalMemory"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(40, 530, 141, 20))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.TotalCallsMade = QtGui.QLineEdit(self.centralwidget)
        self.TotalCallsMade.setGeometry(QtCore.QRect(180, 530, 131, 21))
        self.TotalCallsMade.setObjectName(_fromUtf8("TotalCallsMade"))
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(340, 500, 141, 20))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.Rating = QtGui.QLineEdit(self.centralwidget)
        self.Rating.setGeometry(QtCore.QRect(460, 500, 131, 21))
        self.Rating.setObjectName(_fromUtf8("Rating"))
        self.label_19 = QtGui.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(340, 530, 141, 20))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.TimeComplex = QtGui.QLineEdit(self.centralwidget)
        self.TimeComplex.setGeometry(QtCore.QRect(460, 530, 131, 21))
        self.TimeComplex.setInputMask(_fromUtf8(""))
        self.TimeComplex.setObjectName(_fromUtf8("TimeComplex"))
        self.ConstantView = QtGui.QListWidget(self.centralwidget)
        self.ConstantView.setGeometry(QtCore.QRect(460, 80, 171, 91))
        self.ConstantView.setObjectName(_fromUtf8("ConstantView"))
        self.ComplexView = QtGui.QListWidget(self.centralwidget)
        self.ComplexView.setGeometry(QtCore.QRect(10, 260, 621, 221))
        self.ComplexView.setObjectName(_fromUtf8("ComplexView"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(650, 0, 20, 671))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(680, 10, 81, 17))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.Terminal = QtGui.QListWidget(self.centralwidget)
        self.Terminal.setGeometry(QtCore.QRect(680, 40, 511, 551))
        self.Terminal.setObjectName(_fromUtf8("Terminal"))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.actionProgram_file = QtGui.QAction(mainWindow)
        self.actionProgram_file.setObjectName(_fromUtf8("actionProgram_file"))
        self.actionProgram_folder = QtGui.QAction(mainWindow)
        self.actionProgram_folder.setObjectName(_fromUtf8("actionProgram_folder"))
        self.menuFile.addAction(self.actionProgram_file)
        self.menuFile.addAction(self.actionProgram_folder)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Code Elixer", None))
        self.label.setText(_translate("mainWindow", "File : ", None))
        self.label_2.setText(_translate("mainWindow", "folder : ", None))
        self.Load.setText(_translate("mainWindow", "Load", None))
        self.FilePath.setText(_translate("mainWindow", "<content>", None))
        self.FolderPath.setText(_translate("mainWindow", "<content>", None))
        self.label_5.setText(_translate("mainWindow", "Variables", None))
        self.label_6.setText(_translate("mainWindow", "Memory", None))
        self.label_7.setText(_translate("mainWindow", "Count", None))
        self.label_8.setText(_translate("mainWindow", "Used", None))
        self.label_9.setText(_translate("mainWindow", "Unused", None))
        self.label_10.setText(_translate("mainWindow", "Functions", None))
        self.label_11.setText(_translate("mainWindow", "Calls", None))
        self.label_12.setText(_translate("mainWindow", "Recursive", None))
        self.label_13.setText(_translate("mainWindow", "Constants", None))
        self.label_14.setText(_translate("mainWindow", "Memory", None))
        self.label_15.setText(_translate("mainWindow", "Complexity Tree", None))
        self.label_16.setText(_translate("mainWindow", "Total Memory Used", None))
        self.label_17.setText(_translate("mainWindow", "Total Calls Made", None))
        self.label_18.setText(_translate("mainWindow", "Rating", None))
        self.label_19.setText(_translate("mainWindow", "Time Complexity ", None))
        self.label_20.setText(_translate("mainWindow", "Terminal", None))
        self.menuFile.setTitle(_translate("mainWindow", "file", None))
        self.actionProgram_file.setText(_translate("mainWindow", "program file", None))
        self.actionProgram_folder.setText(_translate("mainWindow", "program folder", None))


    def Load_clicked(self):
        print("clicked")

    def printTerminal(self,value):
        ui.Terminal.addItem(value)

def printTerminal(module,value):
    module.class_ui.Terminal.addItem(value)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    module = moduleMix()
    module.class_ui = ui
    module = setupGloable(module)
    module.class_ui.FolderPath.setText("/home/ghostranger/code-elixer/")
    #module.class_ui.FilePath.setText("/home/ghostranger/code-elixer/modules/constants.py")
    module.class_ui.TimeComplex.setText("O(N^2)")
    #manditory
    module = setupFilmanager(module)
    module = setupVariable(module)
    module = setupLoops(module)
    module = setupConst(module)
    module = setupFunction(module)
    #write the code here----------------------------------------------------
    for i in module.class_const.cconst.const_used:
        module.class_ui.ConstantView.addItem(str(i))
    module.class_ui.ConstantMemory.setText(str(module.class_const.cconst.const_memory)+" Byte")
    #write the code above--------------------------------------------------
    sys.exit(app.exec_())

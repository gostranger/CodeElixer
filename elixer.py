# Creator Kiran.R
# Project Code Elixer
import os
import sys
from FileManager import *
from Gloable import *
from modules.constants import *
from modules.functions import *
from modules.loops import *
from modules.variable import *
from modules.db import *
from modules.savemgr import *
from PyQt4.QtGui import QFileDialog
from PyQt4 import QtCore, QtGui
sys.path.append("/usr/lib/python2.7/dist-packages/PyQt4/bin/")
class moduleClass:
    filemgr = ""
    constant = ""
    functions = ""
    loops = ""
    variable = ""
    gloable = ""
    db = ""
    save = ""



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

class leaderboard(QtGui.QDialog):
    def __init__(self, parent=None):
        super(leaderboard, self).__init__(parent)
        self.setObjectName(_fromUtf8("leaderboardWindow"))
        self.resize(700, 600)
        self.setWindowTitle(_translate("mainWindow", "Code Elixer L", None))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(700, 500))
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        #self.buttonBox = QtGui.QDialogButtonBox(self)
        #self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        #self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.LeadView = QtGui.QListWidget(self.centralwidget)
        self.LeadView.setGeometry(QtCore.QRect(10, 260, 621, 221))
        self.LeadView.setObjectName(_fromUtf8("leaderView"))
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.LeadView)
        #self.verticalLayout.addWidget(self.buttonBox)


class Ui_mainWindow(object):

    class ui:
        module = ""
        label = ""
        label_2= ""
        Load= ""
        FilePath= ""
        FolderPath= ""
        label_5= ""
        label_6= ""
        label_7= ""
        label_8= ""
        label_9= ""
        label_10= ""
        label_11= ""
        label_12= ""
        label_13= ""
        label_14= ""
        label_15= ""
        label_16= ""
        label_17= ""
        label_18= ""
        label_19= ""
        label_20= ""
        menuFile= ""
        fileName= ""
        actionProgram_file= ""
        actionProgram_folder= ""
        lb = ""

    def __init__(self):
        self.ui.module = moduleClass()
        self.ui.module.filemgr = setupFilmanager()
        self.ui.module.constant = setupConst()
        self.ui.module.functions = setupFunction()
        self.ui.module.loops = setupLoops()
        self.ui.module.variable = setupVariable()
        self.ui.module.gloable = setupGloable()
        self.ui.module.db = setupDB()
        self.ui.module.save = setupsave()
        self.ui.lb = leaderboard()
        self.ui.lb.LeadView.clear()
        self.ui = CheckDB(self.ui)
        self.ui = getboard(self.ui)
        self.ui = self.ui.module.save.rowobjs(self.ui)
        self.ui.lb.LeadView.addItem("|id\t|var\t|const\t|fun\t|memory\t|loc\t|calls\t|")
        for i in range(len(self.ui.module.save.projs)):
            self.ui.lb.LeadView.addItem("|"+str(self.ui.module.save.projs[i].id)+"\t|"+str(self.ui.module.save.projs[i].var)+"\t|"+str(self.ui.module.save.projs[i].const)+"\t|"+str(self.ui.module.save.projs[i].func)+"\t|"+str(self.ui.module.save.projs[i].memory)+"\t|"+str(self.ui.module.save.projs[i].loc)+"\t|"+str(self.ui.module.save.projs[i].calls)+"\t|")



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
        self.ui.label = QtGui.QLabel(self.centralwidget)
        self.ui.label.setGeometry(QtCore.QRect(10, 0, 81, 17))
        self.ui.label.setObjectName(_fromUtf8("label"))
        self.ui.label_2 = QtGui.QLabel(self.centralwidget)
        self.ui.label_2.setGeometry(QtCore.QRect(10, 20, 81, 17))
        self.ui.label_2.setObjectName(_fromUtf8("label_2"))
        self.ui.Load = QtGui.QPushButton(self.centralwidget)
        self.ui.Load.setGeometry(QtCore.QRect(580, 0, 61, 41))
        self.ui.Load.setObjectName(_fromUtf8("Load"))
        self.ui.save = QtGui.QPushButton(self.centralwidget)
        self.ui.save.setGeometry(QtCore.QRect(580, 560, 61, 21))
        self.ui.save.setObjectName(_fromUtf8("save"))
        self.ui.FilePath = QtGui.QLabel(self.centralwidget)
        self.ui.FilePath.setGeometry(QtCore.QRect(100, 0, 411, 17))
        self.ui.FilePath.setObjectName(_fromUtf8("FilePath"))
        self.ui.FolderPath = QtGui.QLabel(self.centralwidget)
        self.ui.FolderPath.setGeometry(QtCore.QRect(100, 20, 431, 17))
        self.ui.FolderPath.setObjectName(_fromUtf8("FolderPath"))
        self.ui.label_5 = QtGui.QLabel(self.centralwidget)
        self.ui.label_5.setGeometry(QtCore.QRect(70, 60, 81, 17))
        self.ui.label_5.setObjectName(_fromUtf8("label_5"))
        self.ui.line = QtGui.QFrame(self.centralwidget)
        self.ui.line.setGeometry(QtCore.QRect(-10, 40, 671, 20))
        self.ui.line.setFrameShape(QtGui.QFrame.HLine)
        self.ui.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.ui.line.setObjectName(_fromUtf8("line"))
        self.ui.VarUsedCombo = QtGui.QComboBox(self.centralwidget)
        self.ui.VarUsedCombo.setGeometry(QtCore.QRect(80, 80, 131, 25))
        self.ui.VarUsedCombo.setObjectName(_fromUtf8("VarUsedCombo"))
        self.ui.line_2 = QtGui.QFrame(self.centralwidget)
        self.ui.line_2.setGeometry(QtCore.QRect(223, 50, 20, 171))
        self.ui.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.ui.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.ui.line_2.setObjectName(_fromUtf8("line_2"))
        self.ui.label_6 = QtGui.QLabel(self.centralwidget)
        self.ui.label_6.setGeometry(QtCore.QRect(20, 140, 61, 17))
        self.ui.label_6.setObjectName(_fromUtf8("label_6"))
        self.ui.label_7 = QtGui.QLabel(self.centralwidget)
        self.ui.label_7.setGeometry(QtCore.QRect(20, 170, 51, 17))
        self.ui.label_7.setObjectName(_fromUtf8("label_7"))
        self.ui.label_8 = QtGui.QLabel(self.centralwidget)
        self.ui.label_8.setGeometry(QtCore.QRect(20, 80, 51, 17))
        self.ui.label_8.setObjectName(_fromUtf8("label_8"))
        self.ui.VarUnusedCombo = QtGui.QComboBox(self.centralwidget)
        self.ui.VarUnusedCombo.setGeometry(QtCore.QRect(80, 110, 131, 25))
        self.ui.VarUnusedCombo.setObjectName(_fromUtf8("VarUnusedCombo"))
        self.ui.label_9 = QtGui.QLabel(self.centralwidget)
        self.ui.label_9.setGeometry(QtCore.QRect(20, 110, 121, 17))
        self.ui.label_9.setObjectName(_fromUtf8("label_9"))
        self.ui.VarMemory = QtGui.QLineEdit(self.centralwidget)
        self.ui.VarMemory.setGeometry(QtCore.QRect(80, 140, 131, 21))
        self.ui.VarMemory.setObjectName(_fromUtf8("VarMemory"))
        self.ui.VarCount = QtGui.QLineEdit(self.centralwidget)
        self.ui.VarCount.setGeometry(QtCore.QRect(80, 170, 131, 21))
        self.ui.VarCount.setObjectName(_fromUtf8("VarCount"))
        self.ui.label_10 = QtGui.QLabel(self.centralwidget)
        self.ui.label_10.setGeometry(QtCore.QRect(300, 60, 81, 17))
        self.ui.label_10.setObjectName(_fromUtf8("label_10"))
        self.ui.line_3 = QtGui.QFrame(self.centralwidget)
        self.ui.line_3.setGeometry(QtCore.QRect(440, 50, 20, 171))
        self.ui.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.ui.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.ui.line_3.setObjectName(_fromUtf8("line_3"))
        self.ui.line_4 = QtGui.QFrame(self.centralwidget)
        self.ui.line_4.setGeometry(QtCore.QRect(-10, 210, 671, 20))
        self.ui.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.ui.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.ui.line_4.setObjectName(_fromUtf8("line_4"))
        self.ui.FunctionCombo = QtGui.QComboBox(self.centralwidget)
        self.ui.FunctionCombo.setGeometry(QtCore.QRect(250, 80, 191, 25))
        self.ui.FunctionCombo.setObjectName(_fromUtf8("FunctionCombo"))
        self.ui.FunctionCalls = QtGui.QLineEdit(self.centralwidget)
        self.ui.FunctionCalls.setGeometry(QtCore.QRect(310, 110, 131, 21))
        self.ui.FunctionCalls.setObjectName(_fromUtf8("FunctionCalls"))
        self.ui.label_11 = QtGui.QLabel(self.centralwidget)
        self.ui.label_11.setGeometry(QtCore.QRect(250, 110, 51, 17))
        self.ui.label_11.setObjectName(_fromUtf8("label_11"))
        self.ui.RecursiveCalls = QtGui.QLineEdit(self.centralwidget)
        self.ui.RecursiveCalls.setGeometry(QtCore.QRect(320, 140, 121, 21))
        self.ui.RecursiveCalls.setObjectName(_fromUtf8("RecursiveCalls"))
        self.ui.label_12 = QtGui.QLabel(self.centralwidget)
        self.ui.label_12.setGeometry(QtCore.QRect(250, 140, 71, 17))
        self.ui.label_12.setObjectName(_fromUtf8("label_12"))
        self.ui.label_13 = QtGui.QLabel(self.centralwidget)
        self.ui.label_13.setGeometry(QtCore.QRect(510, 60, 81, 17))
        self.ui.label_13.setObjectName(_fromUtf8("label_13"))
        self.ui.ConstantMemory = QtGui.QLineEdit(self.centralwidget)
        self.ui.ConstantMemory.setGeometry(QtCore.QRect(520, 180, 101, 21))
        self.ui.ConstantMemory.setObjectName(_fromUtf8("ConstantMemory"))
        self.ui.label_14 = QtGui.QLabel(self.centralwidget)
        self.ui.label_14.setGeometry(QtCore.QRect(460, 180, 71, 17))
        self.ui.label_14.setObjectName(_fromUtf8("label_14"))
        self.ui.label_15 = QtGui.QLabel(self.centralwidget)
        self.ui.label_15.setGeometry(QtCore.QRect(260, 230, 121, 20))
        self.ui.label_15.setObjectName(_fromUtf8("label_15"))
        self.ui.line_5 = QtGui.QFrame(self.centralwidget)
        self.ui.line_5.setGeometry(QtCore.QRect(-20, 480, 681, 20))
        self.ui.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.ui.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.ui.line_5.setObjectName(_fromUtf8("line_5"))
        self.ui.label_16 = QtGui.QLabel(self.centralwidget)
        self.ui.label_16.setGeometry(QtCore.QRect(40, 500, 141, 20))
        self.ui.label_16.setObjectName(_fromUtf8("label_16"))
        self.ui.TotalMemory = QtGui.QLineEdit(self.centralwidget)
        self.ui.TotalMemory.setGeometry(QtCore.QRect(180, 500, 131, 21))
        self.ui.TotalMemory.setObjectName(_fromUtf8("TotalMemory"))
        self.ui.label_17 = QtGui.QLabel(self.centralwidget)
        self.ui.label_17.setGeometry(QtCore.QRect(40, 530, 141, 20))
        self.ui.label_17.setObjectName(_fromUtf8("label_17"))
        self.ui.TotalCallsMade = QtGui.QLineEdit(self.centralwidget)
        self.ui.TotalCallsMade.setGeometry(QtCore.QRect(180, 530, 131, 21))
        self.ui.TotalCallsMade.setObjectName(_fromUtf8("TotalCallsMade"))
        self.ui.label_18 = QtGui.QLabel(self.centralwidget)
        self.ui.label_18.setGeometry(QtCore.QRect(340, 500, 141, 20))
        self.ui.label_18.setObjectName(_fromUtf8("label_18"))
        self.ui.Rating = QtGui.QLineEdit(self.centralwidget)
        self.ui.Rating.setGeometry(QtCore.QRect(460, 500, 131, 21))
        self.ui.Rating.setObjectName(_fromUtf8("Rating"))
        self.ui.label_19 = QtGui.QLabel(self.centralwidget)
        self.ui.label_19.setGeometry(QtCore.QRect(340, 530, 141, 20))
        self.ui.label_19.setObjectName(_fromUtf8("label_19"))
        self.ui.TimeComplex = QtGui.QLineEdit(self.centralwidget)
        self.ui.TimeComplex.setGeometry(QtCore.QRect(460, 530, 131, 21))
        self.ui.TimeComplex.setInputMask(_fromUtf8(""))
        self.ui.TimeComplex.setObjectName(_fromUtf8("TimeComplex"))
        self.ui.label_21 = QtGui.QLabel(self.centralwidget)
        self.ui.label_21.setGeometry(QtCore.QRect(40, 560, 141, 20))
        self.ui.label_21.setObjectName(_fromUtf8("label_21"))
        self.ui.TotalLoc = QtGui.QLineEdit(self.centralwidget)
        self.ui.TotalLoc.setGeometry(QtCore.QRect(180, 560, 131, 21))
        self.ui.TotalLoc.setObjectName(_fromUtf8("TotalLoc"))
        self.ui.ConstantView = QtGui.QListWidget(self.centralwidget)
        self.ui.ConstantView.setGeometry(QtCore.QRect(460, 80, 171, 91))
        self.ui.ConstantView.setObjectName(_fromUtf8("ConstantView"))
        self.ui.ComplexView = QtGui.QListWidget(self.centralwidget)
        self.ui.ComplexView.setGeometry(QtCore.QRect(10, 260, 621, 221))
        self.ui.ComplexView.setObjectName(_fromUtf8("ComplexView"))
        self.ui.line_6 = QtGui.QFrame(self.centralwidget)
        self.ui.line_6.setGeometry(QtCore.QRect(650, 0, 20, 671))
        self.ui.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.ui.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.ui.line_6.setObjectName(_fromUtf8("line_6"))
        self.ui.label_20 = QtGui.QLabel(self.centralwidget)
        self.ui.label_20.setGeometry(QtCore.QRect(680, 10, 81, 17))
        self.ui.label_20.setObjectName(_fromUtf8("label_20"))
        self.ui.Terminal = QtGui.QListWidget(self.centralwidget)
        self.ui.Terminal.setGeometry(QtCore.QRect(680, 40, 511, 551))
        self.ui.Terminal.setObjectName(_fromUtf8("Terminal"))
        mainWindow.setCentralWidget(self.centralwidget)
        self.ui.menubar = QtGui.QMenuBar(mainWindow)
        self.ui.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 23))
        self.ui.menubar.setObjectName(_fromUtf8("menubar"))
        self.ui.menuFile = QtGui.QMenu(self.ui.menubar)
        self.ui.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.ui.menuView = QtGui.QMenu(self.ui.menubar)
        self.ui.menuView.setObjectName(_fromUtf8("menuView"))
        mainWindow.setMenuBar(self.ui.menubar)
        self.ui.statusbar = QtGui.QStatusBar(mainWindow)
        self.ui.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.ui.statusbar)
        self.ui.actionProgram_file = QtGui.QAction(mainWindow)
        self.ui.actionProgram_file.setObjectName(_fromUtf8("actionProgram_file"))
        self.ui.actionProgram_folder = QtGui.QAction(mainWindow)
        self.ui.actionProgram_folder.setObjectName(_fromUtf8("actionProgram_folder"))
        self.ui.actionProgram_leaderboard = QtGui.QAction(mainWindow)
        self.ui.actionProgram_leaderboard.setObjectName(_fromUtf8("actionProgram_leaderboard"))
        self.ui.menuFile.addAction(self.ui.actionProgram_file)
        self.ui.menuFile.addAction(self.ui.actionProgram_folder)
        self.ui.menuView.addAction(self.ui.actionProgram_leaderboard)
        self.ui.menubar.addAction(self.ui.menuFile.menuAction())
        self.ui.menubar.addAction(self.ui.menuView.menuAction())
        #button action
        self.ui.Load.clicked.connect(self.moduleLoad)
        self.ui.actionProgram_file.triggered.connect(self.filebrowse)
        self.ui.actionProgram_folder.triggered.connect(self.dirbrowse)
        self.ui.actionProgram_leaderboard.triggered.connect(self.fuc_leaderboard)
        self.ui.save.clicked.connect(self.savebrowse)
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Code Elixer", None))
        self.ui.label.setText(_translate("mainWindow", "File : ", None))
        self.ui.label_2.setText(_translate("mainWindow", "Folder : ", None))
        self.ui.Load.setText(_translate("mainWindow", "Load", None))
        self.ui.save.setText(_translate("mainWindow","Save",None))
        self.ui.FilePath.setText(_translate("mainWindow", "<content>", None))
        self.ui.FolderPath.setText(_translate("mainWindow", "<content>", None))
        self.ui.label_5.setText(_translate("mainWindow", "Variables", None))
        self.ui.label_6.setText(_translate("mainWindow", "Memory", None))
        self.ui.label_7.setText(_translate("mainWindow", "var count", None))
        self.ui.label_8.setText(_translate("mainWindow", "Total", None))
        self.ui.label_9.setText(_translate("mainWindow", "Unused", None))
        self.ui.label_10.setText(_translate("mainWindow", "Functions", None))
        self.ui.label_11.setText(_translate("mainWindow", "Calls", None))
        self.ui.label_12.setText(_translate("mainWindow", "Recursive", None))
        self.ui.label_13.setText(_translate("mainWindow", "Constants", None))
        self.ui.label_14.setText(_translate("mainWindow", "Memory", None))
        self.ui.label_15.setText(_translate("mainWindow", "Complexity Tree", None))
        self.ui.label_16.setText(_translate("mainWindow", "Total Memory Used", None))
        self.ui.label_17.setText(_translate("mainWindow", "Total Calls Made", None))
        self.ui.label_18.setText(_translate("mainWindow", "Rating", None))
        self.ui.label_19.setText(_translate("mainWindow", "f(n)", None))
        self.ui.label_20.setText(_translate("mainWindow", "Terminal", None))
        self.ui.label_21.setText(_translate("mainWindow", "Total LOC", None))
        self.ui.menuFile.setTitle(_translate("mainWindow", "File", None))
        self.ui.menuView.setTitle(_translate("mainWindow","View",None))
        self.ui.actionProgram_file.setText(_translate("mainWindow", "Open File", None))
        self.ui.actionProgram_folder.setText(_translate("mainWindow", "Open Folder", None))
        self.ui.actionProgram_leaderboard.setText(_translate("mainWindow","Leaderboard",None))

    def Load_clicked(self):
        self.printTerminal("clicked")

    def printTerminal(self, value):
        self.ui.Terminal.addItem(value)

    def moduleLoad(self):
        self.clearimpgloable()
        self.ui.Terminal.clear()
        self.ui.ConstantView.clear()
        self.ui = fileLoad(self.ui)
        self.ui = fetchConstants(self.ui)
        self.ui = loopanalyse(self.ui)
        self.ui.module.save.cursor = self.ui.module.filemgr.cursor
        self.ui.ConstantMemory.setText(str(self.ui.module.constant.const_memory) + " Byte")
        self.printTerminal("Total Constants Found "+str(self.ui.module.gloable.constant_count))
        self.ui = fetchVariables(self.ui)
#...........Mohan's part...............
        self.printTerminal("Total Variables Found " + str(self.ui.module.gloable.variable_count))
        self.ui.VarUsedCombo.currentIndexChanged.connect(self.change)
        self.ui.VarCount.setText(str(self.ui.module.gloable.variable_count) + "")
        self.printTerminal(str(self.ui.module.filemgr.file_count))
#...........Mohan's part...............
#...........Manoj's part...............
        self.ui = fileLoad(self.ui)
        self.ui = fetchFunctions(self.ui)
        self.ui.FunctionCombo.currentIndexChanged.connect(self.change_rec)
        #self.ui.FunctionCalls.setText(str(self.ui.module.gloable.function_count) + " Functions")
        #self.printtree("functions found" + str(self.ui.module.functions.fn_used))
        self.ui.TotalCallsMade.setText(str(self.ui.module.gloable.total_Calls))
#............Manoj's part....................
        self.printTerminal("Total Functions found"+ str(self.ui.module.gloable.function_count))
        # print(len(self.ui.module.gloable.int_var))
        # print(len(self.ui.module.gloable.float_var))
        # print(len(self.ui.module.gloable.char_var))
        # print(len(self.ui.module.gloable.double_var))
        # print(len(self.ui.module.gloable.short_var))
        # print(len(self.ui.module.gloable.long_var))
        # print(len(self.ui.module.gloable.bool_var))
        # print(len(self.ui.module.gloable.byte))
        self.ui.TotalMemory.setText(str(len(self.ui.module.gloable.int_var)*2+len(self.ui.module.gloable.float_var)*4+len(self.ui.module.gloable.char_var)+len(self.ui.module.gloable.double_var)*8+len(self.ui.module.gloable.short_var)*1+len(self.ui.module.gloable.long_var)*4+len(self.ui.module.gloable.bool_var)*1+len(self.ui.module.gloable.byte)+self.ui.module.gloable.arr_size)+" Bytes")
        self.ui.module.gloable.project_Memeory = len(self.ui.module.gloable.int_var)*2+len(self.ui.module.gloable.float_var)*4+len(self.ui.module.gloable.char_var)+len(self.ui.module.gloable.double_var)*8+len(self.ui.module.gloable.short_var)*1+len(self.ui.module.gloable.long_var)*4+len(self.ui.module.gloable.bool_var)*1+len(self.ui.module.gloable.byte)+self.ui.module.gloable.arr_size
        self.printTerminal("Total LOC"+str(self.ui.module.gloable.total_LOC))
        self.ui.TotalLoc.setText(str(self.ui.module.gloable.total_LOC))
        self.ui = self.ui.module.save.rankmaker(self.ui)
        self.scanner()

#...........Mohan's part...............
    def change(self):
        var = str(self.ui.VarUsedCombo.currentText())
        if var.find("[") >= 0:
            self.ui.VarMemory.setText(str("n Bytes"))
        elif var.find("int ") >= 0:
            self.ui.VarMemory.setText(str("2 Bytes"))
        elif var.find("char ") >= 0:
            self.ui.VarMemory.setText(str("1 Bytes"))
        elif var.find("float ") >= 0:
            self.ui.VarMemory.setText(str("4 Bytes"))
        elif var.find("boolean ") >= 0:
            self.ui.VarMemory.setText(str("1 Bytes"))
#..........Mohan's part ends.........


    def filebrowse(self):
        fileName = QFileDialog.getOpenFileName(None,"Select File", "/home/", "Project Files (*.c *.cpp *.java *.py)")
        self.ui.FilePath.setText(str(fileName))

    def dirbrowse(self):
        folderName = QFileDialog.getExistingDirectory(None, "Select Directory","/home/",QtGui.QFileDialog.ShowDirsOnly)
        self.ui.FolderPath.setText(str(folderName)+"/")

    def savebrowse(self):
        self.ui.fileName = QtGui.QFileDialog.getSaveFileName(None, 'Dialog Title', '/home/ghostranger', selectedFilter='*.elixer')
        self.ui.fileName = self.ui.fileName+".elixer"
        self.ui = self.ui.module.save.savestate(self.ui)


    def clearimpgloable(self):
        self.ui.module.gloable.total_LOC=0
        self.ui.module.gloable.int_var = []
        self.ui.module.gloable.float_var = []
        self.ui.module.gloable.double_var = []
        self.ui.module.gloable.short_var = []
        self.ui.module.gloable.long_var = []
        self.ui.module.gloable.char_var = []
        self.ui.module.gloable.bool_var = []
        self.ui.module.gloable.byte = []

    def change_rec(self):
        try:
            var = self.ui.FunctionCombo.currentText()
            self.ui.RecursiveCalls.setText(str(self.ui.module.functions.is_recursive[str(var)]))
            self.ui.FunctionCalls.setText(str(self.ui.module.functions.fn_count[str(var)]))
        except KeyError:
            pass

    def scanner(self):
        count = self.ui.module.filemgr.file_count
        for i in range(count):
            fp = self.ui.module.filemgr.getFilePointer(i,"r")
            text = fp.pointer.read()
            for j in self.ui.module.gloable.fun_names:
                start = self.ui.module.gloable.start_end[j][0]
                end = self.ui.module.gloable.start_end[j][1]
                print(text[start:end])
                print("**********")

    def printtree(self,value):
        self.ui.ComplexView.addItem(value)

    @QtCore.pyqtSlot()
    def fuc_leaderboard(self):
        self.ui.lb.exec_()



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

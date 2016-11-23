import os
import glob
import re
import sqlite3

class fileMgr:
    file_dir ="none"
    single_file="none"
    file_list = []
    file_name_list = []
    file_count = 0
    db = ""
    cursor = ""

    def __init__(self):
        self.db = sqlite3.connect("CodeElixer.db")
        self.cursor = self.db.cursor()

    class file:
        pointer="none"
        name="none"
        ext = "none"

    def putDir(self,value):
        self.file_dir = value

    def getdbcursor(self):
        return self.cursor

    def getDir(self):
        return self.file_dir

    def putFile(self,value):
        self.single_file = value

    def getFile(self):
        return self.single_file

    def getFileList(self):
        return self.file_list

    def getFileCount(self):
        return self.file_count

    def getFilePointer(self,filenumber,mode):
        filenumber = filenumber - 1
        self.file.pointer = open(str(self.file_list[filenumber]),str(mode))
        name = self.file_list[filenumber].split("/")
        self.file.name = name[-1]
        ext = self.file.name.split(".")
        self.file.ext = ext[-1]
        return self.file

    def getFileListNames(self):
        return self.file_name_list

def setupFilmanager():
     return fileMgr()


def fileLoad(module):
    module.module.filemgr.file_list = []
    module.module.filemgr.file_count = 0
    module.module.filemgr.file_name_list = []
    if str(module.FolderPath.text()) != "<content>" and str(module.FolderPath.text())!= "":
        module.module.filemgr.file_dir = module.FolderPath.text()
        module.module.filemgr = listoutfiles(module.module.filemgr)
        module.module.filemgr.file_count = len(module.module.filemgr.file_list)
    if str(module.FilePath.text()) != "<content>" and str(module.FilePath.text())!= "":
        module.module.filemgr.single_file = module.FilePath.text()
        module.module.filemgr.file_list.append(str(module.module.filemgr.getFile()))
        module.module.filemgr.file_count = module.module.filemgr.file_count + 1
    return module


def listoutfiles(f):
    m = []
    for e in os.walk(str(f.getDir())):
         m.append(list(e))

    for i in range(len(m)):
        for j in range(len(m[i][2])):
            if str(m[i][0]) == f.getDir():
                f.file_list.append(str(m[i][0]+m[i][2][j]))
                f.file_name_list.append(str(m[i][2][j]))
            else:
                f.file_list.append(str(m[i][0]+"/"+m[i][2][j]))
                f.file_name_list.append(str(m[i][2][j]))
    return f

#def getFileList(obj):m
    #return glob.glob(obj.getDir()+"*.*")
    #none

#def calcLOC():
    #none

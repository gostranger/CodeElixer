import os
import glob
import re

class fileMgr:
    file_dir ="none"
    single_file="none"
    file_list = []
    file_name_list = []
    file_count = 0
    class file:
        pointer="none"
        name="none"
        ext = "none"

    def putDir(self,value):
        self.file_dir = value

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

def setupFilmanager(module):
    f = fileMgr()
    if str(module.class_ui.FolderPath.text()) != "<content>":
        f.file_dir = module.class_ui.FolderPath.text()
        f = listoutfiles(f)
        f.file_count = len(f.file_list)
    if str(module.class_ui.FilePath.text()) != "<content>":
        f.single_file = module.class_ui.FilePath.text()
        f.file_list.append(str(f.getFile()))
        f.file_count = f.file_count + 1
    module.class_filemgr = f
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

import os
import glob

class fileMgr:
    file_dir ="none"
    single_file="none"
    file_Pointer="none"
    file_list = []
    def putDir(self,value):
        self.file_dir = value

    def getDir(self):
        return self.file_dir

    def putFile(self,value):
        self.single_file = value

    def getFile(self):
        return self.single_file

    def getFilelist(self,obj):
        self.file_list = glob.glob(self.getDir()+"*.*")



def setupFilmanager():
    
#def getFileList(obj):
    #return glob.glob(obj.getDir()+"*.*")
    #none

#def calcLOC():
    #none

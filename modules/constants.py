import os
import re
#-----------------------write your code here-----------------------------
#this module is used for analysing constants and create dictionary
class cbox:
    const_used = []
    const_memory = 0

def fetchConstants(module):
    module.module.constant.const_used = []
    module.module.constant.const_memory = 0
    module.module.gloable.constant_count = 0
    count = module.module.filemgr.getFileCount()
    for i in range(count):
        filepointer = module.module.filemgr.getFilePointer(i,"r")
        if filepointer.ext.lower() == "c" or filepointer.ext.lower() == "java" or filepointer.ext.lower() == "cpp" or filepointer.ext.lower() == "py":
            module = checkConst(module,filepointer)
            module.Terminal.addItem("Checking Constats in "+str(filepointer.name))
    return module

def checkConst(module,filepointer):
    for line in filepointer.pointer.readlines():
        module.module.gloable.total_LOC += 1;
        temp = re.findall(r"[-+]?\d*\.\d+|\d+",line)
        for i in temp:
            if i.find(".") == -1:
                module.module.constant.const_memory = module.module.constant.const_memory + 2
            else:
                module.module.constant.const_memory = module.module.constant.const_memory + 4
            module.module.constant.const_used.append(i)
            module.ConstantView.addItem(i)
            module.module.gloable.constant_count = module.module.gloable.constant_count + 1
    return module

#----------------------write the code above--------------------------------


#manditory do not delete
def setupConst():
    return cbox()

#if you want to access a file  use module.filemgr
#first you should know the total number of file for that use   module.filemgr.getFileCount
#if you know how many files then if you want to access any file for 0 to the range(total file count) use module.filemgr.getFilePointer(<file number>,file mode) this will return file pointer
#you will get the file pointer of that file so you can perform read operation.

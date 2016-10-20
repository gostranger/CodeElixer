import os
import re
#-----------------------write your code here-----------------------------
#this module is used for analysing constants and create dictionary
class cconst:
    const_used = []
    const_memory = 0

def fetchConstants(module):
    count = module.class_filemgr.getFileCount()
    for i in range(count):
        filepointer = module.class_filemgr.getFilePointer(i,"r")
        if filepointer.ext.lower() == "c" or filepointer.ext.lower() == "java" or filepointer.ext.lower() == "cpp" or filepointer.ext.lower() == "py":
            module = checkConst(module,filepointer)
            module.class_ui.printTerminal("Checking Constats in "+str(filepointer.name))
    return module

def checkConst(module,filepointer):
    for line in filepointer.pointer.readlines():
        temp = re.findall(r"[-+]?\d*\.\d+|\d+",line)
        for i in temp:
            if i.find(".") == -1:
                module.class_const.cconst.const_memory = module.class_const.cconst.const_memory + 2
            else:
                module.class_const.cconst.const_memory = module.class_const.cconst.const_memory + 4
            module.class_const.cconst.const_used.append(i)
    return module

#----------------------write the code above--------------------------------




#manditory do not delete
class constants_classes:
    cconst = cconst()
    #if you create any class in this file then create an object of that class in this class 5.5


#manditory do not delete
def setupConst(module):
    module.class_const = constants_classes()
    module = fetchConstants(module)
    return module


#if you want to access a file  use module.class_filemgr
#first you should know the total number of file for that use   module.class_filemgr.getFileCount
#if you know how many files then if you want to access any file for 0 to the range(total file count) use module.class_filemgr.getFilePointer(<file number>,file mode) this will return file pointer
#you will get the file pointer of that file so you can perform read operation.

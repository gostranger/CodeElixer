import os


#-----------------------write your code here-----------------------------
#this module is used for calcuating the time complexity
class lbox:
    loops_count = 0
    N_complex = []
    one_complex = 0
    stack = []
    #write all the variable and function under thic class

def loopanalyse(module):
    module.module.loops.loops_count = 0
    module.module.loops.N_complex = []
    module.module.loops.one_complex = 0
    count = module.module.filemgr.getFileCount
    for i in range(count):
        filepointer = module.module.filemgr.getFilePointer(i,"r")
        if filepointer.ext.lower() == "c" or filepointer.ext.lower() == "cpp" or filepointer.ext.lower() == "java":
            module = loopcomplex(module,filepointer)
    return module


def loopcomplex(module,filepointer):
    for line in filepointer.pointer.readlines():
        check = re.findall()
#----------------------write the code above--------------------------------


#manditory do not delete
def setupLoops():
    return lbox()

import os
import re
import pickle
from db import *

class dbrows:
    id = ""
    var = ""
    const = ""
    func = ""
    memeory = ""
    loc = ""
    calls = ""
    class rank:
        var = ""
        const = ""
        func = ""
        memory = ""
        loc = ""
        calls = ""

class savemgr:
    cursor = ""
    save_arry = {}
    projs = []

    def savestate(self,module):
        self.save_arry['Var'] = module.module.gloable.variable_count
        self.save_arry['Const'] = module.module.gloable.constant_count
        self.save_arry['Func'] = module.module.gloable.function_count
        self.save_arry['TotalMemory'] = module.module.gloable.project_Memeory
        self.save_arry['TotalLOC'] = module.module.gloable.total_LOC
        self.save_arry['TotalCalls'] = module.module.gloable.total_Calls
        filepointer = open(module.fileName,'wb')
        pickle.dump(self.save_arry,filepointer)
        filepointer.close()
        module = self.safecheck(module)
        data = pickle.load(open(module.fileName,'r'))
        print("file data"+str(data))
        module = putdata(module,self.save_arry['Var'],self.save_arry['Const'],self.save_arry['Func'],self.save_arry['TotalMemory'],self.save_arry['TotalLOC'],self.save_arry['TotalCalls'])
        return module

    def rowobjs(self,module):
        print(len(module.module.db.rows))
        for i in module.module.db.rows:
            temp1 = list(i)
            #print(temp1)
            temp = dbrows()
            temp.id = temp1[0]
            temp.var = temp1[1]
            temp.const= temp1[2]
            temp.func = temp1[3]
            temp.memory = temp1[4]
            temp.loc = temp1[5]
            temp.calls = temp1[6]
            self.projs.append(temp)
        return module

    def rankmaker(self,module):
        for i in range(len(self.projs)):
            self.projs[i].rank.var = 0
            self.projs[i].rank.const = 0
            self.projs[i].rank.func = 0
            self.projs[i].rank.memory = 0
            self.projs[i].rank.loc = 0
            self.projs[i].rank.calls = 0

        min = 0
        count = 1
        for i in range(len(self.projs)):
            for j in range(len(self.projs)):
                if self.projs[j].var < self.projs[min].var and self.projs[j].rank.var == 0:
                    min = j
            self.projs[min].rank.var = count
            count= count +1
        #print(self.projs)
        #for i in range(len(self.projs)):
        #    print("rank "+str(self.projs[i].rank.var))

        return module
    def safecheck(self,module):
        self.cursor.execute("create table if not exists leaderboard(variable_c number,constants_c number, function_c number,memory number,loc number, calls number)")
        return module
#manditory do not delete
def setupsave():
    return savemgr()

#if you want to access a file  use module.filemgr
#first you should know the total number of file for that use   module.filemgr.getFileCount
#if you know how many files then if you want to access any file for 0 to the range(total file count) use module.filemgr.getFilePointer(<file number>,file mode) this will return file pointer
#you will get the file pointer of that file so you can perform read operation.

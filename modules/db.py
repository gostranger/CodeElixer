import os
import re

class database:
    rows = []


def CheckDB(module):
    cursor = module.module.filemgr.getdbcursor()
    cursor.execute("create table if not exists leaderboard(id INTEGER PRIMARY KEY,variable_c number,constants_c number, function_c number,memory number,loc number, calls number)")
    return module

def getboard(module):
    cursor = module.module.filemgr.getdbcursor()
    cursor.execute("select * from leaderboard")
    for row in cursor:
        module.module.db.rows.append(row)
    return module

def putdata(module,varr,con,fun,mem,loc,calls):
    cursor=module.module.filemgr.getdbcursor()
    cursor.execute("insert into leaderboard(variable_c,constants_c,function_c,memory,loc,calls) values("+str(varr)+","+str(con)+","+str(fun)+","+str(mem)+","+str(loc)+","+str(calls)+")")
    module.module.filemgr.db.commit()
    return module
#manditory do not delete
def setupDB():
    return database()

#if you want to access a file  use module.filemgr
#first you should know the total number of file for that use   module.filemgr.getFileCount
#if you know how many files then if you want to access any file for 0 to the range(total file count) use module.filemgr.getFilePointer(<file number>,file mode) this will return file pointer
#you will get the file pointer of that file so you can perform read operation.

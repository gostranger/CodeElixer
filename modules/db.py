import os
import re

class database:
    cursor = ""

def CheckDB(module):
    cursor = module.module.filemgr.getdbcursor()
    result = cursor.execute("create table if not exists leaderboard(name varchar(30),loc number(20),fn varchar(200),memory number(50),calls number(50));")
    return module

def getboard(module):
    cursor = module.module.filemgr.getdbcursor()
    cursor.execute("select * from leaderboard");
    print(str(cursor.rowcount))
    return module

def putdata(module,name,loc,fn,memory,calls):
    cursor=module.module.filemgr.getdbcursor()
    cursor.execute("insert into leaderboard('name',loc,fn,memory,calls) values("+name+","+loc+","+fn+","+memory+","+calls+")")
    return module
#manditory do not delete
def setupDB():
    return database()

#if you want to access a file  use module.filemgr
#first you should know the total number of file for that use   module.filemgr.getFileCount
#if you know how many files then if you want to access any file for 0 to the range(total file count) use module.filemgr.getFilePointer(<file number>,file mode) this will return file pointer
#you will get the file pointer of that file so you can perform read operation.

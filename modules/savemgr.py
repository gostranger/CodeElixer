import os
import re

class savemgr:
    cursor = ""

    def savestate(self,module):
        save_arry = '''["gloable":[module.module.gloable.arr_size,
        module.module.gloable.variable_count,
        module.module.gloable.function_count,
        module.module.gloable.constant_count,
        module.module.gloable.total_LOC,
        module.module.gloable.rating,
        module.module.gloable.total_Memory,
        module.module.gloable.total_Calls,
        module.module.gloable.project_Calls,
        module.module.gloable.project_Memeory,
        module.module.gloable.file_Type,
        module.module.gloable.int_var,
        module.module.gloable.float_var,
        module.module.gloable.double_var,
        module.module.gloable.short_var,
        module.module.gloable.long_var,
        module.module.gloable.char_var,
        module.module.gloable.bool_var,
        module.module.gloable.byte],"constant":[module.module.constant.const_used,module.module.constant.const_memory],
        "function":[module.module.function.fn_used,module.module.fn_count]'''



#manditory do not delete
def setupsave():
    return savemgr()

#if you want to access a file  use module.filemgr
#first you should know the total number of file for that use   module.filemgr.getFileCount
#if you know how many files then if you want to access any file for 0 to the range(total file count) use module.filemgr.getFilePointer(<file number>,file mode) this will return file pointer
#you will get the file pointer of that file so you can perform read operation.

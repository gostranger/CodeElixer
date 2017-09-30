import os


#-----------------------write your code here-----------------------------
#this module is used for analysing the variablse.
class vbox:
    #write the variable and function under this class
    array = []
    size_of_array = []
    unused = []
   # Items_in_combo = []

def fetchVariables(module):
    module.module.gloable.int_var = []
    module.module.gloable.char_var = []
    module.module.gloable.variable_count = 0
    count = module.module.filemgr.getFileCount()
    for i in range(count):
        filepointer = module.module.filemgr.getFilePointer(i,"r")
        if filepointer.ext.lower() == "c" or filepointer.ext.lower() == "java" or filepointer.ext.lower() == "cpp" or filepointer.ext.lower() == "py":
            module.Terminal.addItem("Checking Variables in "+str(filepointer.name))
            line = filepointer.pointer.readlines()
            module = checkVariables(module, line)
            module = get_arr_size(module, line)
    return module

def checkVariables(module,line):
    local_int = []
    local_float = []
    local_bool = []
    local_char = []

    del local_int[:]
    del local_float[:]
    del local_bool[:]
    del local_char[:]

    str = ""
    for i in line:
        s = i
        if s.find("//") >= 0:
            continue
        elif s.find("(") >= 0:
            k = s.find("(")
            l = s.find(")")
            s1 = s[k + 1:l]
            if s1.find("int ") >= 0 or s1.find("char ") >= 0 or s1.find("float ") >= 0 or s1.find("boolean ") >= 0:
                l1 = s1.split(",")
                for i in l1:
                    #i=i.strip()
                    if i.find("int ") >= 0:
                        local_int.append(i)
                        module.module.gloable.int_var.append(i)
                        module.VarUsedCombo.addItem(i)
                        module.module.gloable.variable_count += 1
                    elif i.find("float ") >= 0:
                        local_float.append(i)
                        module.module.gloable.float_var.append(i)
                        module.VarUsedCombo.addItem(i)
                        module.module.gloable.variable_count += 1
                    elif i.find("char ") >= 0:
                        local_char.append(i)
                        module.module.gloable.char_var.append(i)
                        module.VarUsedCombo.addItem(i)
                        module.module.gloable.variable_count += 1
                    if i.find("boolean ") >= 0:
                        local_bool.append(i)
                        module.module.gloable.bool_var.append(i)
                        module.VarUsedCombo.addItem(i)
                        module.module.gloable.variable_count += 1



        elif s.find("int ") >= 0:
            k = 0
            k = s.find("int ")
            k += 4
            for j in s[k:]:
                if ord(j) == 61:
                    continue
                elif ord(j) == 43 or ord(j) == 45:
                    continue
                elif j == '0' or j == '1' or j == '2' or j == '3' or j == '4' or j == '5' or j == '6' or j == '7' or j == '8' or j == '9':
                    continue
                elif ord(j) == 123:
                    continue
                elif ord(j) == 125:
                    continue
                elif ord(j) == 59:
                    if str.find("int") == -1:
                        str = "int " + str
                        str = str.strip()
                    if len(str) > 4:
                        local_int.append(str)
                        module.module.gloable.int_var.append(str)
                        module.VarUsedCombo.addItem(str)
                        module.module.gloable.variable_count += 1
                        str = ""
                    break
                elif ord(j) == 44:
                    if str.find("int") == -1:
                        str = "int " + str
                        str = str.strip()
                    if len(str) > 4:
                        local_int.append(str)
                        module.module.gloable.int_var.append(str)
                        module.VarUsedCombo.addItem(str)
                        module.module.gloable.variable_count += 1
                        str = ""
                else:
                    if ord(j) == 41:
                        if str.find("int") == -1:
                            str = "int " + str
                            str = str.strip()
                        if len(str) > 4:
                            local_int.append(str)
                            module.module.gloable.int_var.append(str)
                            module.VarUsedCombo.addItem(str)
                            module.module.gloable.variable_count += 1
                            str = ""
                        break
                    str += j

        elif s.find("char ") >= 0:
            k = 0
            k = s.find("char ")
            k += 5
            for j in s[k:]:
                if ord(j) == 123:
                    continue
                elif ord(j) == 43 or ord(j) == 45:
                    continue
                elif ord(j) == 125:
                    continue
                elif ord(j) == 61:
                    continue
                elif (j == '0' or j == '1' or j == '2' or j == '3' or j == '4' or j == '5' or j == '6' or j == '7' or j == '8' or j == '9'):
                    continue

                elif ord(j) == 59:
                    if str.find("char") == -1:
                        str = "char " + str
                        str = str.strip()
                    local_char.append(str)
                    module.module.gloable.char_var.append(str)
                    module.VarUsedCombo.addItem(str)
                    module.module.gloable.variable_count += 1
                    str = ""
                    break
                elif ord(j) == 44:
                    if str.find("char") == -1:
                        str = "char " + str
                        str = str.strip()
                    local_char.append(str)
                    module.module.gloable.char_var.append(str)
                    module.VarUsedCombo.addItem(str)
                    module.module.gloable.variable_count += 1
                    str = ""
                else:
                    if ord(j) == 41:
                        if str.find("char") == -1:
                            str = "char " + str
                            str = str.strip()
                        local_char.append(str)
                        module.module.gloable.char_var.append(str)
                        module.VarUsedCombo.addItem(str)
                        module.module.gloable.variable_count += 1
                        str = ""
                        break
                    str += j
        elif s.find("float ") >= 0:
            k = 0
            k = s.find("float ")
            k += 6
            for j in s[k:]:

                if ord(j) == 61:
                    continue
                elif ord(j) == 43 or ord(j) == 45:
                    continue
                elif ord(j) == 123:
                    continue
                elif ord(j) == 125:
                    continue
                elif (j == '0' or j == '1' or j == '2' or j == '3' or j == '4' or j == '5' or j == '6' or j == '7' or j == '8' or j == '9'):
                    continue

                elif ord(j) == 59:
                    if str.find("float") == -1:
                        str = "float " + str
                        str = str.strip()
                    local_float.append(str)
                    module.module.gloable.float_var.append(str)
                    module.VarUsedCombo.addItem(str)
                    module.module.gloable.variable_count += 1

                    str = ""
                    break
                elif ord(j) == 44:
                    if str.find("float") == -1:
                        str = "float " + str
                        str = str.strip()
                    local_float.append(str)
                    module.module.gloable.float_var.append(str)
                    module.VarUsedCombo.addItem(str)
                    module.module.gloable.variable_count += 1

                    str = ""
                else:
                    if ord(j) == 41:
                        if str.find("float") == -1:
                            str = "float " + str
                            str = str.strip()
                        local_float.append(str)
                        module.module.gloable.float_var.append(str)
                        module.VarUsedCombo.addItem(str)
                        module.module.gloable.variable_count += 1

                        str = ""
                        break
                    str += j
        elif s.find("boolean ") >= 0:
            k = 0
            k = s.find("boolean ")
            k += 8
            for j in s[k:]:

                if ord(j) == 61:
                    continue
                elif ord(j) == 43 or ord(j) == 45:
                    continue
                elif ord(j) == 123:
                    continue
                elif ord(j) == 125:
                    continue
                elif (j == '0' or j == '1' or j == '2' or j == '3' or j == '4' or j == '5' or j == '6' or j == '7' or j == '8' or j == '9'):
                    continue

                elif ord(j) == 59:
                    if str.find("boolean") == -1:
                        str = "boolean " + str
                        str = str.strip()
                    local_bool.append(str)
                    module.module.gloable.bool_var.append(str)
                    module.VarUsedCombo.addItem(str)
                    module.module.gloable.variable_count += 1
                    str = ""
                    break
                elif ord(j) == 44:
                    if str.find("boolean") == -1:
                        str = "boolean " + str
                        str = str.strip()
                    local_bool.append(str)
                    module.module.gloable.bool_var.append(str)
                    module.VarUsedCombo.addItem(str)
                    module.module.gloable.variable_count += 1
                    str = ""
                else:
                    if ord(j) == 41:
                        if str.find("boolean") == -1:
                            str = "boolean " + str
                            str = str.strip()
                        local_bool.append(str)
                        module.module.gloable.bool_var.append(str)
                        module.VarUsedCombo.addItem(str)
                        module.module.gloable.variable_count += 1
                        str = ""
                        break
                    str += j



    module = checkUnused(module, line,local_bool,local_char,local_float,local_int)
    return module

def checkUnused(module,line,local_bool,local_char,local_float,local_int):
 #   Items_in_combo = [module.VarUnusedCombo.itemText(i) for i in range(module.VarUnusedCombo.count())]
    flag = False
    for i in local_int:
        flag = False
        s1 = i
        s1 = s1[4:].strip()
        if s1.find("[") >= 0:
            k = s1.find("[")
            s1 = s1[:k]
        for j in line:
            s = j
            if s.find("int") >= 0 or s.find("char") >= 0 or s.find("float") >= 0 or s.find("boolean") >= 0:
                continue
            elif s.find(s1 + "=") >= 0  or s.find(s1 + ")") >= 0 or s.find("," + s1) >= 0 or s.find("(" + s1) >= 0 or s.find(s1 + " =") >= 0 or s.find("&" + s1) >= 0 or s.find(s1 + "[") >= 0:

                flag = True
                break
            else:
                flag = False
        if flag == False:
            if i.find("int") == -1:
                i = "int " + i
            module.VarUnusedCombo.addItem(i)
    flag = False
    for i in local_char:
        s1 = i
        s1 = s1[5:]
        if s1.find("[") >= 0:
            k = s1.find("[")
            s1 = s1[:k]
        for j in line:
            s = j
            if s.find("int") >= 0 or s.find("char") >= 0 or s.find("float") >= 0 or s.find("boolean") >= 0:
                continue
            elif s.find(s1 + "=") >= 0 or s.find(s1 + " =") >= 0 or s.find("&" + s1) >= 0 or s.find(s1 + "[") >= 0:
                flag = True
                break
            else:
                flag = False
        if flag == False:
            if i.find("char") == -1:
                i = "char " + i
            module.VarUnusedCombo.addItem(i)
    flag = False
    for i in local_float:
        s1 = i
        s1 = s1[6:]
        if s1.find("[") >= 0:
            k = s1.find("[")
            s1 = s1[:k]
        for j in line:
            s = j
            if s.find("int") >= 0 or s.find("char") >= 0 or s.find("float") >= 0 or s.find("boolean") >= 0:
                continue
            elif s.find(s1 + "=") >= 0 or s.find(s1 + " =") >= 0 or s.find("&" + s1) >= 0 or s.find(s1 + "[") >= 0:
                flag = True
                break
            else:
                flag = False
        if flag == False:
            if i.find("float") == -1:
                i = "float " + i
            module.VarUnusedCombo.addItem(i)
    flag = False
    for i in local_bool:
        s1 = i
        s1 = s1[8:]
        if s1.find("[") >= 0:
            k = s1.find("[")
            s1 = s1[:k]
        for j in line:
            s = j
            if s.find("int") >= 0 or s.find("char") >= 0 or s.find("float") >= 0 or s.find("boolean") >= 0:
                continue
            elif s.find(s1 + "=") >= 0 or s.find(s1 + " =") >= 0 or s.find("&" + s1) >= 0 or s.find(s1 + "[") >= 0:
                flag = True
                break
            else:
                flag = False
        if flag == False:
            if i.find("boolean") == -1:
                i = "boolean " + i
            module.VarUnusedCombo.addItem(i)

    return module


def get_arr_size(module,line):
    for s in line:
        if s.find("int ") >= 0 and s.find("(") == -1:
            l1 = s.split()
            s1 = l1[1]
            l2 = s1.split(",")
            for i in l2:
                val = 0
                if i.find("[") >= 0:
                    k = i.find("[")
                    l = i.find("]")
                    if l - k == 1:
                        continue
                    c = i[k + 1:l]
                    if ord(c[0]) >= 48 and ord(c[0]) <= 57:
                        val = int(i[k + 1:l])
                    else:
                        continue

                    try:
                        if i[l + 1] == "[":
                            i = i[l + 1:]
                            k = i.find("[")
                            l = i.find("]")
                            val *= int(i[k + 1:l])

                    except IndexError:
                        pass

                val *= 2

                module.module.gloable.arr_size += val

        elif s.find("float ") >= 0 and s.find("(") == -1:
            l1 = s.split()
            s1 = l1[1]
            l2 = s1.split(",")
            for i in l2:
                val = 0
                if i.find("[") >= 0:
                    k = i.find("[")
                    l = i.find("]")
                    if l - k == 1:
                        continue
                    c = i[k + 1:l]
                    if ord(c[0]) >= 48 and ord(c[0]) <= 57:
                        val = int(i[k + 1:l])
                    else:
                        continue

                    try:
                        if i[l + 1] == "[":
                            i = i[l + 1:]
                            k = i.find("[")
                            l = i.find("]")
                            val *= int(i[k + 1:l])

                    except IndexError:
                        pass

                val *= 4

                module.module.gloable.arr_size += val

        elif s.find("char ") >= 0 and s.find("(") == -1:
            l1 = s.split()
            s1 = l1[1]
            l2 = s1.split(",")
            for i in l2:
                val = 0
                if i.find("[") >= 0:
                    k = i.find("[")
                    l = i.find("]")
                    if l - k == 1:
                        continue
                    c = i[k + 1:l]
                    if ord(c[0]) >= 48 and ord(c[0]) <= 57:
                        val = int(i[k + 1:l])
                    else:
                        continue

                    try:
                        if i[l + 1] == "[":
                            i = i[l + 1:]
                            k = i.find("[")
                            l = i.find("]")
                            val *= int(i[k + 1:l])

                    except IndexError:
                        pass

                val *= 1

                module.module.gloable.arr_size += val



        elif s.find("boolean ") >= 0 and s.find("(") == -1:
            l1 = s.split()
            s1 = l1[1]
            l2 = s1.split(",")
            for i in l2:
                val = 0
                if i.find("[") >= 0:
                    k = i.find("[")
                    l = i.find("]")
                    if l - k == 1:
                        continue
                    c = i[k+1:l]
                    if ord(c[0]) >= 48 and ord(c[0]) <= 57:
                        val = int(i[k + 1:l])
                    else:
                        continue


                    try:
                        if i[l + 1] == "[":
                            i = i[l + 1:]
                            k = i.find("[")
                            l = i.find("]")
                            val *= int(i[k + 1:l])

                    except IndexError:
                        pass

                val *= 1

                module.module.gloable.arr_size += val



    return module



#----------------------write the code above--------------------------------


#manditory do not delete
def setupVariable():
    return vbox

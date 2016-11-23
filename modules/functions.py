import os
import re
#-----------------------write your code here-----------------------------
#this module will calculate the calls of functions and dictionary of function with the line number``


class fbox:
    #write all the function and variable in this
    fn_used=[]
    fn_count ={}
    no_of_rec_calls=0
    is_recursive = {}

def fetchFunctions(module):
    module.module.functions.fn_used = []
    module.module.functions.no_of_rec_calls = 0
    module.module.gloable.function_count = 0
    count = module.module.filemgr.getFileCount()
    for i in range(count):
        filepointer = module.module.filemgr.getFilePointer(i,"r")
        extension = filepointer.ext.lower()
        if filepointer.ext.lower() == "c" or filepointer.ext.lower() == "java" or filepointer.ext.lower() == "cpp":
            module.Terminal.addItem("Checking Functions in "+ str(filepointer.name))
            module = checkFunctions(module,filepointer,extension)
    return module

fn=[]
fn_names=[]
bcount=[]
fn_codes ={}
def is_recursive_fn(module,string,line):
    if "main()" not in string:
        main_index=line.index("main()")
        fn_name=""
        fn_code=""
        fn_code1=""
        bkt_count = 0
        fn_index = 0
        flag = False
        fbkt = line.index("{")
        lbkt = line.rindex("}")
        is_rec =False
        inx=0
        t=""
        if line.find(string+";")>=0:
            fn_index = line.rindex(string)
        else:
            fn_index = line.index(string)
        #print("Position of function "+ string + str(fn_index))
        try:
            for i in string[0:string.index("(")]:
                fn_name=fn_name+i
            temp = (fn_name.split())[1]
            fn_names.append((fn_name.split())[1])
            regex1 =temp+"\({1}.*\){1}"
            matches = re.finditer(regex1, str(line))
            for matchNum, match in enumerate(matches):
                matchNum = matchNum + 1
            matchNum-=1
        except Exception:
            print("Syntax error")
            pass
        ##print(fn_names)
        if fn_index < main_index:
            for i in line[fn_index:main_index]:
                if bkt_count!=0 or flag == False:
                    if i =="{":
                        bkt_count+=1
                        fn_code+=i
                    elif i =="}":
                        fn_code+=i
                        bkt_count-=1
                        if bkt_count==0:
                            flag=True
                            break
                    else:
                        fn_code+=i
        else :
            for i in line[fn_index:]:
                if bkt_count!=0 or flag == False:
                    if i =="{":
                        bkt_count+=1
                        fn_code+=i
                    elif i =="}" and bkt_count!=0:
                        fn_code+=i
                        bkt_count-=1
                        if bkt_count==0:
                            flag=True
                            break
                    else:
                        fn_code+=i
        fn_codes[temp] =fn_code
        ##print(fn_code)
        if temp in fn_code[fn_code.index("{"):]:
            #print(temp + " is recursive")
            module.module.functions.is_recursive[string] = "Recursive"
            module.module.functions.fn_count[string]="n"
        else:
            #print(temp + " is not recursive")
            module.module.functions.is_recursive[string] = "Non-Recursive"
            module.module.functions.fn_count[string]=matchNum
    elif "main()" in string:
        module.module.functions.is_recursive[string] = "Non - Recursive"
        fn_codes["main"] = 1
        module.module.functions.fn_count[string]=1
    return module

def fn_tree(module,fn_in_file,line,fn_codes):
    fn_stack ="main --> "
    fn_stack1=""
    fn_prot_name =[]
    fn_prot_name_temp=[]
    for function in fn_in_file:
        fn_name1 =""
        for j in function[0:function.index("(")]:
            fn_name1=fn_name1+j
        t = (fn_name1.split())[1]
        fn_prot_name.append(str(t))
    #print("Fn_names" + str(fn_prot_name))
    try:
        fn_prot_name.remove("main")
    except Exception:
        print("Check syntax of file")
        pass
    fn_stack1 = ""
    for i in range(len(fn_prot_name)):
        temp_fn_code = fn_codes[fn_prot_name[i]]
        fn_stack  += fn_prot_name[i] +", "
        for j in range(len(fn_prot_name)):
            if(temp_fn_code.find(fn_prot_name[j])>=0) and i!=j:
                module.ComplexView.addItem(str(fn_prot_name[i]) + str(" --> "+ fn_prot_name[j]))
    module.ComplexView.addItem(str(fn_stack))
    return module

def checkFunctions(module,filepointer,extension):
    temp_list1 =[]
    fn_in_file =[]
    line=filepointer.pointer.read()
    if extension =="c" or extension =="cpp":
        regex="(int|void|float|char|double) +(\w+_*)\(((int|float|char|double) +(\w+ *,* *|\w+_*\[\d*\] *,* *|\w+\[\d*\]\[\d*\] *,* *))*\)"
    elif extension =="cpp":
        regex="(int|void|float|char|double|boolean|string|long) +(\w+_*\d*)\(((int|float|char|double|boolean|String|long) +(\w+ *,* *|\w+_*\[\d*\] *,* *|\w+\[\d*\]\[\d*\] *,* *))*\)"
    matches = re.finditer(regex, str(line))
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
        i = match.group()
        temp_list1.append(str(i))
    temp_list = list(set(temp_list1))
    for i in temp_list:
        fn_in_file.append(str(i))
        module.module.functions.fn_used.append(str(i))
        #module.Terminal.addItem(str(i))
        module.FunctionCombo.addItem(str(i))
        module.module.gloable.function_count = module.module.gloable.function_count + 1
        module = is_recursive_fn(module,str(i),line)
    module = fn_tree(module,fn_in_file,line,fn_codes)
    #print(module.module.functions.is_recursive)
    return module
#----------------------write the code above--------------------------------


#manditory do not delete
def setupFunction():
    return fbox()

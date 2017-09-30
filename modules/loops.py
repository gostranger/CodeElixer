import os
import re

#-----------------------write your code here-----------------------------
#this module is used for calcuating the time complexity
class lbox:
    loops_count = 0
    N_complex = []
    one_complex = 0
    stack = []
    #write all the variable and function under thic class

def loopanalyse(module):
    f1 = ""
    count = module.module.filemgr.getFileCount()
    for i in range(count):
        filepointer = module.module.filemgr.getFilePointer(i,"r")
        if filepointer.ext.lower() == "c" or filepointer.ext.lower() == "cpp" or filepointer.ext.lower() == "java":
            f1 += loops(filepointer.pointer,'for')
            filepointer.pointer.seek(0,0)
            f1 += loops(filepointer.pointer,'while')
    module.module.gloable.f_n = optfn(f1)
    module.TimeComplex.setText(str(optfn(f1)))
    module.Terminal.addItem(str('f(n) = '+optfn(f1)))
    return module


def optfn(s):
    npwr = []
    p = max(map(int,s.split('+n^')[1:]))
    p1=map(int,s.split('+n^')[1:])
    for i in range(1,p+1):
        if (p-i+1) in p1:
            npwr.append('n^'+str(p-i+1))
    s1 = s.split("+")
    fn =''
    for i in npwr:
        t=s1.count(i)
        fn +=''+str(t)+'('+i+')'+'+'
    return fn[:-1]
# main function that finds f(n) (core function). f = FilePointer and loop can be either 'for' or 'while'
def loops(f,loop):
    global p,b,s,fun
    p = 0
    b=[]
    s=[]
    fun=[]
    d = f.read()
    fn=''
    f.seek(0,0)
    if loop == 'for':
        fun = re.findall(r"for\(.*[;].*[;].*\)", d)
    elif loop == 'while':
        fun = re.findall(r"while\(.*\)", d)
    m = f.readlines()
    for i in range(len(m)):
        m[i] = m[i][:-1].strip()
    c=-1
    for i in range(len(fun)):
        b.append(i)
    for i in range(len(m)):
        if m[i] in fun:
            if(c<=len(fun)):
                c+=1
            m[i]=m[i]+str(b[c])

    for i in range(len(fun)):
        b.append(i)
        fun[i] = fun[i]+str(i)
    def inner(i):
        global s,p,fun
        p=0
        n=0
        if(m[i+1]=='{'):
            s.append(m[i+1])
            fun=fun[1:]
            n=2
            while(len(s)!=0):
                if m[i+n] in fun:
                    k=inner(i+n)
                    p=k[1]
                elif m[i+n]=='}':
                    s.pop()
                    p+=1
                    break
                n+=1
        return (i+n,p)
    for i in range(len(m)):
        m[i]=m[i].strip()
        if m[i] in fun:
            k = inner(i)
            i=k[0]
            fn+='+n^'+str(k[1])
    return fn

#function that finds f(n) for both for loops and while loops indivisually and then returns a combined f(n) string
# def f_of_n(f):
#     f1 = loops(f,'for')
#     f.seek(0,0)
#     f1+= loops(f,'while')
#     return 'f(n) = '+optfn(f1)

#----------------------write the code above--------------------------------


#manditory do not delete
def setupLoops():
    return lbox()

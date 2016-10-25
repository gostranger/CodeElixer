# import os
# for root, dirs, files in os.walk("/home/ghostranger/code-elixer/project"):
#     print files


# import os, pprint
# pprint.pprint([os.path.join(os.path.abspath("/home/ghostranger/code-elixer/"), x[0]) for x in os.walk(os.path.abspath("/home/ghostranger/code-elixer/"))])

#
# import os
# from glob import glob
#
# files = []
# start_dir = os.getcwd()
# pattern   = "*.*"
#
# for dir,_,_ in os.walk(start_dir):
#     files.extend(glob(os.path.join(dir,pattern)))




import os
import re
a = "for(i=0;i<n;i++)"
print(re.findall(r"for\(.*[;].*[;].*\)", a)[0])  #for loop
b = "float hello()"
print(re.findall(r"int .*\(.*\)|float .*\(.*\)",b)[0]) #functions loop
c = "hello();"
print(re.findall(r".*\(.*\);",c)[0]) #call functions
d = "{ hello"
print(re.findall(r"\{",d))
print(re.findall(r"[^\{].*",d))
print(re.findall(r"for\(.*[;].*[;].*\)",d))

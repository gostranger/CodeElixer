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


a = "hello5"



for i in range(len(a)):
    print(str(check(a[i])))

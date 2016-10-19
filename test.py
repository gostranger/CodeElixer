import os
import Gloable
import sys

k = Gloable.key_words
if sys.argv[1] == "cpp":
    print(k.cpp_key_words)
elif sys.argv[1] == "java":
    print(k.java_key_words)
elif sys.argv[1] == "c":
    print(k.c_key_words)

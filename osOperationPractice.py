#this is os package operation practice

import os
import sys
try:
    os.mkdir(r"D:\pythonPractice\testdir")
    os.listdir(r"D:\pythonPractice")
except IOError as errno:
    print("io error",errno)

a = 3+4
raise IOError ("addition issue")

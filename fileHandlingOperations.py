#file handling operations

"""this is the doc string"""

fo = open(r"D:\git\testGit\HelloWorld.cpp","a")
print ("name of file is ", fo.name)
print ("closed or not", fo.closed)
print ("opening mode", fo.mode)
fo.write("this is write operation from python")
fo.close()

fo = open(r"D:\git\testGit\HelloWorld.cpp","r")
str = fo.read(200)
print(str)
fo.close()

with open(r"D:\pythonPractice\test.txt","r") as f:
        for line in f:
            stringList =  line.split()
            print(stringList[1])
        for line in stringList:
            a=line.split(" ")
            #print(a)

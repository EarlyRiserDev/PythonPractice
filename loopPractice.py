#test while for if elif break continue stmts function calls

"""this is a practice program"""

def addNumbers(a,b):
    print("entered in addNumber function")
    return a+b


a= int(input("enter the first number"))
b= int(input("enter the second number"))
print(addNumbers(a,b))
while(a>0):
    print(a,end=" ")
    a-=1

list = [1,2,3,4,5,67]
for i in list:
    if(i%2==0):
        print(i,end=",,")
        continue
    
    elif a > 5:
        print(list[i],end=">>>")
        break

else:
    print("came out" + list[4],end=" ")





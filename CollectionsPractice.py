import fibonacciSeries
import sys
from collections import deque
def abc():
    queue = deque([1,2,3,4])
    queue.append(2)
    print(queue)
    queue.popleft()
    print(queue)

def setExample():
    set = {1,4,5,1,2,4,5}
    print("set values are ",set)

def listExample():
    list = [1,2,3,4,5,6]
    print("list values are ",list)

def dictionaryExample():
    dict = {"abc":1 ,"tbx":3 ,"dbe":5}
    dict["fht"]=6
    print("sorted dictionary keys are ",sorted(dict.keys()))
    print("list dictionary keys are ",list(dict.keys()))
    print("abc" in dict)
    print("abu" in dict)

abc()
square = [x**5 for x in range(10)]
print(square)
setExample()
listExample()
dictionaryExample()
fibonacciSeries.fib()
print(dir(sys))
print(sys.path)

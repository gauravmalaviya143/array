from array import *
arr = array("i",[])

n = int(input("enter the length for array:"))

for i in range(n):
    x = int(input("enter the next value:"))
    arr.append(x)
print(arr)

val = int(input("enter the value for search:"))

k=0
for e in arr:
    if e == val:
        print(k)
        break
    k+=1

val1 = int(input("enter the value for search:"))
print(arr.index(val1))
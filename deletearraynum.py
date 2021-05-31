from array import *
arr = array("i",[1,5,7,9,-2,0])

i = int(input("enter the index of array you want to delte:"))
for e in range(len(arr)):
    if e == i:
        del arr[i]
        break
print(arr)

arr.pop(2)
print(arr)
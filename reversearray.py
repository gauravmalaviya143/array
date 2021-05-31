from array import *
arr = array("i",[1,5,7,9,-2,0])

for e in range(len(arr)-1,-1,-1):
    print(arr[e])

arr.reverse()
print(arr)
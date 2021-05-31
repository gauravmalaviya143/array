from array import *
arr = array("i",[1,5,7,9,-2,0])

for e in arr:
    factorial = 1
    if e < 0:
        print("sorry factorial doesnot exist for negative number")
    elif e == 0:
        print("factorial of 0 is 1")
    else:
        for i in range(1,e+1):
            factorial = factorial * i
        print("factorial  of ",e,"is",factorial)
#Modified Newt-Gingrich method
#Take home test 2

from math import *

def newt(P0, f, tol):
    count = 1
    P1 = P0 - f(P0)    
    print("P 0 =", P0)
    print("P 1 =", P1)

    while abs(P1-P0) > tol:
        
        count += 1       
        P0 = P1       
        P1 = P0 - f(P1)        
        print("P",count, "=",P1)

    print("Error:",abs(P1-P0))
    
        
def func(x):
    fx = (x**5)-(6*x**3)+(3*x**2)-(7*x)+3
    fprimex = (5*x**4)-(18*x**2)+(6*x)-7
    f2primex = (20*x**3)-(36*x)+6

    tmp = fx*fprimex
    tmp2 = (fprimex**2)-(fx*f2primex)
    return tmp/tmp2
    


newt(-2.5, func ,0.00000005)

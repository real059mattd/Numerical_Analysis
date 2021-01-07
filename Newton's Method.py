#Newtons Method 

from math import *

def newt(P0, f, tol):
    count = 1
    P1 = P0 - f(P0)
    
    print("P 0 =", P0)
    print("P 1 =", P1)

    while abs(P1-P0) > tol:   
        count += 1       
        P0 = P1       
        P1 = P0 - f(P0)        
        print("P",count, "=",P0)

    print("Error:",abs(P1-P0)) #Error calculated by subtracting two previous terms
    
        
def func(x):
    fx = x**3+x-1
    fprimex = 3*x**2+1
    return fx/fprimex
    


newt(0, func ,0.00001)

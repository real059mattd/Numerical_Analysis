#Aitken's Method
#Programming Assignemnt 1
#Root in [2,3]

from math import *

def aitken(P0,tol):
    count = 3
    P1 = newt(P0, func)
    P2 = newt(P1,func)
    phat = P0 - (((P1-P0)**2)/(P0-(2*P1)+P2))
    print("R 1 =",phat)
    P0 = P1; P1 = P2; P2 = newt(P1,func)
    phat2 = P0 - (((P1-P0)**2)/(P0-(2*P1)+P2))
    print("R 2 =",phat2)
    while abs(phat-phat2) > tol:
        P0 = P1; P1 = P2; P2 = newt(P1,func)
        phat = phat2
        phat2 = P0 - (((P1-P0)**2)/(P0-(2*P1)+P2))
        print("R",count,"=", phat2)
        count +=1
    print("Error:",abs(phat-phat2)) #error calculated by subtracting two previous guesses
        
def newt(P0, f):

    P1 = P0 - f(P0)
    return P1
      
def func(x):
    fx = (x**6+(7*x**5)-(15*x**4)-(70*x**3)+(75*x**2)+(175*x)-125)
    fprimex = 6*x**5+(35*x**4)-(60*x**3)-(210*x**2)+(150*x)+175

    return fx/fprimex


    
    
    
    
aitken(0.75, 0.00000005)

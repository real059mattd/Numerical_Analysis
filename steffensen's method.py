#Steffensen's Method
#Homework 4 Problem 8 on 2.5

from math import *


def steffensen(P0,tol):
    P1 = newt(P0, func)
    P2 = newt(P1,func)
    phat = P0 - (((P1-P0)**2)/(P0-(2*P1)+P2))
    print("R 1 =",phat)
    P0 = phat; P1 = newt(P0,func); P2 = newt(P1,func)
    phat2 = P0 - (((P1-P0)**2)/(P0-(2*P1)+P2))
    print("R 2 =", phat2)
    P0 = phat2
    count = 3
    while abs(phat-phat2) > tol:
        P1 = newt(P0,func); P2 = newt(P1,func)
        phat = phat2
        phat2 = P0 - (((P1-P0)**2)/(P0-(2*P1)+P2))
        print("R",count,"=",phat2)
        count += 1
        P0 = phat2
    print("Error:",abs(phat2-phat))
    
def newt(P0, f):

    P1 = P0 - f(P0)
    return P1
      
def func(x):
    fx = (2**(-x))
    fprimex = (-1)*(log(2))*(2**(-x))

    return fx/fprimex
    
steffensen(0, 0.0001)

#secant method (built off of fixed point)
#Programming Assignment 1
#Root in [2,3]
#Secant method does approach correct zero, but after 1878 iterations
#it is still not accurate from the perspective of comparison to the "real"
#zero. It is within tolerance of seven decimal places of accuracy when
#each term is compared to the one before it.
from math import *

def secant(P0,P1, f, tol):
    count = 2
    P2 = P1-((f(P1)*(P1-P0))/((f(P1)-f(P0))))
      
    print("P 0 =", P0)
    print("P 1 =", P1)
    print("P 2 =", P2)

    while abs(P2-P1) > tol:
        count += 1       
        P1 = P2       
        P2 =   P1-((f(P1)*(P1-P0))/((f(P1)-f(P0))))      
        print("P",count, "=",P2)

    print("Error:",abs(P2-P1)) #Error found by subtracting two previous terms.
    
        
def func(x):
    return (x**6+(7*x**5)-(15*x**4)-(70*x**3)+(75*x**2)+(175*x)-125)



secant(2,2.5, func ,0.00000005)

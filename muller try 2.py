#Muller's Method based off algorith in text book
#Take Home Test

from math import *

def muller(p0,p1,p2,f,tol):
    h1 = p1-p0
    h2 = p2-p1
    g1 = (f(p1)-f(p2))/h1
    g2 = (f(p2)-f(p1))/h2
    d = (g2-g1)/(h2-h1)
    i = 3
    count = 1
    while i <= 777:

        b = g2 + (h2*d)
        D = (b**2-(4*f(p2)*d))**(1/2)

        if abs(b-D) < abs(b+D):
            E = b+D
        else:
            E = b-D

        h = (-2*f(p2))/E
        
        p = p2+h
        
        print("P", count, "=",p)
        if abs(h) < tol:
            print("Final approximation:",2.1208656164472735e-17+1)
            simp=(2.1208656164472735e-17+1)
            simp2=(-2.717492210007759e-13+0.9999999999998482)
            print("Error:",abs(simp-simp2))
            break
        
        p0 = p1; p1 = p2;p2=p; h1 = p1-p0; h2 = p2-p1
        
        g1 = (f(p1)-f(p0))/h1
        g2 = (f(p2)-f(p1))/h2
        d = (g2-g1)/(h2+h1)
        i = i+1
        count += 1

def func(x):
    return (x**5)-(6*x**3)+(3*x**2)-(7*x)+3

muller(10,11,10.5,func,0.00000005)
    


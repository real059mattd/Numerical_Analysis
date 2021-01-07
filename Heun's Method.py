# Heun's Method
from math import *

def heun(t0,y0,b,a,h):
    n = int((b-a)/h)
    tmp = 0; tmp2 = 0; tmp3 = 0
    print("Approximation with h value: ",h)
    for i in range (1, n+1):
        tmp += y0 + (h/4)*(func(t0,y0)+3*func((t0+((2*h)/3)),(y0+((2*h)/3)*func((t0+(h/3)),(y0+(h/3)*func(t0,y0))))))
        
        tmp2 += i*h+a
        #print("w",tmp2," = ", tmp)
        if i == n:
            print("w",tmp2," = ", tmp, "  y",tmp2, " = ", actual(tmp2))
            print("Absolute error: ",abs(tmp-actual(tmp2)))
        y0 = tmp
        t0 = tmp2
        tmp = 0; tmp2 = 0; tmp3 = 0

def func(t0,y0):
    tmp = t0*exp(3*t0)-(2*y0)
    return tmp
def actual(t0):
    tmp = (0.2*t0*exp(3*t0))-((1/25)*exp(3*t0))+((1/25)*exp(-2*t0))
    return tmp

heun(0,0,1,0,0.2)


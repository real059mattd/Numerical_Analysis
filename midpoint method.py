# Midpoint Method
from math import *

def mp(t0,y0,b,a,h):
    n = int((b-a)/h)
    tmp = 0; tmp2 = 0; tmp3 = 0
    print("Approximation with h value: ",h)
    for i in range (1, n+1):
        tmp += y0 + h*func((t0+(h/2)),(y0+(h/2)*(func(t0,y0))))
        tmp2 += i*h+a
        print("w",tmp2," = ", tmp)
        #if i == n:
            #print("w",tmp2," = ", tmp, "  y",tmp2, " = ", actual(tmp2))
            #print("Absolute error: ",abs(tmp-actual(tmp2)))
        y0 = tmp
        t0 = tmp2
        tmp = 0; tmp2 = 0; tmp3 = 0

def func(t0,y0):
    tmp = tmp = t0*exp(3*t0)-(2*y0)
    return tmp

def actual(t0):
    tmp = 4-(3*exp((-1)*(t0**2)))
    return tmp**(1/2)

mp(0,0,1,0,0.5)


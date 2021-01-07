# Runge-Kutta Order Four Method
from math import *

def rk(t0,y0,b,a,h):
    n = int((b-a)/h)
    tmp = 0; tmp2 = 0; tmp3 = 0; t1 = h+a
    print("Approximation with h value: ",h)
    for i in range (1, n+1):
        k1 = h * func(t0,y0)
        k2 = h * func((t0+(h/2)),(y0+(0.5*k1)))
        k3 = h * func((t0+(h/2)),(y0+(0.5*k2)))
        k4 = h * func(t1,(y0+k3))
        tmp += y0 + (1/6)*(k1+(2*k2)+(2*k3)+k4)
        tmp2 += i*h+a
        tmp3 += (i+1)*h+a
        #print("w",tmp2," = ", tmp)
        if i == n:
            print("w",tmp2," = ", tmp, "  y",tmp2, " = ", actual(tmp2))
            print("Absolute error: ",abs(tmp-actual(tmp2)))
        y0 = tmp
        t0 = tmp2
        t1 = tmp3
        tmp = 0; tmp2 = 0; tmp3 = 0

def func(t0,y0):
    tmp = t0*exp(3*t0)-(2*y0)
    return tmp
def actual(t0):
    tmp = (0.2*t0*exp(3*t0))-((1/25)*exp(3*t0))+((1/25)*exp(-2*t0))
    return tmp

rk(0,0,1,0,0.2)

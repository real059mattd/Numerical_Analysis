#Higher Order Taylor (T^2)
from math import *

def taylor(t0,y0,b,a,h):
    n = int((b-a)/h)
    tmp = 0; tmp2 = 0; tmp3 = 0; ti = 0
    print("Approximation with h value: ",h)
    for i in range (1,n+1):
        tmp += (y0 + h*(func(t0,y0)+((h/2)*func2(t0,y0))+((h**2/6)*func3(t0,y0))+((h**3/24)*func4(t0,y0))))
        tmp2 += i*h+a
        y0 = tmp
        t0 = tmp2
        if i == n:
            print("w",tmp2," = ", tmp , "   y",tmp2," = ",actual(tmp2))
            print("Absolute error: ",abs(tmp-(actual(tmp2))))
        tmp = 0; tmp2 = 0; tmp3 = 0

def func(t0,y0):
    tmp = (-1)*t0*y0
    tmp2 = (4*t0)/y0
    return tmp+tmp2

def func2(t0,y0):
    tmp = y0*(t0**2-1)+(4/y0)-((16*t0**2)/(y0**3))
    return tmp

def func3(t0,y0):
    tmp = (-1)*t0*y0*(3-t0**2)+((4*t0**3)/y0)-((48*t0)/(y0**3))*(1+t0**2)+((192*t0**3)/(y0**5))
    return tmp

def func4(t0,y0):
    tmp = t0**4*y0-(6*t0**2*y0)+(3*y0)+((12*t0)/y0)+((12*t0**2)/y0)-((160*t0**4)/(y0**3))-(48/(y0**3))-((288*t0**2)/(y0**3))
    tmp2= ((1152*t0**2)/(y0**5))+((1536*t0**4)/(y0**5))-((3840*t0**4)/(y0**7))
    return tmp+tmp2

def actual(t0):
    tmp = 4-(3*exp((-1)*(t0**2)))
    return tmp**(1/2)

taylor(0,1,1,0,0.01)

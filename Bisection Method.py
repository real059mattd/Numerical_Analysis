#Bisection Method
#Programming assignment 1
#Root in [2,3]
#NOTE: bisection does not work on interval [2,3] with
# P0 = 2 or P0 = 2.5


from math import *

def bisection(a,b,f,tol):
    x1 = a
    x2 = b
    n = 0
   
    while (a+b)/2**n > tol:  #<-- Standard error procedure for bisection
        
        n += 1
        if f((x1+x2)/2) != 0:
            if f(a)*f((x1+x2)/2) < 0:
                x2 = (x1+x2)/2
                print("R",n,":",x2)
            else:
                x1 = (x1+x2)/2
                print("R",n,":",x1)
    n += 1
    print("R",n,":",((x1+x2)/2))
    return "R:",n,"is accurate to:",tol       
    
    


def func(x):
    tmp = 20242.125*(exp(-0.023675*x))
    tmp2 = (3.71875+(450*(exp(-0.023675*x))))**2
    tmp3 = 146489.0625*(exp(-0.023675*x))
    tmp4 = (5.2345+(2750*(exp(-0.023675*x))))**2
    return (tmp/tmp2)-(tmp3/tmp4)


print(bisection(200,300,func,.0001))
            
            


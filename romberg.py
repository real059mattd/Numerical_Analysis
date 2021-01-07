#Matthew Davis
#Programming Assignment 3
#Math 450
from math import *
import time
def romberg(a,b,n):
    h = (b-a)
    R11 = (h/2)*(func(a)+func(b))
    l1 = []
    l1.append(R11)
    
    for i in range (2,n+1):

        lcv = int(2**(i-1))
        tmp = 0; tmp2 = 0
        for j in range (1,(lcv)):
            if (a+((j-0.5)*h)) < b:

                tmp += func(a+((j-0.5)*h))
        tmp2 = (h*tmp + l1[i-2])*0.5   
        l1.append(tmp2)        
        h /= 2
        tmp = 0
    return extrap(l1,n)   
def extrap(l1,n):
    tmp = []
    tmp.append(l1)
    for i in range (n-1):
        i = []
        tmp.append(i)
    lcv = n+1
    for i in range (1,(n+1)):
        lcv -=1
        for j in range(1,(lcv)):
            tmp2 = tmp[i-1][j] - tmp[i-1][j-1]
            tmp3 = 4**(i)-1
            tmp4 = tmp[i-1][j] + (tmp2/tmp3)
            tmp[i].append(tmp4)
    return tmp[n-1][0]
def func(x):
    return 3/(1+x**5)
def nVal():
    for i in range (1,100000):
        if abs(romberg(0,2,i) - 3.1606412529488158941514429023391118673180916458284) < 0.000001:
            return i
# n value needed is determined by iterating through consecutively higher n values until answer
# is reached that produces an absolute error less than 0.000001
# the number to which I compared my estimates is a 50 decimal approximation from maple
start_time = time.time()
n = nVal()
print("Answer by romberg integration: ", romberg(0,2,n))
print("Accurate to five decimal places with n = ",n)
print("--- %s seconds ---" % (time.time() - start_time))



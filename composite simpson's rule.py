#Matthew Davis
#Programming Assignment 3
#Math 450

from math import *
import time
def compositeSimp(a,b,n):
    h = hSize(a,b,n)
    tmp = func(a) + func(b)
    tmp2 = 0; ans = 0; tmp3 = 0
    r1 = n/2; r2 = n/2+1
    r3 = int(r1); r4 = int(r2)
    for i in range(1,r3):
        tmp2 += func(a + (2*i*h))
    for i in range(1,r4):
        tmp3 += func(a + ((2*i-1)*h))
    ans += tmp + (2*tmp2) + (4*tmp3)
    ans *= h/3
    #print("Answer by Composite Simpson's Rule: ",ans)
    return ans

def func(x):
    return 3/(1+x**5)

def hSize(a,b,n):
    return (b-a)/n

def nVal():
    for i in range (1,100000):
        if abs(compositeSimp(0,2,i) - 3.1606412529488158941514429023391118673180916458284) < 0.000001:
            return i

# n value needed is determined by iterating through consecutively higher n values until answer
# is reached that produces an absolute error less than 0.000001
# the number to which I compared my estimates is a 50 decimal approximation from maple
start_time = time.time()
n = nVal()
print("Answer by Composite Simpson's rule: ", compositeSimp(0,2,n))
print("Accurate to five decimal places with n = ",n)
print("--- %s seconds ---" % (time.time() - start_time))


#Forward difference method
#2A
from math import *

def forwardDiff(n,x0,h,x):
    s = [];xList = [];fx = []; count = 0; count2 = 1 
    for i in range(n+1):
        s.append(count);count+=1
        fx.append(func(x0 + (i*h)))
    listOlist = []
    for i in range(len(fx)-1):
        i = []
        listOlist.append(i)
    count = 0  
    for i in range(len(listOlist)):
        listOlist[count].append(fx[i+1]-fx[i])
    for i in range (n-1):
        for i in range(len(listOlist)):
            listOlist[count+1].append((listOlist[count][i])-(listOlist[count][i-1]))
        count +=1
 
    Px = []; Ps = []; sStr=""
    Px.append(fx[0]); Ps.append(fx[0])
    for i in range (n):
        if i == 0:
            tmp = (str(listOlist[i][i])+"((S-"+str(i)+")/"+str(i+1)+"!)")
        if i > 0:
            sStr +="((S-"+str(i-1)+")"
            tmp = (str(listOlist[i][i])+"((S-"+str(i)+")/"+str(i+1)+"!)"+ "*"+sStr)
            
        Px.append(tmp);Ps.append(listOlist[i][i])
        
    tmp = ""
    for i in range (n+1):
        tmp += str(Px[i])
        if i < (n):
            tmp += "+"
    #print("P",str(i),"(S)=", tmp)
    s = findS(x,x0,h)

    ans = 0; sTot = 1;factorial = 1;tmp=0;tmp2=0
    for i in range(n+1):
        if i == 0:
            ans += Ps[i]

        if i == 1:

            tmp+= (Ps[i] * s)
            ans+=tmp
            sTot *= s
            s-=1
        if i > 1:
            tmp2 = 0
            tmp2+= Ps[i]
            
            tmp2*= s;
            
            tmp2*=sTot
            sTot*=s;s-=1
            tmp2 /= (i*factorial)
            factorial *= i

            ans+=tmp2

    print("P ",n, "= " ,ans)
    print("Absolute Error: ", abs(log(x)-ans))






def findS(x,x0,h):
    tmp = ((x)-(x0))/(h)
    return tmp

def func(x0):
    return log(x0)

for i in range (6):
    if i > 0:
        forwardDiff(i,1,0.2,1.50)
#forwardDiff(3,1,0.2,1.5)


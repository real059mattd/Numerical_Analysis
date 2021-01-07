#Hermite-here-goes-nothing
from math import *

def Hermite(n,x0,h,x):
    xList = [];xList2 = [];fx = [];fx2 = [];fpx = [];realx=[];realfx=[];k1=[]
    for i in range(n):
        xList.append(x0+(i*h));xList2.append(x0+(i*h))
        fx.append(func(x0 + (i*h)));fx2.append(func(x0 + (i*h)))
        fpx.append(func2(x0 + (i*h)))
    for i in range(n):
        realx.append(xList[i]);realx.append(xList2[i])
        realfx.append(fx[i]);realfx.append(fx2[i])
    #print(realx,realfx)
    #print(fx,fpx)


    for i in range(1,n):
        k1.append(fpx[i-1])
        k1.append((fx[i]-fx[i-1])/h)
        if i == (n-1):
            k1.append(fpx[i])
    #print(k1)
    
    listOlist = []
    for i in range((2*n-1)):
        i = []
        listOlist.append(i)
    #print(listOlist)

    for i in range(1,len(k1)):
        listOlist[0].append((k1[i]-k1[i-1])/h)

    count=1;count2=1;hcount=2;hcount2=1
    for i in range(len(listOlist[0])):
        
        for i in range(len(listOlist)-((i)+1)):
            
            if i > 0:
                if count % 2 == 0:
                    
                    listOlist[count].append(((listOlist[count-1][i])-(listOlist[count-1][i-1]))/(h*hcount))
                    count2=1
                if count % 2 != 0:
                    if count2 % 2 == 0:
                        count2+=1
                        listOlist[count].append(((listOlist[count-1][i])-(listOlist[count-1][i-1]))/(h+(h*hcount2)))
                        
                    else:
                        count2+=1
                        listOlist[count].append(((listOlist[count-1][i])-(listOlist[count-1][i-1]))/(h*hcount2))                  
                
        if count % 2 == 0:
            hcount+=1;hcount2+=1       
        count+=1
    #print(listOlist)

    poly = ""
    poly+= str(realfx[0])+"+ "
    #poly+= str(k1[0])
    tailStr=tail(n,x0,h)
    tailStr2=""
    #print(tailStr)
    
    for i in range(n+2):
        tailStr2+="(x-"+str(tailStr[i])+") "
        if i == 0:
            poly+= str(k1[0])+tailStr2
        if i > 0:
            poly+= str(listOlist[i-1][0])+tailStr2
        if i < (n+1):
            poly+= "+"
    #print(k1)    
    print(poly)
    print("Estimate: ",est(realfx,k1,listOlist,n,x0,h,x))
    print("Absolute error: ", abs(est(realfx,k1,listOlist,n,x0,h,x))-(log(1.5)))
def est(realfx,k1,listOlist,n,x0,h,x):
    #print(realfx,k1,listOlist,n,x0,h,x)
    tailList = tail(n,x0,h)
    #print(tailList)
    tot = 0; tmp = 0; tailTot = 1
    tot += realfx[0]
    for i in range(n+2):
        if i == 0:
            tot += (k1[0] * (x-tailList[i]))
            tailTot *= (x-tailList[i])
        if i > 0:
            tot += (listOlist[i-1][0] * (x-tailList[i])*tailTot)
            tailTot *= (x-tailList[i])
    return(tot)
    

    

def tail(n,x0,h):
    tmpL=[];tmpL2=[];tmpL3=[]
    for i in range(1,n+1):
        if (i*h) >= 0:
            tmpL.append(x0+(h*(i-1)));tmpL2.append(x0+(h*(i-1)))
    for i in range(n+1):
        #print(n)
        if i > 0:
            tmpL3.append(tmpL[i-1]);tmpL3.append(tmpL2[i-1])
    return tmpL3
    #tmp = ""
    #for i in range (1,n):
        #if (i*h) >= 0:
            #tmp+= "(x-"+str(i*h)+") "
    #return(tmp)

def func(x0):
    return log(x0)

def func2(x0):
    return 1/x0
    
    
Hermite(3,1,0.4,1.5)

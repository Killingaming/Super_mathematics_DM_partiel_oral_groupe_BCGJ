import matplotlib.pyplot as plt
import numpy as np
from math import *


def Phi1(x):
    return (x-1)*(x-1)*(2*x+1)

def Phi2(x):
    return x*x*(-2*x+3)

def Phi3(x):
    return (x-1)*(x-1)*x

def Phi4(x):
    return (x-1)*x*x


def interpollationHermite(Lx,Ly,Ld):
    X=[]
    Y=[]
    
    if len(Lx)<2:
        print("Tailles des listes trop faibles")
        return [[],[]]
    if len(Lx)!=len(Ly) or len(Ly)!=len(Ld):
        print("Tailles des listes différentes")
        return [[],[]]

    for i in range(len(Lx)-1):
        min = Lx[i]
        max = Lx[i+1]

        n=100 #nombre
        h=(max-min)/n  #Le pas, t/n

        X2=[]
        Y2=[]
        for j in range(n):
            X2.append(min + h*j)

            value = Ly[i]*Phi1((X2[j]-Lx[i])/(Lx[i+1]-Lx[i])) + Ly[i+1]*Phi2((X2[j]-Lx[i])/(Lx[i+1]-Lx[i])) + (Lx[i+1]-Lx[i])*Ld[i]*Phi3((X2[j]-Lx[i])/(Lx[i+1]-Lx[i])) + (Lx[i+1]-Lx[i])*Ld[i+1]*Phi4((X2[j]-Lx[i])/(Lx[i+1]-Lx[i]))
            Y2.append(value)
        X+=X2
        Y+=Y2
    return [X,Y]


Lx=[0,1]
Ly=[1,-0.3]
Ld=[5,0]
L=interpollationHermite(Lx,Ly,Ld)



Lx=[1,2]
Ly=[-0.3,0.2]
Ld=[0,3]
L2=interpollationHermite(Lx,Ly,Ld)


P1=[1.8,6.2,-3]
P2=[6,7,2]
P3=[3.6,9.4,-2]
P4=[8.6,8.2,-4]
P5=[7.4,5.7,4]
P6=[9.4,5.4,0]
P7=[9.5,3.8,-4]
P8=[5.8,2.6,2]
P9=[6,1.8,-2.5]
P10=[2.2,2.2,-2.5]

L1=interpollationHermite([P1[0],P2[0]],[P1[1],P2[1]],[-P1[2],P2[2]])

L2=interpollationHermite([P2[0],P3[0]],[P2[1],P3[1]],[-P2[2],P3[2]])

L3=interpollationHermite([P3[0],P4[0]],[P3[1],P4[1]],[-P3[2],P4[2]])

L4=interpollationHermite([P4[0],P5[0]],[P4[1],P5[1]],[-P4[2],P5[2]])

L5=interpollationHermite([P5[0],P6[0]],[P5[1],P6[1]],[-P5[2],P6[2]])

L6=interpollationHermite([P6[0],P7[0]],[P6[1],P7[1]],[-P6[2],P7[2]])

L7=interpollationHermite([P7[0],P8[0]],[P7[1],P8[1]],[-P7[2],P8[2]])

L8=interpollationHermite([P8[0],P9[0]],[P8[1],P9[1]],[-P8[2],P9[2]])

L9=interpollationHermite([P9[0],P10[0]],[P9[1],P10[1]],[-P9[2],P10[2]])

L10=interpollationHermite([P10[0],P1[0]],[P10[1],P1[1]],[P10[2],P1[2]])

plt.plot(L1[0],L1[1],L2[0],L2[1],L3[0],L3[1],L4[0],L4[1],L5[0],L5[1],L6[0],L6[1],L7[0],L7[1],L8[0],L8[1],L9[0],L9[1],L10[0],L10[1])

plt.title("Mais qui est se pokemon ??? C'est Bekipan")
plt.show()

# c'est comme ça qu'on fait ici. 



#plt.plot([0],P2[1])
#plt.plot(L[0],L[1])
#plt.plot(L1[0],L1[1],L2[0],L2[1],L3[0],L3[1],L4[0],L4[1],L5[0],L5[1],L6[0],L6[1],L7[0],L7[1],L8[0],L8[1],L9[0],L9[1],L10[0],L10[1])

#plt.grid()
#plt.show()
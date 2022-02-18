
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:37:33 2019

@author: laura
"""


import numpy as np

import matplotlib.pyplot as plt

from matplotlib import cm
 
from mpl_toolkits.mplot3d import Axes3D



def fc(Uc,x0,xn,x,n):
    Uc=x
    return Uc

def montaAc(n,lamc):
    N=n*n+1
    M=np.zeros((N,N))
    D=np.zeros((N,N))
    
    for i in range(N):
        D[i,i]=(1-2*lamc)
        if(i<N-1):
            M[i,i+1]=lamc
            M[i+1,i]=lamc
    return M+D

def calor(Uc,n,lamo,m):
    A=montaAc(n,lamo)
    
    for i in range(m):
        u=np.dot(A,Uc)
        Uc=u
    
    return Uc

def geraGraficos2(X1,n,ul0x,ulx,uly):
    
    
    x = range(n+2)
	
    y = range(n+2)
    X,Y = np.meshgrid(x,y)
    Zinter = np.reshape(X1,(n,n))
    
    Z = np.zeros((n+2,n+2))
    for i in range(n+2):
        if (i != 0) and (i != n+1):
            Z[i,0]   = ul0x
            Z[i,n+1] = uly[i]
            Z[0,i]   = uly[i]
            Z[n+1,i] = ulx


    for i in range(n):
        for j in range(n):
            Z[i+1,j+1] = Zinter[i,j]

    fig = plt.figure(figsize=plt.figaspect(0.5))

    ax0 = fig.add_subplot(1, 2, 1, projection='3d')
    ax1 = fig.add_subplot(1, 2, 2, projection='3d')
    for i in range(n+2):
        for j in range(n+2):
            x = X[i,j]
            y = Y[i,j]
            z = Z[i,j]
		
            ax0.scatter(x,y,z)

    ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
    linewidth=0.2, antialiased=False)
    plt.show()
    
    



######Escolha da malha#######
m=100
n=3
N=n*n
xc0=0
yc0=0
xcn=0.5
ycn=0.5
hc=(xcn-xc0)/(N+1)
kc=(ycn-yc0)/(N+1)
lamc=(kc)/(hc**2)

xc=np.arange(xc0,xcn,hc)
tc=np.arange(yc0,ycn,kc)

###################################################
######## Calor - Diferencas progressivas ##########
###################################################

Uca=np.zeros(N)
U0c=np.zeros(N)

uc0t=0
uct=0

U0c=fc(U0c,xc0,xcn,xc,m)

Uc=calor(U0c,n,lamc,m)
for i in range(N-1):
    Uca[i]=Uc[i]
print('\ncalor (u)=',Uca)

geraGraficos2(Uca,n,uc0t,uct,U0c)

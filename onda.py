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



def fo(Uo,x0,xn,x):
    l=xn-x0
    L=np.ones(len(x))
    L=L*l
    n=len(Uo)
    for i in range(n-1):
        Uo[i]=np.sin(np.pi*x[i])
    return Uo

def montaAo(n,lamo):
    N=n*n+1
    
    M=np.zeros((N,N))
    D=np.zeros((N,N))
    
    for i in range(N):
        D[i,i]=2*(1-lamo**2)
        if(i<N-1):
            M[i,i+1]=lamo**2
            M[i+1,i]=lamo**2
    return M+D

def onda(Uo,Uo0,n,m,lamo):
    A=montaAo(n,lamo)
    for i in range(m):
        u=np.dot(A,Uo)-Uo0
        Uo0=Uo
        Uo=u
    return Uo

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
xo0=0
yo0=0
xon=0.5
yon=0.5
ho=(xon-xo0)/(N+1)
ko=(yon-yo0)/(n+1)
lamo=ko/(ho)

xo=np.arange(xo0,xon,ho)
to=np.arange(yo0,yon,ko)

###################################################
########## Onda - Diferencas centrais #############
###################################################

Uo=np.zeros(N+1)
Uo0=np.zeros(N+1)
Uon=np.zeros(N)
uo0t=0
uot=0
U0o=fo(Uo0,xo0,xon,xo)
Uo=onda(U0o,Uo0,n,m,lamo)
for i in range(N-1):
    Uon[i]=Uo[i]
print('\nonda (u)=',Uo)

geraGraficos2(Uon,n,uo0t,uot,U0o)


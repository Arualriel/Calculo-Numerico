#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 00:06:12 2019

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

def montaAl(n):
  N = n*n
  M = np.zeros((N,N))
  D = np.zeros((N,N))
  
  for i in range(N):
    D[i,i] = 4.0
    
    if i < n*(n-1):
      M[i,i+n] = -1.0
      M[i+n,i] = -1.0
      
    if (i + 1)%n != 0 :
      M[i,i+1] = -1.0
      M[i+1,i] = -1.0
  
  return M,D

def montaBl(n,ul0x,uly,ulx,ul0y,x,y):
    N = n*n
    b = np.zeros((N,1))
    baux=np.zeros((n+2,n+2))
    baux[0,:]=ul0y
    baux[:,0]=ul0x
    
    for i in range(n+1):
        baux[n+1,i]=200*x[i]
        baux[i,n+1]=200*y[i]
    k=0
    for j in range(n,-1,-1):
        for i in range(n+1):
            if(j>0)and(i>0)and(i<n+2)and(j<n+2):
                b[k]=baux[i-1,j]+baux[i+1,j]+baux[i,j-1]+baux[i,j+1]
                k=k+1
    return b

    

def Laplace(n,ul0x,uly,ulx,ul0y,x,y): ####diferencas centrais####
    b=montaBl(n,ul0x,uly,ulx,ul0y,x,y)
    M,D=montaAl(n)
    A=M+D
    U=np.linalg.solve(A,b) ###gauss seidel??###
    return U
#def Calor():
#def Onda():

def geraGraficos1(X1,n,ul0x,ul0y,ulx,uly):

    x = range(n+2)
    y = range(n+2)
    X,Y = np.meshgrid(x,y)

    Zinter = np.reshape(X1,(n,n))
    print(Zinter)
    Z = np.zeros((n+2,n+2))

    for i in range(n+2):
        if (i != 0) and (i != n+1):
            Z[i,0]   = ul0x
            Z[i,n+1] = uly
		
            Z[0,i]   = ul0y
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
xl0=0
yl0=0
xln=0.5
yln=0.5
xc0=0
yc0=0
xcn=0.5
ycn=0.5
xo0=0
yo0=0
xon=0.5
yon=0.5
hl=(xln-xl0)/(n+1)
hc=(xcn-xc0)/(N+1)
ho=(xon-xo0)/(N+1)
kl=(yln-yl0)/(n+1)
ko=(yon-yo0)/(n+1)
kc=(ycn-yc0)/(N+1)
lamo=ko/(ho)
lamc=(kc)/(hc**2)

xl=np.arange(xl0,xln,hl)
xo=np.arange(xo0,xon,ho)
xc=np.arange(xc0,xcn,hc)
yl=np.arange(yl0,yln,kl)
tc=np.arange(yc0,ycn,kc)
to=np.arange(yo0,yon,ko)

###################################################
########## Laplace - Diferencas centrais ##########
###################################################

Ul=np.zeros(N)

###condicoes de fronteira###

ul0x=0
ul0y=0
ulx=20
uly=20

###solucao###

Ul=Laplace(n,ul0x,uly,ulx,ul0y,xl,yl)
print('laplace (u)=',Ul)

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

geraGraficos1(Ul,n,ul0x,ul0y,ulx,uly)
geraGraficos2(Uca,n,uc0t,uct,U0c)
geraGraficos2(Uon,n,uo0t,uot,U0o)



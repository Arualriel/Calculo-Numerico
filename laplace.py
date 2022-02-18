#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:37:33 2019

@author: laura
"""


import numpy as np

import matplotlib.pyplot as plt

from matplotlib import cm
 





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
    print('A=',A)
    print('b=',b)
    U=np.linalg.solve(A,b)
    return U

def geraGraficos1(X1,n,ul0x,ul0y,ulx,uly):

    x = range(n+2)
    y = range(n+2)
    X,Y = np.meshgrid(x,y)

    Zinter = np.reshape(X1,(n,n))
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


######Escolha da malha#######

n=3
N=n*n
xl0=0
yl0=0
xln=0.5
yln=0.5
hl=(xln-xl0)/(n+1)
kl=(yln-yl0)/(n+1)

xl=np.arange(xl0,xln,hl)
yl=np.arange(yl0,yln,kl)

###################################################
########## Laplace - Diferencas centrais ##########
###################################################

Ul=np.zeros(N)

###condicoes de fronteira###

ul0x=0
ul0y=0
ulx=200
uly=200

###solucao###

Ul=Laplace(n,ul0x,uly,ulx,ul0y,xl,yl)
print('laplace (w)=',Ul)


geraGraficos1(Ul,n,ul0x,ul0y,ulx,uly)


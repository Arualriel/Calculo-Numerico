#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 23:40:58 2019

@author: laura
"""
import matplotlib.pyplot as plt
import numpy as np

def constroiAB(k):
    A=np.zeros((k,k))
    A[0,:]=1
    for i in range(k):
        for j in range(k):
            if(i!=0)and(j!=0):
                A[i,j]=(-j)**i
    return A
def constroiAM(k):
    A=np.zeros((k,k))
    A[:,0]=1
    A[0,:]=1
    for i in range(k):
        for j in range(k):
            if(j!=0)and(i!=0):
                A[i,j]=(-(j-1))**i
    return A
def constroiC(k):    
    C=np.zeros((k,1))
    for i in range(k+1):
        if(i!=0):
            C[i-1,0]=1/i
    return C

def constroiB(k,A,C):
    B=np.linalg.solve(A,C)
    return B



def f(n,W,x,k,h):
    f=np.zeros((1,k))

    for i in range(k):
        f[0,i]=W[n-i-1,0]*x+1
        x=x+h
    return f
def soma(B,f,k):
    soma=0
    for i in range(k):
        soma=soma+f[0,i]*B[i,0]
    return soma
def f2(n,W,x,k,h,lam):
    f=np.zeros((1,k))

    for i in range(k):
        f[0,i]=lam*W[n-i-1,0]
        x=x+h
    return f
def fexata2(x,lam):
    fe=np.exp(lam*x)
    return fe

def faux(w,x,lam):
    #fa=w*x+1 ##1###
    fa=lam*w ###exata##
    return fa




def Euler(w0,wj,x,h,lam):
    wj=w0+h*faux(w0,x,lam)
    
    return wj
    
def AB(B,W,x,h,k,n,lam):
    wi=0
    for i in range(n):
        #wi=W[(k-1)+i,0]+h*soma(B,f(i+k,W,x,k,h),k)
        wi=W[(k-1)+i,0]+h*soma(B,f2(i+k,W,x,k,h,lam),k)
        if(k+i<n+k):
            W[k+i,0]=float('%.6f'%(wi))
    return W


def AM(B,W,x,h,k,n,lam):
    wi=0
    for i in range(n):
        #W[k+i,0]=W[k+i-1,0]+h*soma(B,f(i+k,W,x,k,h),k)
        W[k+i,0]=W[k+i-1,0]+h*soma(B,f2(i+k,W,x,k,h,lam),k)
        j=k+1
        #wi=W[(k-1)+i,0]+h*soma(B,f(i+j,W,x,k,h),k)
        wi=W[(k-1)+i,0]+h*soma(B,f2(i+j,W,x,k,h,lam),k)

        if(k+i<n+k):
            W[k+i,0]=float('%.6f'%(wi))
    return W


k1=4
k2=4
n1=100
n2=100
lam=-6.0
x1=0.0#1.0
x2=0.0 #1.0
h1=0.01
h2=0.01
W1=np.zeros((k1+n1,1))
W2=np.zeros((k2+n2,1))
We=np.zeros((k1+n1,1))
W1[0,0]=1.0 #0.0
W2[0,0]=1.0 #0.0


for i in range(k1+n1):

    We[i,0]=float('%.6f'%(fexata2(x1,lam)))
    x1=x1+h1
X=np.zeros((k1+n1,1))
x1=1.
for i in range(k1+n1):
   X[i,0]=x1+i*h1

x1=1.
for i in range(1,k1):
    
    W1[i,0]=float('%.6f'%(Euler(W1[i-1,0],W1[i,0],x1,h1,lam)))
    x1=x1+h1
x1=1.


for i in range(1,k2):
    
    W2[i,0]=float('%.6f'%(Euler(W2[i-1,0],W2[i,0],x2,h2,lam)))
    x2=x2+h2
x2=1.

A1=constroiAB(k1)
C1=constroiC(k1)
B1=constroiB(k1,A1,C1)
A2=constroiAM(k2)
C2=constroiC(k2)
B2=constroiB(k2,A2,C2)
W1=AB(B1,W1,x1,h1,k1,n1,lam)
W2=AM(B2,W2,x2,h2,k2,n2,lam)
print('X',X)
print('solucao exata W=',We)
print('A1=',A1,'\n','C1=',C1,'\n','B1=',B1,'\n','W1=',W1)
print('A2=',A2,'\n','C2=',C2,'\n','B2=',B2,'\n','W2=',W2)


linha1,=plt.plot( X, W1, label="Adams-Bashforth", color='orange')


linha2,=plt.plot( X, W2, label="Adams-Moulton", color='blue')
linha3,=plt.plot( X, We, label="Solucao exata", color='red')
plt.xlabel("x")
plt.ylabel("w(x)")
plt.legend(handles=[linha1, linha2,linha3])
#plt.legend(handles=[linha1, linha2])
plt.show()

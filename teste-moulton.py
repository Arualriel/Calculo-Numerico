#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 23:40:58 2019

@author: laura
"""

import numpy as np

def constroiA(k):
    A=np.zeros((k,k))
    A[0,:]=1
    for i in range(k):
        for j in range(k):
            if(i!=0)and(j!=0):
                A[i,j]=(-j)**i
    return A
def constroiC(k):    
    C=np.zeros((k,1))
    for i in range(k+1):
        if(i!=0):
            C[i-1,0]=1/i
    return C

def constroiB(k):
    B=np.linalg.solve(A,C)
    return B



def f(n,W,x,k,h):
    f=np.zeros((1,k))

    for i in range(k):
        f[0,i]=W[n-i,0]*x+1
        x=x+h
    return f
def soma(B,f,k):
    soma=0
    for i in range(k):
        soma=soma+f[0,i]*B[i,0]
    
    return soma
def faux(w,x,h):
    fa=w*x+1
    return fa
    
def Euler(w0,wj,x,h):
    wj=w0+h*faux(w0,x,h)
    return wj

def AM(B,W,x,h,k,n):
    wi=0
    for i in range(n):
        W[k+i,0]=Euler(W[k+i-1,0],W[k+i,0],x,h)
        wi=W[(k-1)+i,0]+h*soma(B,f(i+k,W,x,k,h),k)
        
        if(k+i<n+k):
            W[k+i,0]=wi
    return W
    

k=4
n=10

x0=1
x=x0
h=0.1
W=np.zeros((k+n,1))
W[0,0]=0.0

for i in range(1,k):
    W[i,0]=Euler(W[i-1,0],W[i,0],x,h)
    x=x+h


A=constroiA(k)
C=constroiC(k)
B=constroiB(k)
W=AM(B,W,x,h,k,n)
print('A=',A,'\n','C=',C,'\n','B=',B,'\n','W=', W)
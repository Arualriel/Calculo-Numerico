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



def f(n,W,k,h):
    f=np.zeros((1,k))

    for i in range(k):
        f[0,i]=W[n-i-1,0]-((n-i-1)*h)**2+1
        
    return f
def soma(B,f,k):
    soma=0
    for i in range(k):
        soma=soma+f[0,i]*B[i,0]
    
    return soma

def AB(B,W,h,k,n):
    wi=0
    for i in range(n):
        wi=W[(k-1)+i,0]+h*soma(B,f(i+k,W,k,h),k)
        
        if(k+i<n):
            W[(k-1)+i+1,0]=wi
    return W
    

k=4
n=10
#x0=0
h=0.2
W=np.zeros((k+n,1))
W[0,0],W[1,0],W[2,0],W[3,0]=0.5,0.8292933,1.2140762,1.6489220
#C=np.zeros((k,1))
#A=np.zeros((k,k))
#
#B=np.zeros((k,1))
A=constroiA(k)
C=constroiC(k)
B=constroiB(k)
W=AB(B,W,h,k,n)
print('A=',A,'\n','C=',C,'\n','B=',B,'\n','W=', W)
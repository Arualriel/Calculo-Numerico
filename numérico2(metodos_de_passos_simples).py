#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 01:18:32 2018

@author: laura
"""

import numpy as np


def f1(x1,w1):
    f=-w1+x1+1
   
    return f

def f2(x2,w2):
    f=w2+x2**2
    return f

def f3(x3,w3):
    f=x3*w3**2
    return f

def exata1emx(x):
    f=x+np.exp(-x)
    return f    

def exata2emx(x):
    f=-3*x-2+4*np.exp(x)
    return f

def exata3emx(x):
    f=-1/(((x**2)/2)-1)
    return f

def Erro(wj,wexato):
    erro=abs(wj-wexato)
    return erro

def Euler(wj,w,h,x):
    for i in range(n+1):
        #wj=w+h*f1(x,w)
        wj=(1+h/x)*w+h
        wj=float('%.6f'%(wj))
        wexato=float('%.6f'%(exata1emx(x)))
        erro=float('%.6f'%(Erro(w,wexato)))
        print("j=",i,"xj=",x,"w=",w,"wj=",wj,"wexato=",wexato,"erro=",erro)
        x=float('%.1f'%(x+h))
        w=wj
    return wj


def Pontomedio(wj,w,h,x):
    for i in range(n+1):
        wj=w+h*f2(x+(h/2),w+(h/2)*f2(x,w))
        wj=float('%.6f'%(wj))
        wexato=float('%.6f'%(exata2emx(x)))
        erro=float('%.6f'%(Erro(w,wexato)))
        print("j=",i,"xj=",x,"w=",w,"wj=",wj,"wexato=",wexato,"erro=",erro)
        x=float('%.1f'%(x+h))   
        w=wj    
    return wj


def Heun(wj,w,h,x):
    for i in range(n+1):
        wj=w+(h/2)*(f3(x,w)+f3(x+h,w+h*f3(x,w)))
        wj=float('%.6f'%(wj))
        wexato=float('%.6f'%(exata3emx(x)))
        erro=float('%.6f'%(Erro(w,wexato)))
        print("j=",i,"xj=",x,"w=",w,"wj=",wj,"wexato=",wexato,"erro=",erro)
        x=float('%.1f'%(x+h))
        w=wj    
    return wj


def EulerImplicito(wj,w,h,x):
    for i in range(n+1):
        wj=w+h*f1(x+h,w+h*f1(x,w))
        wj=float('%.6f'%(wj))
        wexato=float('%.6f'%(exata1emx(x)))
        erro=float('%.6f'%(Erro(w,wexato)))
        print("j=",i,"xj=",x,"w=",w,"wj=",wj,"wexato=",wexato,"erro=",erro)
        x=float('%.1f'%(x+h))
        w=wj    
    return wj

def PontomedioImplicito(wj,w,h,x):
    for i in range(n+1):
        wj=w+h*f2(x+(h/2),(2*w+h*f2(x,w))/2)
        wj=float('%.6f'%(wj))
        wexato=float('%.6f'%(exata2emx(x)))
        erro=float('%.6f'%(Erro(w,wexato)))
        print("j=",i,"xj=",x,"w=",w,"wj=",wj,"wexato=",wexato,"erro=",erro)
        x=float('%.1f'%(x+h))
        w=wj    
    return wj

def Trapezio(wj,w,h,x):
    for i in range(n+1):
        wj=w+(h/2)*(f3(x,w)+f3(x+h,w+h*f3(x,w)))
        wj=float('%.6f'%(wj))
        wexato=float('%.6f'%(exata3emx(x)))
        erro=float('%.6f'%(Erro(w,wexato)))
        print("j=",i,"xj=",x,"w=",w,"wj=",wj,"wexato=",wexato,"erro=",erro)
        x=float('%.1f'%(x+h))
        w=wj    
    return wj


n=10
h=0.1

x1=1
w1=0
wj1=w1

x2=0
w2=2
wj2=w2

x3=0
w3=1
wj3=w3


print ("Euler,f1",Euler(wj1,w1,h,x1))
print ("Ponto medio,f2",Pontomedio(wj2,w2,h,x2))
print ("Heun,f3",Heun(wj3,w3,h,x3))
print ("Euler implicito,f1",EulerImplicito(wj1,w1,h,x1))
print ("Ponto medio implicito,f2",PontomedioImplicito(wj2,w2,h,x2))
print ("Trapezio,f3",Trapezio(wj3,w3,h,x3))
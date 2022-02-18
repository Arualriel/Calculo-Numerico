# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 15:19:49 2017

@author: lauracpm
"""
import numpy as np
num =1.5
erro=10
e=10**(-5)

print(num)
i=0
while(erro>e):
    n=num-(1.0*num**3 - 5.25*num + 3.125)/(3.0*num**2-5.25)
    
    erro=np.abs(n-num)/np.abs(n)
    print("n=",i,"y=",num,"f(y)=",1.0*num**3 - 5.25*num + 3.125,"erro=",erro)
    
    num=n
    i=i+1

print("i=",i,"y=",num,"f(y)=",1.0*num**3 - 5.25*num + 3.125,"erro=",erro)

#d=0
#
#r=1
#for i in 20:
#   d= num
#   r= 
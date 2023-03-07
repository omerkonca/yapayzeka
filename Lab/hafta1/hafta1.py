# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:25:18 2019

@author: Emrullah
"""

import numpy as np

print("Selam Dünya")

a= np.array([1,2,3])

print(a)

logaritma = np.log(a)

print(logaritma)

ortalama= np.mean(a)
print(ortalama)

b= np.array([[1,2,3],[4,5,6]])
print(b)

transpoz= np.transpose(b)
print(transpoz)

b.shape

sil= np.delete(b,[5])
print(sil)





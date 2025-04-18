# -*- coding: utf-8 -*-
"""hw4-python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nuI-Z6LDUVXm0Jst3MljAwbOe5ycLWrm
"""

tup=('A','B')
tup2=('C',)
tup+=tup2
print(tup)

import numpy as np
n =int(input())
A=np.zeros((n,n))
for i in range(n):
  for j in range(n):
    A[i,j]=i*n+j+1
print(A)

B=A.reshape(-1,)
print(B)

import cv2
frame=cv2.imread("Lenna.png",cv2.COLOR_BGR2RGB)

frame1=np.expand_dims(frame,0)
frame2=np.permute_dims(frame1,(0,3,1,2))
print('original',frame.shape)

print('expand dims',frame1.shape)
print('transpose',frame2.shape)
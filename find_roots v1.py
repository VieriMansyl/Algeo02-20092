# -*- coding: utf-8 -*-
"""Copy of Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GZI-DgZjC-as83o7iDoXM01YgVFa4rkd
"""

import numpy as np
from sympy import symbols, Matrix, Symbol, Poly
from sympy.polys.groebnertools import sig
import math

def lambdaMat(mat , need):
  newMat = []
  for i in range(len(mat)):
    newMat.append(np.array(mat[i]) * -1)
    newMat[i][i] = need + newMat[i][i]
    
  return newMat

def find_roots(Mat):
  aat = np.matmul(Mat , np.transpose(Mat))
  need = Symbol('l')

  matAll = Matrix(lambdaMat(aat , need))
  deter = matAll.det()
  print(matAll.det())

  koef = Poly(deter).all_coeffs()
  print(koef)

  root = np.roots(koef)
  root.sort()
  root = root[::-1]
  print(root)

  sigma = []
  for each in root:
      if(each >= 0):
          sigma.append(each**(0.5))

  newsigma = np.array(sigma)

  return root, newsigma

a = [[1,2,3],[4,5,6],[7,8,9]]
root , newsigma = find_roots(a)
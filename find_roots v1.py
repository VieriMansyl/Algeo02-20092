# -*- coding: utf-8 -*-

import numpy as np
from sympy import symbols, Matrix, Symbol, Poly
from sympy.polys.groebnertools import sig
import math

#makeTransMat -> membentuk matriks AAt / AtA
#typeMat = 0 -> membentuk AAt
#typeMat = 1 -> membentuk AtA
def makeTransMat(mat , typeMat):
  if(typeMat == 0):
    return np.matmul(mat , np.transpose(mat))
  else:
    np.matmul(np.transpose(mat) , mat)

#lambdaMat -> untuk menghasilkan matriks (λI - AAt)
def lambdaMat(mat , need):
  newMat = []
  for i in range(len(mat)):
    newMat.append(np.array(mat[i]) * -1)
    newMat[i][i] = need + newMat[i][i]
  
    
  return newMat

#find_roots -> menghasilkan akar-akar  (a.k.a. nilai eigen) dari matriks Mat
def find_roots(mat):
  aat = makeTransMat(mat,0)
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


#Test case
a = [[1,2,3],[4,5,6],[7,8,9]]
root , newsigma = find_roots(a)

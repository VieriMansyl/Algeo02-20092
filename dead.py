import numpy as np
from sympy import symbols, Matrix, Symbol, Poly
from sympy.polys.groebnertools import sig
import math

need = Symbol('l')

a = np.array([need - 10 , 0, -2])
b = np.array([0, need - 10, -4])
c = np.array([-2, -4, need - 2])

all = [a, b, c]
matAll = Matrix(all)
deter = matAll.det()
print(deter)

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
#Perhatiin buat rootnya (desimalnya)
print(newsigma)

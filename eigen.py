'''
README

File ini berisi fungsi dan prosedur yang diperlukan untuk mencari nilai eigen.
	1. fungsi rounding, akan melakukan pembulatan kepada nilai floating point dengan toleransi 1e-12
	2. fungsi convRootEig, akan melakukan pemilihan dari akar-akar persamaan menjadi nilai eigen dan sigma
	3. fungsi convDet, akan menerima sebuah persamaan determinan, yang kemudian akan dicari akar-akarnya dengan memanfaatkan 
	bantuan library sympy
	4. fungsi findDeter, akan menerima sebuah matriks (AAT atau ATA) dan variabel, kemudian akan membentuk matriks lambdaI - AAT 
	atay matriks lambdaI - ATA kemudian dicari determinannya dengan memanfaatkan sympy. Perlu diperhatikan bahwa matriks dan persamaan
	yang dikembalikan akan berbentuk persamaan dengan memanfaatkan Symbol di sympy
'''
import copy
import numpy as np
from numpy.core.fromnumeric import sort
import sympy as sy
from sympy import det
import math

def rounding(val):	
	valRound = round(val)	
	
	#Toleransi : 1e-9
	if(math.isclose(val, valRound, rel_tol=1e-9)):
		val = valRound
		
	return val

#Menerima Koefisien Persamaan, kemudian dicari akar-akarnya
def convEigSig(rawroot, rawvec):
	# print("RAW")
	# print(rawroot)
	rawvecT = np.transpose(rawvec)
	newroot = []
	newsigma = []
	newvec = []

	for i in range(len(rawroot)):
		if(rawroot[i] > 0):
			newroot.append(rounding(rawroot[i]))
			newsigma.append((rounding(rawroot[i]) ** 0.5))
			newvec.append(rawvecT[i])
		elif(math.isclose(rawroot[i], 0, abs_tol = 1e-9)):
			newroot.append(0)
			newvec.append(rawvecT[i])

	return newroot, newsigma, newvec

def findEigen(mat):
	pq = np.eye(mat.shape[0])
	dummy = copy.deepcopy(mat)
	dummy1 = []

	for i in range(100):
		q, r = np.linalg.qr(dummy)
		pq = np.dot(pq, q)
		dummy1 = np.dot(r, q)

		similar = True
		for j in range(len(dummy)):
			if(not math.isclose(dummy[j][j], dummy1[j][j], rel_tol=1e-12)):
				similar = False
				break
		if(similar):
			break
		else:
			dummy = copy.deepcopy(dummy1)
	
	return  np.diag(dummy1), pq

# arr = np.array([[3,1,1],[-1,3,1]])



# pq, val = findEigen(np.matmul(arr, np.transpose(arr)))
# pq1,val1 = findEigen(np.matmul(np.transpose(arr), arr))
# print(val)
# print(pq)

# print(pq1)
# print(val1)
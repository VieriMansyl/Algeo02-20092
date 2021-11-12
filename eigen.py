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
def convEigSig(rawroot):
	# print("RAW")
	# print(rawroot)
	newroot = []
	newsigma = []

	for root in rawroot:
		if(root > 0):
			newroot.append(rounding(root))
			newsigma.append((rounding(root) ** 0.5))
		elif(root == 0):
			if(0 not in newsigma):
				newroot.append(0)

	return newroot, newsigma

def findEigen(mat):
	dummy = copy.deepcopy(mat)
	dummy1 = []

	while True:
		q, r = np.linalg.qr(dummy)
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
	
	return np.diag(dummy1)
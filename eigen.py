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

import numpy as np
import sympy as sy
import math

def rounding(val):	
	valRound = round(val)	
	
	#Toleransi : 1e-9
	if(math.isclose(val, valRound, rel_tol=1e-12)):
		val = valRound
		
	return val

#Menerima Koefisien Persamaan, kemudian dicari akar-akarnya
def convRootEig(rawroot):
	newroot = []
	newsigma = []

	for root in rawroot:
		if(root > 0):
			newroot.append(rounding(root))
			newsigma.append(rounding(root) ** 0.5)
		elif(root == 0):
			if(0 not in newsigma):
				newroot.append(0)
				newsigma.append(0)

	return newroot, newsigma


#Menerima Persamaan Determinan, diubah menjadi koefisien
def convDet(determinant):
	koef = sy.Poly(determinant).all_coeffs()  # Create koeficient lienar equation

	froot = np.roots(koef)  # Cari akar-akar persamaan

	# Sort descending
	froot.sort()

	froot = froot[::-1]

	eigenval, sigmaval = convRootEig(froot)
	return eigenval, sigmaval


#Mencari persamaan determinan dan mengembalikan 
def findDeter(matT, vars):

	all = []
	for i in range(len(matT)):
		each = []
		for j in range(len(matT[0])):
			if(i == j):
				each.append(vars - matT[i][j])  # ngisi kalau diagonal
			else:
				each.append(-matT[i][j])  # ngisi selain diagonal

		npeach = np.array(each)  # Convert ke np array
		all.append(npeach)

	matAll = sy.Matrix(all)
	deter = matAll.det()

	return matAll, deter


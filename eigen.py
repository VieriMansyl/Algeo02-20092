#Tool untuk mencari nilai eigen dan sigma

import numpy as np
import sympy as sy
import scipy as sc

def rounding(val):
	cekRound = 0.00000000001		#10^-12
	valRound = round(val)
	
	if((valRound  - val) < cekRound):
		val = valRound
		
	return val

#Menerima Koefisien Persamaan, kemudian dicari akar-akarnya
def convKoefRoot(rawroot):
	newroot = []
	newsigma = []

	for root in rawroot:
		if(root > 0):
			newroot.append(rounding(root))
			newsigma.append(rounding(root ** 0.5))
		elif(root == 0):
			if(0 not in newsigma):
				newroot.append(rounding(root))
				newsigma.append(rounding(root ** 0.5))

	sigma = np.array(newsigma)
	finalroot = np.array(newroot)

	return newroot, newsigma


#Menerima Persamaan Determinan, diubah menjadi koefisien
def convDet(determinant):
	koef = sy.Poly(determinant).all_coeffs()  # Create koeficient lienar equation

	froot = np.roots(koef)  # Cari akar-akar persamaan

	# Sort descending
	froot.sort()

	froot = froot[::-1]

	eigenval, sigmaval = convKoefRoot(froot)
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


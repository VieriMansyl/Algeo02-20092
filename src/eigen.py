'''
README

File ini berisi fungsi dan prosedur yang diperlukan untuk mencari nilai eigen.
	1. fungsi rounding, akan melakukan pembulatan kepada nilai floating point dengan toleransi 1e-9
	2. fungsi convRootEig, akan melakukan pemilihan dari akar-akar persamaan menjadi nilai eigen dan sigma
'''
import copy
import numpy as np
from numpy.core.fromnumeric import sort
#import sympy as sy
#from sympy import det
import math

def rounding(val):	
	valRound = round(val)	
	
	#Toleransi : 1e-9
	if(math.isclose(val, valRound, rel_tol=1e-9)):
		val = valRound
		
	return val

#Menerima Koefisien Persamaan, kemudian dicari akar-akarnya
def convEigSig(rawroot, rawvec):
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

def findEigen(mat, maxiter):
	pq = np.eye(mat.shape[0])
	dummy = copy.deepcopy(mat)
	dummy1 = []

	for i in range(maxiter):
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

def createSigmaMat(sigma, nrow, ncol):
	sigmaMat = []

	for i in range(nrow):
		eachRow = []
		for j in range(ncol):
			if(i == j):
				eachRow.append(sigma[i])
			else:
				eachRow.append(0)
		sigmaMat.append(eachRow)

	return sigmaMat

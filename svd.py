import numpy as np
import sympy as sy
import scipy as sc
import copy


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


def createFinalMat(value, mat, neff, var):
	copyMat = copy.deepcopy(mat)
	for i in range(neff):
		const = copyMat[i][i] - var  # Get constanta
		copyMat[i][i] = value + const #Convert every diagonal
		copyMat[i].append(0)
		
	return copyMat


# membentuk matriks singular (pembentuk matriks U dan V)
def makeMatEigen(mat, matEigen):

	transpose_solusi = np.transpose(mat)

	for i in range(1, len(mat[0])):
		if(transpose_solusi[i][len(transpose_solusi[i]) - 1] == 1):
			newVector = transpose_solusi[i][0:(len(transpose_solusi[i]) - 1)]
			normalize(newVector, len(newVector))
			matEigen.append(newVector)
	
	return matEigen

def normalize(basis, neff):
	length = 0
	for val in basis:
		length += val ** 2

	length = length ** 0.5

	for i in range(neff):
		basis[i] /= length
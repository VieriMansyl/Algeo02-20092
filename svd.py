'''
README

File ini berisi fungsi dan prosedur yang diperlukan untuk membentuk matriks-matriks SVD
	1. fungsi createSigmaMat, akan menerima 3 argumen, sigma (array berisi sigma dari AAT), nrow adalah banyak baris, dan ncol adalah banyak kolom.
	Kemudian, akan dibuat matriks Sigma dari SVD
	2.fungsi createFinalMat, akan menerima 4 argumen, value(nilai eigen), mat(Matriks yang masih berupa lambdaI -AAT atau ATA,
	lambda yang berbentuk Symbol akan diganti menjadi nilai value), neff (ukuran efektif matriks), var (variabel Symbol yang digunakan).
	Fungsi ini akan mengembalikan mat yang sudah diganti variabelnya menjadi value
	3.fungsi makeMatEigen, akan menerima 2 argumen, mat(matriks yang berisi nilai parameter dari Gauss), dan matEigen(matriks yang berisi kondisi U atau V sekarang)
	Fungsi ini akan mengembalikan matEigen yang sudah ditambahin basisnya
	4.fungsi normalize, akan menerima 2 argumen, yaitu basis (sebuah vektor basis), neff( banyak elemen di vektor basis).
	Fungsi ini akan mengembalikan vektor basis yang sudah dinormalisasi
'''


import numpy as np
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


def createFinalMat(value, mat, nrow, ncol):
	copyMat = []
	for i in range(nrow):
		eachrow = []
		for j in range(ncol):  # Get constanta
			if(i == j):
				eachrow.append(value - mat[i][i]) #Convert every diagonal
			else:
				eachrow.append(-mat[i][j])
		eachrow.append(0)
		copyMat.append(eachrow)
				
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
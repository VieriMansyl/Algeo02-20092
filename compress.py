import copy
import cv2 as cv
import numpy as np
import sympy as sy
import scipy as sc
import math
import time

import eigen
import gauss
import svd


# image = directory foto => "Folder_ini/static/ini_foto.png"
# compression_rate = xx%

# Fungsi compress ini nantinya mengkompress foto
# lalu hasilnya disimpan dalam folder static
# dan me-return directory dari foto tersebut
def compress(image, compression_rate):
	start = time.time()			# End

	# return("static/hasil.png")
	src = cv.imread(image, cv.IMREAD_ANYCOLOR)

	b, g, r = np.split(src)	 # b, g, r masing-masing channel
	
	bfinal = process(b, compression_rate)
	gfinal = process(g, compression_rate)
	rfinal = process(r, compression_rate)

	finalsrc = np.stack(bfinal, gfinal, rfinal, axis = 0)

	cv.imwrite(image, finalsrc)
	end = time.time()
	delta = start - end
	return delta

#cr -> compression reate
#Asumsi mat -> m * n
def process(mat,cr):
	
	matT = np.transpose(mat)

	nrow = mat.shape[0] # m 
	ncol = mat.shape[1] # n
	
	var = sy.Symbol('x')
	
	# Untuk ATA
	matAll, matDet = eigen.findDeter(np.matmul(matT, mat), var)

	listAll = matAll.tolist()

	eig, sig = eigen.convDet(matDet) #Eigenvalue dan sigma untuk ATA

	sigmaMat = svd.createSigmaMat(sig, nrow, ncol) #Matriks Sigma, berbentuk list biasa

	matU = [] #Basis yang udah di normalisasi 
	matV = []

	for val in eig:

		matFinal = svd.createFinalMat(val, listAll, ncol, var)
		reducedMat = gauss.makeGauss(matFinal) #Matriks Baris 
		solGauss = gauss.getValue(reducedMat)
		matV = svd.makeMatEigen(solGauss, matV)
	
	return matV, sigmaMat

arr = [[3,1,1],
	   [-1,3,1]]

matArr = sy.Matrix(arr)
mu, sig = process(matArr, 10)
print(mu)
print(sig)
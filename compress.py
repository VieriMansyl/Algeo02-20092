import cv2 as cv
import numpy as np
import sympy as sy
import math
import time


import eigen
import gauss
import svd

'''
README

1. compress(image, compression_rate)	: konversi image menjadi 3 matriks R,G,B
3. findK(cr)							: mencari nilai k dari conversion rate
2. process(mat,cr)						: dekomposisi matriks mengikuti metode SVD (U∑Vt)
'''


# image = directory foto => "Folder_ini/static/ini_foto.png"
# compression_rate = xx%

# Fungsi compress ini nantinya mengkompress foto
# lalu hasilnya disimpan dalam folder static
# dan me-return directory dari foto tersebut
def compress(image, compression_rate):
	start = time.time()			# End

	# return("static/hasil.png")
	src = cv.imread(image, cv.IMREAD_ANYCOLOR)

	b, g, r = cv.split(src)	 # b, g, r masing-masing channel
	
	bfinal = process(b, compression_rate)
	gfinal = process(g, compression_rate)
	rfinal = process(r, compression_rate)
	
	finalsrc = np.dstack([bfinal, gfinal, rfinal])

	cv.imshow("", finalsrc)
	key = cv.waitKey(0)

	if(key == ord('c')):
		cv.destroyAllWindows()

	# cv.imwrite(image, finalsrc)
	end = time.time()
	delta = start - end
	# return delta


def findK(cr, singVal):
	k = (cr/100) * singVal
	#Tentuin sistem Rounding
	return round(k)

#cr -> compression reate
#Asumsi mat -> m * n
def process(mat , cr):

	matT = np.transpose(mat)
	nrow = mat.shape[0] # m 
	ncol = mat.shape[1] # n
	
	var = sy.Symbol('x')
	
	#Untuk AAT
	matAll1, matDet1 = eigen.findDeter(np.matmul(mat, matT), var)
	listAll1 = matAll1.tolist()
	eig1, sig1 = eigen.convDet(matDet1) #Eigenvalue dan sigma untuk AAT

	#Untuk ATA
	matAll2, matDet2 = eigen.findDeter(np.matmul(matT, mat), var)
	listAll2 = matAll2.tolist()
	eig2, sig2 = eigen.convDet(matDet2) #Eigenvalue dan sigma untuk ATA
	# m x n = 5 x 4
	# u = 5 x 5 = 5 x 4   5 x 4
	# sig =  = k x k 4 x 4
	# v = 3 x 3 = k x n 4 x 4


	if(0 in sig2):
		k = findK(cr, len(sig2) - 1)
	else:
		k = findK(cr, len(sig2))
		
	sigmaMat = svd.createSigmaMat(sig2, k, k) #Matriks Sigma, berbentuk list biasa

	matU = [] #Basis yang udah di normalisasi 
	matV = [] 

	#Untuk Matriks U
	for val1 in eig1:
		matFinal = svd.createFinalMat(val1, listAll1, nrow, var)
		reducedMat = gauss.makeGauss(matFinal) #Matriks Baris 
		solGauss = gauss.getValue(reducedMat)
		matU = svd.makeMatEigen(solGauss , matU)
		if (len(matU) == k):
			break
		elif(len(matU) > k):
			matU = matU[:k]
			break
		
	#Untuk Matriks V
	for val2 in eig2:
		matFinal = svd.createFinalMat(val2, listAll2, ncol, var)
		reducedMat = gauss.makeGauss(matFinal) #Matriks Baris 
		solGauss = gauss.getValue(reducedMat)
		matV = svd.makeMatEigen(solGauss , matV)
		if (len(matV) == k):
			break
		elif(len(matV) > k):
			matV = matV[:k]
			break

	return multiplyMat(np.transpose(matU) , sigmaMat ,  matV)

def multiplyMat(mu, sig, mv):
	mul1 = np.matmul(mu, sig)
	mul2 = np.matmul(mul1, mv)
	return mul2



compress("balls.jpeg", 100)





# arr = [[3,1,1],
# 	   [-1,3,1]]

# matArr = sy.Matrix(arr)
# mu, mv, sig = process(matArr, 75)
# print("ini mu :")
# for line in mu:
# 	print(line)
# print("\nini sig :")
# for line in sig:
# 	print(line)
# print("\nini mv :")
# for line in mv:
# 	print(line)

# mul1 = np.matmul(mu, sig)
# mul2 = np.matmul(mul1, mv)
# print(type(mul2))

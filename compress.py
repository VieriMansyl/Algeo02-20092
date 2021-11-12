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
	print(type(b))
	print(g)
	print(r)

	blist = b.tolist()
	glist = g.tolist()
	rlist = r.tolist()
	bfinal = process(np.array(blist), compression_rate)*(1/255)
	gfinal = process(np.array(glist), compression_rate)*(1/255)
	rfinal = process(np.array(rlist), compression_rate)*(1/255)

	print(bfinal)
	print(gfinal)
	print(rfinal)

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

	matAAT = np.matmul(mat, matT)
	matATA = np.matmul(matT, mat)

	# print(matAAT)
	finalAAT = matAAT.tolist()
	finalATA = matATA.tolist()


	raweig1 = eigen.findEigen(matAAT)
	# print(raweig1)
	# print("Eigen 1")
	raweig2 = eigen.findEigen(matATA)
	# print(raweig2)
	# print("Eigen 2")

	eig1, sig1 = eigen.convEigSig(raweig1)
	eig2, sig2 = eigen.convEigSig(raweig2)

	# print(eig1)
	# print(eig2)
	# print(sig2)

	k = findK(cr, len(sig2))

	sigmaMat = svd.createSigmaMat(sig2, k, k) #Matriks Sigma, berbentuk list biasa
	# for line in sigmaMat:
	# 	print(line)
	# print("Sigma")
	matU = [] #Basis yang udah di normalisasi
	matV = []

	#Untuk Matriks U
	for val1 in eig1:
		matFinal = svd.createFinalMat(val1, finalAAT, nrow, nrow)
		# for line in matFinal:
		# 	print(line)

		reducedMat = gauss.makeGauss(matFinal) #Matriks Baris

		# for line in reducedMat:
		# 	print(line)
		solGauss = gauss.getValue(reducedMat)
		matU = svd.makeMatEigen(solGauss , matU)
		if (len(matU) == k):
			break
		elif(len(matU) > k):
			matU = matU[:k]
			break
	print("U")
	#Untuk Matriks V
	for val2 in eig2:
		matFinal = svd.createFinalMat(val2, finalATA, ncol, ncol)
		reducedMat = gauss.makeGauss(matFinal) #Matriks Baris
		solGauss = gauss.getValue(reducedMat)

		matV = svd.makeMatEigen(solGauss , matV)
		if (len(matV) == k):
			break
		elif(len(matV) > k):
			matV = matV[:k]
			break
	print("v")

	return multiplyMat(np.transpose(matU) , sigmaMat ,  matV)


def multiplyMat(mu, sig, mv):
	mul1 = np.matmul(mu, sig)
	mul2 = np.matmul(mul1, mv)
	return mul2



compress("static/10x10.jpg", 100)
# m x k
# k x k
# k X n

# 2 x 3

# arr = [[3,1,1],
# 	   [-1,3,1]]

# matArr = sy.Matrix(arr)
# mu, sig, mv= process(matArr, 100)
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
# print(mul2)


# arr1 = [[223, 219, 216, 215, 215, 216, 216],
# 	[238, 224, 208, 201, 212, 223, 228],
# 	[251, 216, 177, 162, 182, 216, 241],
# 	[251, 194, 134, 116, 134, 192, 246],
# 	[251, 201, 153, 146, 153, 200, 250],
# 	[253, 209, 156, 129, 156, 209, 253],
# 	[255, 213, 143,  87, 143, 213, 255]]

# arr2 = [[223, 219, 216, 215, 215, 216, 216],
# 	[238, 224, 208, 200, 212, 223, 228],
# 	[251, 216, 178, 163, 183, 216, 241],
# 	[251, 195, 137, 119, 136, 193, 246],
# 	[251, 202, 156, 149, 156, 202, 250],
# 	[253, 211, 160, 136, 160, 211, 253],
# 	[255, 214, 148, 97, 148, 214, 255]]

# arr3 = [[223, 219, 216, 215, 215, 216, 216],
#  [238, 224, 207, 200, 211, 222, 228],
#  [251, 217, 180, 166, 184, 216, 241],
#  [251, 197, 143, 129, 143, 195, 246],
#  [251, 204, 162, 159, 162, 204, 250],
#  [253, 213, 169, 153, 169, 213, 253],
#  [255, 217, 162, 125, 162, 217, 255]]

# ans1 = process(np.array(arr1), 100)
# ans2 = process(np.array(arr2), 100)
# ans3 = process(np.array(arr3), 100)
# print(ans1)
# print(ans2)
# print(ans3)

# src = np.dstack([ans1, ans2, ans3])

# cv.imshow("", src)
# key = cv.waitKey(0)

# if(key == ord('c')):
# 	cv.destroyAllWindows()
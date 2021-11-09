import cv2 as cv
import numpy as np
import time
from numpy.core.defchararray import upper
from scipy import linalg
from sympy import symbols, Matrix, Symbol, Poly
from scipy.linalg import lu
from sympy.polys.groebnertools import sig
import math


# image = directory foto => "Folder_ini/static/ini_foto.png"
# compression_rate = xx%

# Fungsi compress ini nantinya mengkompress foto
# lalu hasilnya disimpan dalam folder static
# dan me-return directory dari foto tersebut
def compress(image, compression_rate):
	start = time.time()
	print("Start")				# Start
	print(compression_rate)		# 70
	print(image)				# static\lenna.png
	print("End")				# End

	# return("static/hasil.png")
	src = cv.imread(image, cv.IMREAD_ANYCOLOR)

	b, g, r = np.split(src)	 # b, g, r masing-masing channel

	# bt = np.transpose(b)  # Transpose b, g, r
	# gt = np.transpose(g)
	# rt = np.transpose(r)

	# Untuk AAT
	# broot1, bsigma1 = findroots(np.matmul(b, bt))
	# groot1, gsigma1 = findroots(np.matmul(g, gt))
	# rroot1, rsigma1 = findroots(np.matmul(r, rt))

	# # Untuk ATA
	# broot2, bsigma2 = findroots(np.matmul(bt, b))
	# groot2, gsigma2 = findroots(np.matmul(gt, g))
	# rroot2, rsigma2 = findroots(np.matmul(rt, r))

	



	end = time.time()
	delta = start - end
	return delta

# def findroots(matT):

# 	vars = Symbol('x')  # Variabel yang dipakai

# 	all = []
# 	for i in range(len(matT)):
# 		each = []
# 		for j in range(len(matT[0])):
# 			if(i == j):
# 				each.append(vars - matT[i][j])  # ngisi kalau diagonal
# 			else:
# 				each.append(-matT[i][j])  # ngisi selain diagonal

# 		npeach = np.array(each)  # Convert ke np array
# 		all.append(npeach)

# 	matAll = Matrix(all)
# 	deter = matAll.det()

# 	return convDetKoef(deter)


# def convDetKoef(determinant):
# 	koef = Poly(determinant).all_coeffs()  # Create koeficient lienar equation

# 	froot = np.roots(koef)  # Cari akar-akar persamaan

# 	# Sort descending
# 	froot.sort()

# 	froot = froot[::-1]
# 	return convKoefRoot(froot)

# # Convert Koeficient to Root and Sigma


# def convKoefRoot(rawroot):
# 	newroot = []
# 	newsigma = []

# 	for root in rawroot:
# 		if(root > 0):
# 			newroot.append(root)
# 			newsigma.append(root ** 0.5)
# 		elif(root == 0):
# 			if(0 not in newsigma):
# 				newroot.append(root)
# 				newsigma.append(root ** 0.5)

# 	sigma = np.array(newsigma)
# 	finalroot = np.array(newroot)

# 	return newroot, newsigma


# # makeTransMat -> membentuk matriks AAt / AtA
# # typeMat = 0 -> membentuk AAt
# # typeMat = 1 -> membentuk AtA
# def makeTransMat(mat, typeMat):
# 	if(typeMat == 0):
# 		return np.matmul(mat, np.transpose(mat))
# 	else:
# 		return np.matmul(np.transpose(mat), mat)


# # lambdaMat -> untuk menghasilkan matriks (λI - AAt)
# def lambdaMat(mat, need):
# 	newMat = []
# 	for i in range(len(mat)):
# 		newMat.append(np.array(mat[i]) * -1)
# 		newMat[i][i] = need + newMat[i][i]

# 	return newMat


# '''*********************************Gauss*********************************'''

# # mencari baris dengan 1 utama di kolom yang berkorespondesi pada baris tersebut


# def getRowMain(mat, i):
# 	found1Utama = False
# 	row = i+1

# 	while (row > 0 and not(found1Utama)):
# 		row -= 1
# 		col = 0
# 		nonZero = False

# 	while (col <= i-1 and not(nonZero)):
# 		if(mat[row][col] != 0):
# 			nonZero = True
# 		else:
# 			col += 1

# 	if (not(nonZero) and (mat[row][col] == 1)):
# 		found1Utama = True

# 	if ((row == 0) and not (found1Utama)):
# 		row = 999
# 	return row

# # mengembalikan nilai tiap variabel (x1,x2,...x ke-n) bersesuaian pada matriks


# def getValue(mat):
# 	idx_UNDEF = 999
# 	paramCol = 0

#   # inisialisasi matriks solusi -> menyimpan nilai konstanta berserta keof. parameternya
# 	solusi = [[0 for i in range(len(mat[0]))] for j in range(len(mat[0]))]

# 	# Kalau baris paling bawah 1, berarti dia kepake parameternya (atau nggak full 0)
# 	for i in range(len(mat)-1, -1, -1):  # dari X ke-n s.d. X1
# 		if (getRowMain(mat, i) == idx_UNDEF):
# 			paramCol += 1
# 			solusi[i][paramCol] = 1
# 			solusi[len(solusi) - 1][paramCol] = 1
# 		else:
# 			rowMain = getRowMain(mat, i)
# 			# C , p , q , dst (C : constant ; p,q,... : parameter)
# 			for j in range(0, paramCol + 1):
# 				for k in range(i+1, len(mat), 1):
# 					solusi[i][j] -= mat[rowMain][k] * solusi[k][j]

# 	return solusi

# # mengembalikan matriks berisikan vektor-vektor eigen

# def solveGauss(mat):
# 	upperMat, pivot = mat.rref() 

# 	"""
# 	lowMat, upperMat = lu(mat, permute_l=True)
# 	x = len(upperMat)
# 	for i in range(len(upperMat)):
# 		divisor = upperMat[i][i]
# 		if(divisor != 0):
# 			for j in range(i, len(upperMat[0])):
# 				upperMat[i][j] /= divisor
# 	"""
# 	upperT = np.transpose(upperMat)

# 	added = [0.0 for i in range(len(upperT[0]))]
# 	# Error di append
# 	appended = np.append(upperT, [added], axis=0)

# 	newUpper = np.transpose(appended)

# 	solusi = getValue(newUpper)

# 	return solusi


# '''***************************Vektor Eigen***************************'''


# def findFinalMat(value, matT):
# 	all = []
# 	for i in range(len(matT)):
# 		each = []
# 		for j in range(len(matT[0])):
# 			if(i == j):
# 				each.append(value - matT[i][j])  # ngisi kalau diagonal
# 			else:
# 				each.append(-matT[i][j])  # ngisi selain diagonal
# 		npeach = np.array(each)  # Convert ke np array
# 		all.append(npeach)

# 	matAll = Matrix(all)
# 	return matAll


# # membentuk matriks singular (pembentuk matriks U dan V)
# def makeMatEigen(mat, matEigen):
# 	transpose_solusi = np.transpose(mat)
# 	for i in range(1, len(mat[0])):
# 		if(transpose_solusi[i][len(transpose_solusi[i]) - 1] == 1):
# 			newVector = transpose_solusi[i][0:(len(transpose_solusi[i]) - 1)]
# 			matEigen.append(newVector)

# 	return matEigen


# '''***************************Vektor Eigen***************************'''
# # createUEVt -> membentuk U dan ∑ dan V
# # typeSingular = 0 -> membentuk U dan ∑
# # typeSingular = 1 -> membentuk V


# def createUEVt(mat, typeSingular):
# 	if(typeSingular == 0):  # AAT
# 		matT = np.matmul(mat, np.transpose(mat))
# 	else:  # ATA
# 		matT = np.matmul(np.transpose(mat), mat)

# 	roots, sigma = findroots(matT)
# 	matEigen = []

# 	# membentuk matriks vektor eigen / matriks singular
# 	# roots -> array isinya lambda, buat diap lambda butuh cari basis eigen
# 	#roots = [a,b,c,d]
# 	for root in roots:
# 		finalbanget = findFinalMat(root, matT)
# 		solusi = solveGauss(finalbanget)
# 		matEigen = makeMatEigen(solusi, matEigen)

# 	matE = Matrix(matEigen)

# 	# membentuk matriks ∑
# 	matSigma = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
# 	count = 0
# 	while (count < len(sigma)):
# 		matSigma[count][count] = sigma[count]
# 		count += 1

# 	# membentuk matriks transpose Vt untuk matriks singular V
# 	if(typeSingular == 1):
# 		matE = np.transpose(matE)

# 	return matE, matSigma


# '''***********************************SVD***********************************'''
# # test case
# mat = [[1, 2, 3],
# 	   [4, 5, 6],
# 	   [7, 8, 9],
# 	   [10, 11, 12]]

# for i in range(0, 2, 1):
# 	# i == 0 -> U (4x4), sigma (4x3) 
# 	# i == 1 -> v (3x3)

# 	matEigen, matSigma = createUEVt(mat, i)

# 	print("OKE")
# 	if(i == 0):
# 		print(matEigen)
# 	else:
# 		for line in matEigen:
# 			print(line)

# 	print("Check")
# 	for line in matSigma:
# 		print(line)


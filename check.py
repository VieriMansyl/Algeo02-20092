import numpy as np
import sympy as sy
import scipy as sc
# import gauss

def findroots(matT):

	vars = sy.Symbol('x')  # Variabel yang dipakai

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

	return convDetKoef(deter)


def convDetKoef(determinant):
	koef = sy.Poly(determinant).all_coeffs()  # Create koeficient lienar equation

	froot = np.roots(koef)  # Cari akar-akar persamaan

	# Sort descending
	froot.sort()

	froot = froot[::-1]
	return convKoefRoot(froot)

# Convert Koeficient to Root and Sigma


def convKoefRoot(rawroot):
	newroot = []
	newsigma = []

	for root in rawroot:
		if(root > 0):
			newroot.append(root)
			newsigma.append(root ** 0.5)
		elif(root == 0):
			if(0 not in newsigma):
				newroot.append(root)
				newsigma.append(root ** 0.5)

	sigma = np.array(newsigma)
	finalroot = np.array(newroot)

	return newroot, newsigma

def findFinalMat(value, matT):
	all = []
	for i in range(len(matT)):
		each = []
		for j in range(len(matT[0])):
			if(i == j):
				each.append(value - matT[i][j])  # ngisi kalau diagonal
			else:
				each.append(-matT[i][j])  # ngisi selain diagonal
		npeach = np.array(each)  # Convert ke np array
		all.append(npeach)

	matAll = sy.Matrix(all)
	return matAll

def getValue(mat):
	idx_UNDEF = 999
	paramCol = 0

	nrow = mat.shape[0]
	ncol = mat.shape[1]

  # inisialisasi matriks solusi -> menyimpan nilai konstanta berserta keof. parameternya
	solusi = [[0 for i in range(ncol)] for j in range(nrow + 1)]

	# Kalau baris paling bawah 1, berarti dia kepake parameternya (atau nggak full 0)
	for i in range(nrow-1, -1, -1):  # dari X ke-n s.d. X1
		if (getRowMain(mat, i) == idx_UNDEF):
			paramCol += 1
			solusi[i][paramCol] = 1
			solusi[nrow][paramCol] = 1
		else:
			rowMain = getRowMain(mat, i)
			# C , p , q , dst (C : constant ; p,q,... : parameter)
			for j in range(0, paramCol + 1):
				for k in range(i+1, nrow, 1):
					solusi[i][j] -= mat[rowMain, k] * solusi[k][j]

	return solusi


def getRowMain(mat, i):
	#print("i ", i)
	col = -1
	row = i+1
	
	nonZero = False
	found1Utama = False

	while (row > 0 and not(found1Utama)):
		row -= 1
		col = 0
		nonZero = False

		while (col < i and not(nonZero)):
			if(mat[row,col] != 0):
				nonZero = True
			else:
				col += 1
		#print("IN while", col)

		if (not(nonZero) and (mat[row,col] == 1)):
			found1Utama = True

	if ((row == 0) and not (found1Utama)):
		row = 999
	
	return row

def makeMatEigen(mat, matEigen):
	transpose_solusi = np.transpose(mat)
	for i in range(1, len(mat[0])):
		if(transpose_solusi[i][len(transpose_solusi[i]) - 1] == 1):
			newVector = transpose_solusi[i][0:(len(transpose_solusi[i]) - 1)]
			matEigen.append(newVector)

	return matEigen


def row_echelon(A):
    """ Return Row Echelon Form of matrix A """

    # if matrix A has no columns or rows,
    # it is already in REF, so we return itself
    r, c = A.shape
    if r == 0 or c == 0:
        return A

    # we search for non-zero element in the first column
    for i in range(len(A)):
        if A[i,0] != 0:
            break
    else:
        # if all elements in the first column is zero,
        # we perform REF on matrix from second column
        B = row_echelon(A[:,1:])
        # and then add the first zero-column back
        return np.hstack([A[:,:1], B])

    # if non-zero element happens not in the first row,
    # we switch rows
    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row

    # we divide first row by first element in it
    A[0] = A[0] / A[0,0]
    # we subtract all subsequent rows with first row (it has 1 now as first element)
    # multiplied by the corresponding element in the first column
    A[1:] -= A[0] * A[1:,0:1]

    # we perform REF on matrix from second row, from second column
    B = row_echelon(A[1:,1:])

    # we add first row and first (zero) column, and return
    return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ])


def gaussJordan(mat):
	for p in range(len(mat)-1):
		for r in range (p+1 , len(mat) , 1):
			ratio = mat[p][r]
		for s in range(len(mat[0])):
			mat[p][s] -= ratio * mat[r][s]
		print(mat)
	return mat


mat = [[1, 2, 3],
	   [4, 5, 6],
	   [7, 8, 9],
	   [10, 11, 12]]


aftertran = np.transpose(mat)
mulMat1 = np.matmul(mat, aftertran) #AAT
mulMat2 = np.matmul(aftertran, mat) #ATA

root1, sigma1 = findroots(mulMat1)
root2, sigma2 = findroots(mulMat2)

matEigen = []
for root in root1:
	print(root)
	final1 = findFinalMat(root, mulMat1)
	
	upperT = np.transpose(final1)

	added = [0.0 for i in range(len(upperT[0]))]
		# Error di append
	appended = np.append(upperT, [added], axis=0)

	newUpper = np.transpose(appended)
	
	decmat,pivot = sy.Matrix(newUpper).rref()
	sol = getValue(decmat)
	
	
	# if(root == 1.6658075612787901):
	# 	print(final1)
	# 	print(newUpper)
	# 	print(reducedrow)
	# 	print(sol)
	
	matEigen = makeMatEigen(sol, matEigen)

print(matEigen)
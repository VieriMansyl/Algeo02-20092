import cv2 as cv
import numpy as np
import time	
from scipy import linalg
from sympy import symbols, Matrix, Symbol, Poly


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

	bt = np.transpose(b) #Transpose b, g, r
	gt = np.transpose(g)
	rt = np.transpose(r)

	#Untuk AAT
	broot1, bsigma1 = findroots(np.matmul(b, bt)) 
	groot1, gsigma1 = findroots(np.matmul(g, gt))
	rroot1, rsigma1 = findroots(np.matmul(r, rt))

	#Untuk ATA
	broot2, bsigma2 = findroots(np.matmul(bt, b)) 
	groot2, gsigma2 = findroots(np.matmul(gt, g))
	rroot2, rsigma2 = findroots(np.matmul(rt, r))

	end = time.time()
	delta = start - end

def findroots(matT):
	
	vars = Symbol('x') #Variabel yang dipakai

	all = []
	for i in range(len(matT)):
		each = []
		for j in range(len(matT[0])):
			if(i == j):
				each.append(vars - matT[i][j]) #ngisi kalau diagonal
			else:
				each.append(-matT[i][j]) #ngisi selain diagonal
		
		npeach = np.array(each) #Convert ke np array
		all.append(npeach)
	
	matAll = Matrix(all)
	deter = matAll.det()

	return convDetKoef(deter)

def convDetKoef(determinant):
	koef = Poly(determinant).all_coeffs() #Create koeficient lienar equation

	froot = np.roots(koef) #Cari akar-akar persamaan

	#Sort descending
	froot.sort()

	froot = froot[::-1]
	return convKoefRoot(froot)

#Convert Koeficient to Root and Sigma
def convKoefRoot(rawroot): 
	newroot = []
	newsigma = []

	for root in rawroot:
		if(root >= 0):
			newroot.append(root)
			newsigma.append(root ** 0.5)
	
	sigma = np.array(newsigma)
	finalroot = np.array(newroot)
	
	return newroot, newsigma





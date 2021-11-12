import numpy as np
import cv2 as cv


import eigen
import svd


def compress(image, cr):
	src = cv.imread(image, cv.IMREAD_ANYCOLOR)

	b, g, r = cv.split(src)	 # b, g, r masing-masing channel

	blist = b.tolist()
	glist = g.tolist()
	rlist = r.tolist()

	bfinal = solve(blist, cr)*(1/255)
	gfinal = solve(glist, cr)*(1/255)
	rfinal = solve(rlist, cr)*(1/255)

	finalsrc = np.dstack([bfinal, gfinal, rfinal])

	cv.imshow("", finalsrc)
	key = cv.waitKey(0)

	if(key == ord('c')):
		cv.destroyAllWindows()

def findK(cr, singVal):
	k = (cr/100) * singVal
	#Tentuin sistem Rounding
	return round(k)

def solve(mat , cr):
	matT = np.transpose(mat)

	#Basis buat mbuat V
	matATA = np.matmul(matT, mat)

	raweig2, raweigv2 = eigen.findEigen(matATA)

	eig2, sig2, matV = eigen.convEigSig(raweig2, raweigv2)
	print("Sigma")
	print(sig2)
	k = findK(cr, len(sig2))
	sigmaMat = svd.createSigmaMat(sig2, k, k) #Matriks Sigma, berbentuk list biasa
	print("Mat")
	finalV = matV[:k]
	current = np.matmul(sigmaMat, finalV)

	matU = np.matmul(mat, np.linalg.pinv(current))
	print("U")
	matUT = np.transpose(matU)
	finalU = matUT[:k]
	
	return multiplyMat(np.transpose(finalU), sigmaMat, finalV)
	 #AB = T
	#B = TA-1

def multiplyMat(mu, sig, mv):
	mul1 = np.matmul(mu, sig)
	mul2 = np.matmul(mul1, mv)
	return mul2


compress("static/20x12.jpg", 10)
# compress("static/10x10.jpg")
# compress("static/20x12.jpg")
# compress("static/smol_pro_max.jpg" , 100)
# compress("static/smol_pro_max.jpg" , 50)
# compress("ultra-smol.jpg" , 100)
# compress("ultra-smol.jpg" , 50)


# arr = [[3,2,2],
# 	   [2,3,-2]]

# mu, sig, mv= solve(arr)


# print("ini mu :")
# for line in mu:
# 	print(line)
# print("\nini sig :")
# for line in sig:
# 	print(line)
# print("\nini mv :")
# for line in mv:
# 	print(line)

# print(multiplyMat(mu, sig, mv))
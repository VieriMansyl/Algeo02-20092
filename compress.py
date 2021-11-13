import cv2 as cv
import numpy as np
import time


import eigen

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
	extension = image.split('.')[-1]

	start = time.time()			# End

	# return("static/hasil.png")
	src = cv.imread(image, cv.IMREAD_UNCHANGED)

	b, g, r, a = cv.split(src)	 # b, g, r masing-masing channel

	#Ubah tiap channel ke list, pemrosesan yang dilakukan berbasis untuk list
	blist = b.tolist()
	glist = g.tolist()
	rlist = r.tolist()
	alist = a.tolist()

	nrow = len(blist)
	ncol = len(blist[0])
	#Oke jadi ini agak weird, tapi kalau mau disave, gak boleh dibagi 1/255
	#Tapi kalau buat show, harus dibagi sama 255, jadi sementara, aku buat 2 jenis 
	#Satu buat show, satu buat save


	bfinal, k = process(blist, compression_rate, max(nrow,ncol))
	gfinal, k = process(glist, compression_rate, max(nrow, ncol))
	rfinal, k = process(rlist, compression_rate, max(nrow, ncol))


	finalsrc = np.dstack([bfinal, gfinal, rfinal, alist])
	
	btoshow = bfinal / 255
	gtoshow = gfinal / 255
	rtoshow = rfinal/255
	srctoshow = np.dstack([btoshow, gtoshow, rtoshow])

	

	cv.imshow("", srctoshow)
	key = cv.waitKey(0)

	if(key == ord('c')):
		cv.destroyAllWindows()

	pathwrite = "static/result." + extension

	cv.imwrite(pathwrite, finalsrc)

	#Calculating time
	end = time.time()
	delta = end - start
	
	pixeldiff = pixdiff(nrow, ncol, k)
	return delta, pixeldiff

def pixdiff(nrow, ncol, k):
	calc = (nrow * k) + k + (ncol *k)
	return (calc/(nrow*ncol)) * 100

def findK(cr, singVal):
	k = ((100 - cr + 1)/100) * singVal

	#Tentuin sistem Rounding
	return round(k)

#cr -> compression reate
#Asumsi mat -> m * n
def process(mat , cr, maxiter):
	matT = np.transpose(mat)

	#Basis buat mbuat V
	matATA = np.matmul(matT, mat)

	#Pencarian dan pemrosesan nilai eigen
	raweig2, raweigv2 = eigen.findEigen(matATA, maxiter)

	eig2, sig2, matV = eigen.convEigSig(raweig2, raweigv2)

	#Penentuan k
	k = findK(cr, len(sig2))
	
	#Matriks Sigma
	sigmaMat = eigen.createSigmaMat(sig2, k, k) 
	
	#Matriks V
	finalV = matV[:k]
	
	#Membuat matriks u dengan memanfaatkan sifat A = USigmaVT
	current = np.matmul(sigmaMat, finalV)
	matU = np.matmul(mat, np.linalg.pinv(current))
	
	matUT = np.transpose(matU)
	finalU = matUT[:k]
	
	return multiplyMat(np.transpose(finalU), sigmaMat, finalV), k


def multiplyMat(mu, sig, mv):
	mul1 = np.matmul(mu, sig)
	mul2 = np.matmul(mul1, mv)
	return mul2

delta, pix = compress("static/ball.png", 100)
print(pix)
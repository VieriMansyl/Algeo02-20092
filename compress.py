import cv2 as cv
import numpy as np
from sympy import symbols, Matrix, Symbol, Poly


# image = directory foto => "Folder_ini/static/ini_foto.png"
# compression_rate = xx%

# Fungsi compress ini nantinya mengkompress foto
# lalu hasilnya disimpan dalam folder static
# dan me-return directory dari foto tersebut
def compress(image, compression_rate):
	print("Start")				# Start
	print(compression_rate)		# 70
	print(image)				# static\lenna.png
	print("End")				# End

	# return("static/hasil.png")
	src = cv.imread(image, cv.IMREAD_ANYCOLOR)

	b, g, r = np.split(src)	


def find_root(a):
	return a
import cv2 as cv
import numpy as np
from sympy import symbols, Matrix, Symbol, Poly

src = cv.imread("static/lenna.png", cv.IMREAD_ANYCOLOR)

B, G, R = cv.split(src)

a = src[0][0]
b = src[132][173]
c = b[0]
d = b[1]
e = b[2]

newlist = np.array([1, 2, 3])
print(a) 
print(b)
print(b[2])
print(a - b)
print(newlist)

cv.imshow("", src)

key = cv.waitKey(0)

#Create file based on extension
if(key == ord('s')):
    cv.imwrite("static/New_file.jpeg", src)
elif(key == ord('x')):
    cv.destroyAllWindows()


# photo = cv.imread("rgb.png", cv.IMREAD_ANYCOLOR)

# b, g, r = cv.split(photo)
# newphoto = np.dstack([b, g, r])

# cv.imshow("normal", photo)

# cv.imshow("r", r)

# cv.imshow("g", g)


# cv.imshow("b", b)

# cv.imshow("new", newphoto)

# x = cv.waitKey(0)
# if(x == ord('c')):
#     cv.destroyAllWindows()
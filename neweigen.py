
import copy
import numpy as np
import math

from numpy.linalg.linalg import eig

# arr =  [[10,0,2],
#         [0,10,4],
#         [2,4,2]]
        
arr2 = [[11,1] , [1,11]]

a = np.array(arr2)
a1 = np.array([])

b = np.array([[0, 2,1], 
            [2, 3,2],
            [1, 3, 4 ]])

p = [1, 5, 10, 20]

while True:
    q, r = np.linalg.qr(a)
    a1 = np.dot(r, q)

    similar = True
    for j in range(len(arr2)):
        if(not math.isclose(a[j][j], a1[j][j], rel_tol=1e-12)):
            similar = False
            break
    
    if(similar):
        break
    else:
        a = copy.deepcopy(a1)

print(a)
eigval = np.diag(a)
print(eigval)
    
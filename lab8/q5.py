# Generate 4x4 matrix with random numbers only from (2,5,9,10) and then multiply this
# matrix with identity matrix. Finally add this matrix to any 4x4 matrix having only odd
# numbers.

import numpy as np
from numpy import random
print("RANDOM 4X4 MATRIX: ")
mat = random.choice([2,5,9,10],size = (4,4))
print(mat)
print("4X4 IDENTITY MATRIX: ")
identity = np.eye(4)
print(identity)
print("MULTIPLICATION OF MAT WITH IDENTITY: ")
matXid = np.multiply(mat,identity)
print(matXid)
print('4X4 ODD MATRIX: ')
odd_mat = np.arange(1,32,2).reshape(4,4)
print(odd_mat)
print("ADDITION OF ODD MATRIX WITH IDENTITYXMAT: ")
odd_add_matxid = np.add(matXid,odd_mat)
print(odd_add_matxid)

# 3. Create 3x3 matrix containing only even numbers. Multiply each element of this array with
# 4 and then multiply resultant matrix with 3x3 identity matrix (identity matrix should not be
# hardcoded).

import numpy as np

arr = np.arange(0,18,2)
arr = arr.reshape(3,3)
print(arr)

print("MULTIPLYING THE EVEN MATRIX BY 4: ")
resultant = np.multiply(arr,4)
print(resultant)

print("MULTIPLYING RESULTANT WITH IDENTITY")
id = np.eye(3)
resXid = np.multiply(resultant,id)
print(resXid)


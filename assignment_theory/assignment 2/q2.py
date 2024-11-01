# Generate a 3x3 matrix with random integers. Calculate the transpose of the matrix.
 
import numpy as np

arr = np.random.randint(1,11,size=(3,3))
print(f"Original Matrix: \n{arr}")

ta = arr.T
print(f"Transpose: \n{ta}")

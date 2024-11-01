# Generate a 2x2 matrix and calculate its determinant and inverse.

import numpy as np
arr = np.arange(5,9).reshape(2,2)
determinant = np.linalg.det(arr)
print(f"Determinant: {determinant}")
inverse = np.linalg.inv(arr)
print(f"Inverse: \n{inverse}")

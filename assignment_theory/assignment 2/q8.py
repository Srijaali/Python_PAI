# Create a 3x3 matrix representing a system of linear equations. Use NumPy to solve the system
# and print the solution.

import numpy as np
arr1 =  np.array([[2, 3, 1],
                   [4, 1, 2],
                   [3, 5, 3]])
print(arr1)

arr2 = np.array([1,2,3])
eq = np.linalg.solve(arr1,arr2)
print(f"Solution: {eq}")

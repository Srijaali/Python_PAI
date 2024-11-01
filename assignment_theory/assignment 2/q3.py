# Create a NumPy array with 20 values and reshape it into a 4x5 matrix.

import numpy as np
arr = np.arange(0,20)
print(f"Array without reshaping: \n{arr}")
arr = arr.reshape(4,5)
print(f"Array after 4x5: \n{arr}")

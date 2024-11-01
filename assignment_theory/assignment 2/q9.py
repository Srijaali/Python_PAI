# Create a NumPy array with 25 values and calculate the 75th percentile.

import numpy as np
arr = np.random.randint(1,25,size=25)
print("array: " ,arr)

perc = np.percentile(arr,75)
print(f"75th Percentile: {perc}")

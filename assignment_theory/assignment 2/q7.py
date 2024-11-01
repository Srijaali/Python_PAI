# Create a NumPy array with 50 random values. Find the indices of the maximum and minimum
# values in the array.

import numpy as np
arr1 = np.random.randint(1,10,size=50)
print(f"original: \n{arr1}")
max_index = np.argmax(arr1)
print(f"Index of maximum value:, {max_index}\n Max val: {arr1[max_index]} ")

min_index = np.argmin(arr1)
print(f"Index of minimum value:, {min_index}\n Min val: {arr1[min_index]}" )

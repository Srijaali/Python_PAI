# Create a multi-dimensional array of 3 rows and 3 columns having odd numbers from 1 to
# 19 including 1 and excluding 19. After that, iterate over this array to print all elements.

import numpy as np
arr = np.arange(1,19,2)
arr = arr.reshape(3,3)
print(arr)
print("Printing after iterating every element in the matrix: ")
for i in arr:
  for j in i:
    print(j)

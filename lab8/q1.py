# Write a program to create numpy array or vector of all the even integers from 20 to 50
# exluding 20 and 50.

import numpy as np
a = np.arange(22,50,2)
print(a)
#this works as well
arr = a[a!=20]
print(arr)

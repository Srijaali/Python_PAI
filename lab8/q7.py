# Write a NumPy program to create a random array with 1000 elements and compute the
# average, variance, standard deviation of the array elements. Save all the results in text file
# created at runtime.

import numpy as np
from numpy import random

arr = random.randint(1,1000,size=1000)
print(arr)
avg = arr.mean()
variance = arr.var()
standard_dev = arr.std()
print(f"Average: ,{avg}")
print(f"\n Variance: , {variance}")
print(f'\n Standard Deviation:  ,{standard_dev}')
with open ('new_file.txt' , 'w') as f:
  f.write(f"Average: ,{avg}")
  f.write(f"\n Variance: , {variance}")
  f.write(f'\n Standard Deviation:  ,{standard_dev}')

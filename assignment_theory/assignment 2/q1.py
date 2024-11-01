# Create a one-dimensional NumPy array containing integers from 1 to 10. Compute the sum,
# mean, and product of the array.

import pandas as pd
import numpy as np

arr = np.arange(1,11)
print(arr)

a = arr.sum()
print(f"Sum: {a}")
b=arr.mean()
print(f"Mean: {b}")
c = arr.prod()
print(f"Prod: {c}")

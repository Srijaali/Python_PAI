# Perform element-wise addition, subtraction, multiplication, and division on two NumPy arrays
# of your choice.

import numpy as np
arr1 = np.arange(1,5)
arr2 = np.arange(5,9)

add = arr1+arr2
print(f"ADDITION: \n{add}")
sub = arr2 - arr1
print(f"SUBTRACTION: \n{sub}")
multiply = arr1*arr2
print(f"MULTIPLICATION: \n{multiply}")
division = arr1/arr2
print(f"DIVISION: \n{division}")

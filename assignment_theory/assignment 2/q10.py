# Implement a function that accepts a NumPy array and normalizes it (subtracts the mean and
# divides by the standard deviation). Apply this function to a sample array.

import numpy as np

def normalise_ARRAY(arr):
    mean = np.mean(arr)         
    std_dev = np.std(arr)        
    normalized_arr = (arr - mean) / std_dev  
    return normalized_arr

arr = np.array([10, 20, 30, 40, 50])
print("Original array:", arr)

# Apply the normalization function
normalized_array = normalise_ARRAY(arr)
print("Normalized array:", normalized_array)

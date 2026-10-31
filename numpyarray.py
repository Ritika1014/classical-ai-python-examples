
import numpy as np
 
# 1D array
a = np.array([1, 2, 3, 4, 5])
print("1D array:", a)
 
# 2D array (matrix)
b = np.array([[1, 2], [3, 4]])
print("2D array:\n", b)
 
# Array of zeros, ones, or range
zeros = np.zeros((2,3))
ones = np.ones((3,2))
range_arr = np.arange(0, 10, 2)  # 0,2,4,6,8
print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Range:", range_arr)

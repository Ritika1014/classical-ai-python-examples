import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])
 
# Matrix multiplication
print("Matrix Product:\n", np.dot(A, B))
 
# Determinant
print("Determinant:", np.linalg.det(A))
 
# Inverse
print("Inverse of A:\n", np.linalg.inv(A))

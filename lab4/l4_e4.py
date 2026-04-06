# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 19:05:21 2026

@author: Antonio
"""

import numpy as np

# 1. Build Matrix A
# We treat each sensor's readings as a column in matrix A
sensor1 = np.array([1, 2])
sensor2 = np.array([2, 4])
A = np.column_stack((sensor1, sensor2))

# 2. Check independence of columns
# We can check this using the Rank of the matrix or the Determinant
rank = np.linalg.matrix_rank(A)
det = np.linalg.det(A)

print("Matrix A:")
print(A)
print(f"\nRank of Matrix A: {rank}")
print(f"Determinant of A: {det:.2f}")

# 3. Logic to check independence
if rank < A.shape[1]:
    print("\nResult: The columns are LINEARLY DEPENDENT.")
else:
    print("\nResult: The columns are LINEARLY INDEPENDENT.")
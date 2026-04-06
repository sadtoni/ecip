# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:14:16 2026

@author: Antonio
"""

import numpy as np

# 1. Define the Data
# (time, humidity) pairs
data = np.array([(1, 40), (2, 42), (3, 45)])
time = data[:, 0]
humidity = data[:, 1]

# 2. Build Matrix A and Vector y
# Matrix A has a column of time values and a column of ones (for the intercept b)
A = np.vstack([time, np.ones(len(time))]).T
y = humidity

# 3. Compute a and b using Least Squares
# np.linalg.lstsq returns several values; the first is the solution vector [a, b]
coeffs, residuals, rank, s = np.linalg.lstsq(A, y, rcond=None)
a, b = coeffs

print("Matrix A:\n", A)
print("\nVector y:", y)
print(f"\nResults:\nSlope (a): {a:.2f}\nIntercept (b): {b:.2f}")
print(f"Linear Model: y = {a:.2f}x + {b:.2f}")
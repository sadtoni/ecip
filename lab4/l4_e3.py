# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:42:31 2026

@author: Antonio
"""

import numpy as np

# 1. Setup Data and Results from Lab 2
time = np.array([1, 2, 3])
y = np.array([40, 42, 45])
A = np.vstack([time, np.ones(len(time))]).T

# Results from Lab 2: a = 2.5, b = 37.33
coeffs = np.array([2.5, 37.33333333]) 

# 2. Compute predicted values (Ax)
y_pred = A @ coeffs

# 3. Compute residual (r = y - Ax)
residuals = y - y_pred

# 4. Compute squared error
# This is the sum of the squares of the residuals
squared_error = np.sum(residuals**2)

print(f"Actual Values (y):    {y}")
print(f"Predicted Values (Ax): {y_pred}")
print(f"Residuals (r):        {residuals}")
print(f"Sum of Squared Error: {squared_error:.4f}")
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 19:16:57 2026

@author: Antonio
"""

import numpy as np

# 1. Given error (residuals) from the sensor data
errors = np.array([-1, 2, -2])

# 2. Compute Squared Error (L2 Norm approach)
# Squaring ensures all values are positive and penalizes larger errors more heavily
squared_errors = errors**2
sum_squared_error = np.sum(squared_errors)

# 3. Compute Absolute Error (L1 Norm approach)
# Absolute value treats all errors linearly regardless of magnitude
absolute_errors = np.abs(errors)
sum_absolute_error = np.sum(absolute_errors)

print(f"Original Errors:  {errors}")
print(f"Squared Errors:   {squared_errors} -> Total: {sum_squared_error}")
print(f"Absolute Errors:  {absolute_errors} -> Total: {sum_absolute_error}")
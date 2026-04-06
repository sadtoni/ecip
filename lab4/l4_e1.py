# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:05:05 2026

@author: Antonio
"""

import numpy as np

# 1. Define the sensor readings (y)
y = np.array([21, 22, 23, 24])

# 2. Compute x (the constant that best fits the data)
# For a constant model, the Least Squares solution is the mean.
x = np.mean(y)

# 3. Interpret and Print Results
print(f"Sensor Readings: {y}")
print(f"Calibrated Temperature (x): {x}")
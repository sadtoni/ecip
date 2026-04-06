# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 19:15:34 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Sample Data: Time (hours) vs Energy (kWh)
# Let's assume energy increases over time
time = np.array([1, 2, 3, 4, 5, 6])
energy = np.array([1.2, 2.5, 3.7, 5.1, 6.2, 7.8])

# 2. Fit Linear Model (y = ax + b)
# We build matrix A and solve for coefficients using Least Squares
A = np.vstack([time, np.ones(len(time))]).T
coeffs, _, _, _ = np.linalg.lstsq(A, energy, rcond=None)
slope, intercept = coeffs

# 3. Interpret Results
print(f"Consumption Rate (Slope): {slope:.4f} kWh per hour")
print(f"Base Energy (Intercept): {intercept:.4f} kWh")

# 4. Plot Data and Fitted Line
plt.figure(figsize=(10, 6))

# Plot the raw data points
plt.scatter(time, energy, color='red', label='Measured Data')

# Plot the fitted line (y = Ax)
y_pred = A @ coeffs
plt.plot(time, y_pred, color='blue', label=f'Fitted Model: y = {slope:.2f}x + {intercept:.2f}')

# Formatting the plot
plt.title('Smart Home Energy Model')
plt.xlabel('Time (Hours)')
plt.ylabel('Energy Consumption (kWh)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
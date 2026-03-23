# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:39:40 2026

@author: Antonio
"""

import numpy as np

x_true = 10
x_hat = np.mean(y_measurements)
error = x_hat - x_true

print(f"True Value (x): {x_true}")
print(f"Estimate (x_hat): {x_hat:.4f}")
print(f"Estimation Error: {error:.4f}")
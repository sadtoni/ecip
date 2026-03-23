# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:44:55 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate correlated random variables
mean = [0, 0]
cov_matrix = [[1, 0.8], [0.8, 1]]  # Target covariance = 0.8
data = np.random.multivariate_normal(mean, cov_matrix, 1000)
x, y = data.T

# Compute sample covariance
sample_cov = np.cov(x, y)[0, 1]

# Plot results
plt.scatter(x, y, alpha=0.5, s=10)
plt.title(f'Sample Covariance: {sample_cov:.4f}')
plt.savefig('correlated_variables.png')
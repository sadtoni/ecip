# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:26:36 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate three sets of Gaussian noise with different variances
mean = 0
vars = [0.2, 1.0, 5.0]
colors = ['blue', 'green', 'red']

for v, color in zip(vars, colors):
    data = np.random.normal(mean, np.sqrt(v), 2000)
    plt.hist(data, bins=50, alpha=0.4, label=f'$\sigma^2={v}$', density=True, color=color)

plt.legend()
plt.title('Gaussian Noise Comparison')
plt.savefig('gaussian_variances.png')
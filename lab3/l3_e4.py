# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:19:59 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

# Comparison of two datasets with different variances
data_low_var = np.random.normal(0, 1, 1000)
data_high_var = np.random.normal(0, 2, 1000) # sigma=2, var=4

plt.hist(data_low_var, bins=30, alpha=0.5, label='$\sigma^2 = 1$', density=True)
plt.hist(data_high_var, bins=30, alpha=0.5, label='$\sigma^2 = 4$', density=True)
plt.legend()
plt.savefig('variance_comparison.png')
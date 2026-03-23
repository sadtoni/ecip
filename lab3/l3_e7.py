# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:35:20 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

x_true = 10
noise = np.random.normal(0, 1, 1000)
y_measurements = x_true + noise

plt.hist(y_measurements, bins=30, edgecolor='black', alpha=0.7)
plt.axvline(x_true, color='red', linestyle='dashed', label='True Value ($x=10$)')
plt.legend()
plt.savefig('measurement_distribution.png')
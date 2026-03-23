# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:24:59 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

gaussian_data = np.random.normal(0, 1, 1000)
uniform_data = np.random.uniform(-2, 2, 1000)

plt.hist(gaussian_data, bins=30, alpha=0.5, label='Gaussian ($\mu=0, \sigma=1$)', density=True)
plt.hist(uniform_data, bins=30, alpha=0.5, label='Uniform ([-2, 2])', density=True)
plt.legend()
plt.savefig('gaussian_vs_uniform.png')
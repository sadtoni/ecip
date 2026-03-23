# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:36:37 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.savefig('histogram.png')
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:34:20 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

x = 0.5
u = 0.1
n_steps = 20
states = []

for t in range(n_steps):
    states.append(x)
    x = x + 0.1 * (x**2) + u

plt.plot(states, marker='o')
plt.title('Nonlinear System Simulation')
plt.show()
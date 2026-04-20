# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:33:55 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

A, B, C = 1, 1, 1
u = 1
x = 0
x_hat = 0
n_steps = 30

innovations = []

for t in range(n_steps):
    x_hat_pred = A * x_hat + B * u
    
    w = np.random.normal(0, 0.5)
    v = np.random.normal(0, 0.5)
    
    y = C * x + v
    
    innovation = y - C * x_hat_pred
    innovations.append(innovation)
    
    x = A * x + B * u + w
    x_hat = x_hat_pred

plt.plot(range(n_steps), innovations, color='red', label='Innovation')
plt.axhline(0, color='black', lw=1, ls='--')
plt.title('Exercise 3: Innovation over Time')
plt.xlabel('Time Step')
plt.ylabel('Error Value')
plt.legend()
plt.show()
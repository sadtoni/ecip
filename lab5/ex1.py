# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:57:57 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

A, B, C = 1, 1, 1
u = 1
x = 0
n_steps = 30

true_states = []
measured_outputs = []

for t in range(n_steps):
    w = np.random.normal(0, 0.5)
    v = np.random.normal(0, 0.5)
    
    y = C * x + v
    measured_outputs.append(y)
    true_states.append(x)
    
    x = A * x + B * u + w

plt.plot(range(n_steps), true_states, label='True State x(t)', marker='o')
plt.plot(range(n_steps), measured_outputs, label='Measured Output y(t)', linestyle='--')
plt.xlabel('Time Step')
plt.ylabel('Value')
plt.legend()
plt.show()
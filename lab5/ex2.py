# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:16:46 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

A, B, C = 1, 1, 1
u = 1
x = 0
x_hat = 0
n_steps = 30

true_states = []
predicted_states = []

for t in range(n_steps):
    x_hat_pred = A * x_hat + B * u
    predicted_states.append(x_hat_pred)
    
    true_states.append(x)
    
    w = np.random.normal(0, 0.5)
    x = A * x + B * u + w
    x_hat = x_hat_pred

plt.plot(range(n_steps), true_states, label='True State $x(t)$')
plt.plot(range(n_steps), predicted_states, label='Predicted State $\hat{x}$', linestyle='--')
plt.title('Exercise 2: State Prediction')
plt.xlabel('Time Step')
plt.ylabel('Value')
plt.legend()
plt.show()
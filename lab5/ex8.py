# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:19:53 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

A, B, C = 1, 1, 1
u = 1
Q = 0.01
R = 0.5
n_steps = 30

x = 0
x_hat = 0
P = 1

predicted_covs = []
updated_covs = []

for t in range(n_steps):
    w = np.random.normal(0, np.sqrt(Q))
    v = np.random.normal(0, np.sqrt(R))
    
    P_minus = A * P * A + Q
    predicted_covs.append(P_minus)
    
    y = C * x + v
    K = P_minus * C / (C * P_minus * C + R)
    P = (1 - K * C) * P
    updated_covs.append(P)
    
    x_hat = (A * x_hat + B * u) + K * (y - C * (A * x_hat + B * u))
    x = A * x + B * u + w

plt.figure(figsize=(10, 5))
plt.plot(predicted_covs, label='Predicted Covariance $P(t|t-1)$', marker='x')
plt.plot(updated_covs, label='Updated Covariance $P(t|t)$', marker='o')
plt.title('Exercise 8: Covariance Analysis')
plt.xlabel('Time Step')
plt.ylabel('Uncertainty (Covariance)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
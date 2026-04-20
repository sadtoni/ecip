# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:57:39 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

def run_kalman_q(Q_val):
    A, B, C, R = 1, 1, 1, 0.5
    u, n_steps = 1, 30
    x, x_hat, P = 0, 0, 1
    
    true_states = []
    estimates = []
    
    for t in range(n_steps):
        w = np.random.normal(0, np.sqrt(Q_val))
        v = np.random.normal(0, np.sqrt(R))
        
        x_hat_minus = A * x_hat + B * u
        P_minus = A * P * A + Q_val
        
        y = C * x + v
        K = P_minus * C / (C * P_minus * C + R)
        x_hat = x_hat_minus + K * (y - C * x_hat_minus)
        P = (1 - K * C) * P
        
        true_states.append(x)
        estimates.append(x_hat)
        x = A * x + B * u + w
        
    return true_states, estimates

qs = [0.0001, 0.01, 1]
plt.figure(figsize=(10, 6))

for q in qs:
    true, est = run_kalman_q(q)
    plt.plot(est, label=f'Estimate (Q={q})')

plt.title('Effect of Process Noise Covariance Q')
plt.xlabel('Time Step')
plt.ylabel('State Value')
plt.legend()
plt.show()
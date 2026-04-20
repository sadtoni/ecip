# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:09:16 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

def run_kalman_r(R_val):
    A, B, C, Q = 1, 1, 1, 0.01
    u, n_steps = 1, 30
    x, x_hat, P = 0, 0, 1
    
    true_states = []
    estimates = []
    
    for t in range(n_steps):
        w = np.random.normal(0, np.sqrt(Q))
        v = np.random.normal(0, np.sqrt(R_val))
        
        x_hat_minus = A * x_hat + B * u
        P_minus = A * P * A + Q
        
        y = C * x + v
        K = P_minus * C / (C * P_minus * C + R_val)
        x_hat = x_hat_minus + K * (y - C * x_hat_minus)
        P = (1 - K * C) * P
        
        true_states.append(x)
        estimates.append(x_hat)
        x = A * x + B * u + w
        
    return true_states, estimates

rs = [0.01, 0.5, 5]
plt.figure(figsize=(10, 6))

for r in rs:
    true, est = run_kalman_r(r)
    plt.plot(est, label=f'Estimate (R={r})')

plt.title('Effect of Measurement Noise Covariance R')
plt.xlabel('Time Step')
plt.ylabel('State Value')
plt.legend()
plt.show()
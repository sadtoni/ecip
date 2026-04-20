# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:46:59 2026

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
x_hat_pred_only = 0
x_hat_kalman = 0
P = 1

true_states = []
pred_only_estimates = []
kalman_estimates = []

for t in range(n_steps):
    w = np.random.normal(0, np.sqrt(Q))
    v = np.random.normal(0, np.sqrt(R))
    
    true_states.append(x)
    
    x_hat_pred_only = A * x_hat_pred_only + B * u
    pred_only_estimates.append(x_hat_pred_only)
    
    x_hat_minus = A * x_hat_kalman + B * u
    P_minus = A * P * A + Q
    y = C * x + v
    K = P_minus * C / (C * P_minus * C + R)
    x_hat_kalman = x_hat_minus + K * (y - C * x_hat_minus)
    P = (1 - K * C) * P
    kalman_estimates.append(x_hat_kalman)
    
    x = A * x + B * u + w

mse_pred = np.mean((np.array(true_states) - np.array(pred_only_estimates))**2)
mse_kalman = np.mean((np.array(true_states) - np.array(kalman_estimates))**2)

print(f"MSE Prediction Only: {mse_pred:.4f}")
print(f"MSE Full Kalman Filter: {mse_kalman:.4f}")

plt.figure(figsize=(10, 6))
plt.plot(true_states, label='True State', color='black', lw=2)
plt.plot(pred_only_estimates, label='Prediction Only', linestyle=':')
plt.plot(kalman_estimates, label='Kalman Filter', linestyle='--')
plt.title('Comparison: Prediction Only vs. Kalman Filter')
plt.legend()
plt.show()
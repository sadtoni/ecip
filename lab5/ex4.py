# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:42:24 2026

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

true_states = []
noisy_measurements = []
kalman_estimates = []
kalman_gains = []
covariances = []

for t in range(n_steps):
    w = np.random.normal(0, np.sqrt(Q))
    v = np.random.normal(0, np.sqrt(R))
    
    x_hat_minus = A * x_hat + B * u
    P_minus = A * P * A + Q
    
    y = C * x + v
    
    K = P_minus * C / (C * P_minus * C + R)
    x_hat = x_hat_minus + K * (y - C * x_hat_minus)
    P = (1 - K * C) * P
    
    true_states.append(x)
    noisy_measurements.append(y)
    kalman_estimates.append(x_hat)
    kalman_gains.append(K)
    covariances.append(P)
    
    x = A * x + B * u + w

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(true_states, label='True State', color='black', lw=2)
plt.scatter(range(n_steps), noisy_measurements, label='Noisy Measurement', alpha=0.5, color='red', s=10)
plt.plot(kalman_estimates, label='Kalman Estimate', color='blue', linestyle='--')
plt.title('Exercise 4: Full Kalman Filter State Estimation')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(kalman_gains, label='Kalman Gain K(t)', color='green')
plt.title('Kalman Gain')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(covariances, label='Covariance P(t)', color='purple')
plt.title('State Covariance')
plt.legend()

plt.tight_layout()
plt.show()
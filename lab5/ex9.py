# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:28:27 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

dt = 1
A = np.array([[1, dt],
              [0, 1]])
B = np.zeros((2, 1))
C = np.array([[1, 0]])

Q = np.array([[0.01, 0],
              [0, 0.01]])
R = np.array([[0.5]])

x = np.array([[0], [1]])
x_hat = np.array([[0], [0]])
P = np.eye(2)

n_steps = 30
true_pos, true_vel = [], []
est_pos, est_vel = [], []

for t in range(n_steps):
    w = np.random.multivariate_normal([0, 0], Q).reshape(2, 1)
    v = np.random.normal(0, np.sqrt(R[0,0]))
    
    true_pos.append(x[0,0])
    true_vel.append(x[1,0])
    
    x_hat_minus = A @ x_hat
    P_minus = A @ P @ A.T + Q
    
    y = C @ x + v
    
    S = C @ P_minus @ C.T + R
    K = P_minus @ C.T @ np.linalg.inv(S)
    x_hat = x_hat_minus + K @ (y - C @ x_hat_minus)
    P = (np.eye(2) - K @ C) @ P
    
    est_pos.append(x_hat[0,0])
    est_vel.append(x_hat[1,0])
    
    x = A @ x + w

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(true_pos, label='True Position', color='black')
ax1.plot(est_pos, label='Estimated Position', linestyle='--', color='blue')
ax1.set_title('Position Estimation')
ax1.legend()

ax2.plot(true_vel, label='True Velocity', color='black')
ax2.plot(est_vel, label='Estimated Velocity', linestyle='--', color='red')
ax2.set_title('Velocity Estimation (Hidden State)')
ax2.legend()

plt.tight_layout()
plt.show()
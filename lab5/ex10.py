# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:33:58 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

A, B, C = 1, 1, 1
L = 0.5
Q, R = 0.01, 0.5
n_steps = 50

x = 10 
x_hat = 0
P = 1

true_states = []
control_signals = []

for t in range(n_steps):
    u = -L * x_hat
    control_signals.append(u)
    true_states.append(x)
    
    w = np.random.normal(0, np.sqrt(Q))
    v = np.random.normal(0, np.sqrt(R))
    
    x_hat_minus = A * x_hat + B * u
    P_minus = A * P * A + Q
    
    y = C * x + v
    K = P_minus * C / (C * P_minus * C + R)
    x_hat = x_hat_minus + K * (y - C * x_hat_minus)
    P = (1 - K * C) * P
    
    x = A * x + B * u + w

plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(true_states, label='State x(t)', color='blue')
plt.title('State Feedback Control')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(control_signals, label='Control Signal u(t)', color='red')
plt.title('Control Signal')
plt.legend()
plt.tight_layout()
plt.show()
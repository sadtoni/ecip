# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:49:13 2026

@author: Antonio
"""

import numpy as np
import matplotlib.pyplot as plt

N = 10000
# Simulate events A and B
event_b = np.random.rand(N) < 0.3
event_a = np.zeros(N, dtype=bool)
event_a[event_b] = np.random.rand(np.sum(event_b)) < 0.7  # P(A|B) = 0.7
event_a[~event_b] = np.random.rand(np.sum(~event_b)) < 0.2

# Estimate P(A|B)
p_b_est = np.mean(event_b)
p_a_given_b_est = np.mean(event_a & event_b) / p_b_est

print(f"Sample P(A|B): {p_a_given_b_est:.4f}")

# Visualize probability components
plt.bar(['P(B)', 'P(A and B)', 'P(A|B)'], [p_b_est, np.mean(event_a & event_b), p_a_given_b_est])
plt.savefig('conditional_prob.png')
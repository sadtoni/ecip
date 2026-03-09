#4. consider the same vector as values for r factor, measured here, across 17 years. answer what will be the populatuon growth in 17th year?

import matplotlib.pyplot as plt

r = 4.0
initial_populations = [0.1, 0.5, 1, 2]
generations = 20

plt.figure(figsize=(10, 6))

for x0 in initial_populations:
    x = x0
    history = [x]
    for _ in range(generations):
        x = r * x * (1 - x)
        history.append(x)
    
    plt.plot(history, marker='o', label=f'Initial x={x0}')

plt.axhline(y=1.0, color='r', linestyle='--', label='Carrying Capacity')
plt.axhline(y=0.0, color='black', linestyle='-')
plt.title(f"Logistic Map Experiments (r = {r})")
plt.xlabel("Generation")
plt.ylabel("Population Ratio")
plt.legend()
plt.grid(True)
plt.show()
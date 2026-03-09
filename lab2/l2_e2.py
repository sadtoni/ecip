#2. use your simulation to point out at what value of r, the population growth becomes chaotic. show your result with a screenshot and plot the data

import matplotlib.pyplot as plt

r = 3.9  # Chaotic growth factor
x = 0.1  # Initial population
history = [x]

for _ in range(100):
    x = r * x * (1 - x)
    history.append(x)

plt.plot(history, marker='o', markersize=3)
plt.title(f"Chaotic Population Growth (r = {r})")
plt.xlabel("Generation")
plt.ylabel("Population Ratio")
plt.grid(True)
plt.savefig('chaotic_growth.png')
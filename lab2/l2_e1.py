#1. make a simualtion by using the logistic regression expression (population growth). use a growth factor r = 0.9. make a report (word/txt) that describes the fate of the population for r=0.9

import matplotlib.pyplot as plt

r = 0.9
x = 0.1
generations = 50
history = [x]

for _ in range(generations):
    x = r * x * (1 - x)
    history.append(x)

plt.plot(history)
plt.title(f"Logistic Growth (r = {r})")
plt.xlabel("Generation")
plt.ylabel("Population Ratio")
plt.grid(True)
plt.show()

print("Final 5 values:", history[-5:])
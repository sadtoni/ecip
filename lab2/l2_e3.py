#3. for each value of r, calculate the population size and plot the data:
#r=[2,2.5,1,1.2,3.1,0.5,4,4.4,3,2.9,2.8,1.9,1.5,1.4,7,3.8,8]

import matplotlib.pyplot as plt

r_values = [2, 2.5, 1, 1.2, 3.1, 0.5, 4, 4.4, 3, 2.9, 2.8, 1.9, 1.5, 1.4, 7, 3.8, 8]
x0 = 0.1

for r in r_values:
    x = x0
    h = [x]
    for _ in range(20):
        x = r * x * (1 - x)
        h.append(max(0, x))
    plt.plot(h, label=f'r={r}')
plt.title("Trajectories for each r")
plt.legend()
plt.show()

x = x0
h_v = [x]
for r in r_values:
    x = r * x * (1 - x)
    x = max(0, x)
    h_v.append(x)
plt.plot(h_v, marker='o')
plt.title("17 Year Population Growth")
plt.show()

print(f"Year 17 Population: {h_v[17]}")
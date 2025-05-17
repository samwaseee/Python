import numpy as np

x = np.random.uniform(0.0, 5.0, 250)
print("Random numbers:", x)

import matplotlib.pyplot as plt

x = np.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100, density=True, alpha=0.5, color='g', edgecolor='black')
plt.title('Histogram of Uniform Distribution')
plt.show() 

x = np.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100, density=True, alpha=0.5, color='g', edgecolor='black')
plt.title('Histogram of Normal Distribution')
plt.show()
import matplotlib.pyplot as plt, numpy as np

x = np.arange(-3, 3, .1)
y = x ** 3
plt.plot(x, y, color = 'skyblue')
plt.show()
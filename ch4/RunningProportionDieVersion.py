# Dependencies
import numpy as np
from matplotlib import pyplot as plt


# A function for computing the long-run relative frequency
def longrun_relative_frequency(trials: int) -> np.ndarray: 
    '''It returns the long-run relative frequency of coming up a six on a six-sided die'''
    # Pseudo-Random Generated Number
    # np.random.seed(47405) I'm suppressing the seed here
    prng = np.random.choice([i for i in range(1, 7)], trials)
    is_six = prng == 6
    
    # Computing relative frequency
    cumsum = np.cumsum(is_six)
    counts = np.arange(1, prng.size + 1)
    result = np.array([i / j for i, j in zip(cumsum, counts)])
    return result


# Plotting the results
_, axes = plt.subplots(2, 2, sharey = True)
t = 'Long-run relative frequency of having a 6 on a six-sided die — p(x = 6)'
p = round(1/6, 3)
for trials, ax in zip(np.geomspace(1e3, 1e6, 4), axes.flatten()):
    data = longrun_relative_frequency(int(trials))
    ax.plot(data, 'c', label = f'N = {data.size}', linewidth = .9)
    ax.axhline(p, color = 'k', linestyle = ':', label = f'P(x) = {p}', linewidth = .9)
    ax.legend()
plt.suptitle(t, fontsize = 10)
plt.show()
import numpy as np
from matplotlib import pyplot as plt

def longrun_relative_frequency(trials: int = 500) -> tuple[np.ndarray, str]: 
    np.random.seed(47405) # Be aware that it won't generate the same data due to Pythton and R PRNG differences
    prng = np.random.choice(['H', 'T'], trials)
    is_head = prng == 'H'    
    cumsum = np.cumsum(is_head)
    counts = np.arange(1, prng.size + 1)
    run_prop = np.array([i / j for i, j in zip(cumsum, counts)])
    display_string = ''.join(prng[:11]) + '...' + f'\nEnd Proportion = {round(run_prop[-1], 2)}'
    return run_prop, display_string


run_prop, display_string = longrun_relative_frequency()
plt.plot(run_prop,'-o', color = 'skyblue', label = display_string)
plt.axhline(.5, color = 'k', linestyle = ':')
plt.xlabel('Flip Numbers', labelpad = 1.5)
plt.ylabel('Proportion Heads', labelpad = 1.5)
plt.legend(frameon = False, handlelength = 0, markerscale = 0)
plt.title('Running Proportion of Heads')
plt.show()
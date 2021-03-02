import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# number of data points
n = 1000

# generate data - log-normal distribution
data = np.exp(np.random.randn(n)/2)

plt.plot(data, 's')
plt.show()

# number of bins
k = 40

plt.hist(data, k)
plt.show()
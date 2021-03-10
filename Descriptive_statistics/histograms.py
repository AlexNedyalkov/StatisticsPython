# import libraries
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# number of data points
n = 1000

# number of histogram bins
k = 40

# generate log-normal distribution
data = np.exp(np.random.randn(n)/2)


# one way to show a histogram
plt.hist(data, k)
plt.xlabel('Value')
plt.ylabel('Count')
plt.show()

# try the Freedman-Diaconis rule

r = 2*stats.iqr(data)*n**(-1/3)
b = np.ceil((max(data)-min(data))/r)
print(b)
plt.hist(data, int(b))


plt.hist(data, bins='fd')

plt.xlabel('Value')
plt.ylabel('Count')
plt.title(f'F-D "rule" using {b} bins')
plt.show()

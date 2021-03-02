import matplotlib.pyplot as plt
import numpy as np

# data sizes
# m - rows or number of observation
# n - columns or features
m = 30
n = 6

# generate data
data = np.zeros((m, n))

for i in range(n):
     data[:, i] = 30*np.random.randn(m) * (2*i/(n-1)-1)**2 + (i+1)**2

fig, ax = plt.subplots(1, 3, figsize=(8, 2))
ax[0].bar(range(n),np.mean(data,axis=0))
ax[0].set_title('Bar plot')

# just the error bars
ax[1].errorbar(range(n),np.mean(data,axis=0),np.std(data,axis=0,ddof=1),marker='s',linestyle='')
ax[1].set_title('Errorbar plot')

# both
ax[2].bar(range(n),np.mean(data,axis=0))
ax[2].errorbar(range(n),np.mean(data,axis=0),np.std(data,axis=0,ddof=1),marker='.',linestyle='',color='k')
ax[2].set_title('Error+bar plot')

plt.show()


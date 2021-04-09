import numpy as np
import matplotlib.pyplot as plt
from statsmodels import robust
import scipy.stats as stats

N = 40
data = np.random.randn(N)
data[data < - 1] = data[data < -1] + 2
data[data > 2] = data[data > 2]**2
print(f'The mean of the data is {data.mean():.2f} and the standard deviation is {data.std():.2f}')
data = data*50 + 200
print(f'The mean of the data is {data.mean():.2f} and the standard deviation is {data.std():.2f}')

data_Z_normalized = (data - data.mean()) / data.std()
print(f'The mean of the data is {data_Z_normalized.mean():.2f} and the standard deviation is {data_Z_normalized.std():.2f}')

zscorethresh = 3

# plot the data
fig, ax = plt.subplots(2, 1, figsize=(8, 6))

ax[0].plot(data, 'k^', markerfacecolor='w', markersize=12)
ax[0].set_xticks([])
ax[0].set_xlabel('Data index')
ax[0].set_ylabel('Orig. scale')

ax[1].plot(data_Z_normalized, 'k^', markerfacecolor='w', markersize=12)
ax[1].plot([0, N], [zscorethresh, zscorethresh], 'r--')
ax[1].set_xlabel('Data index')
ax[1].set_ylabel('Z distance')
# plt.show()

outliers = np.where(abs(data_Z_normalized)>zscorethresh)[0]
ax[0].plot(outliers, data[outliers], 'x', color='r', markersize=20)
ax[1].plot(outliers, data_Z_normalized[outliers], 'x', color='r', markersize=20)
plt.show()

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


# compute modified z
dataMed = np.median(data)
# MAD: mean absolute deivation
dataMAD = robust.mad(data)

dataMz = stats.norm.ppf(.75)*(data-dataMed) / dataMAD
zscorethresh = 3

fig, ax = plt.subplots(2, 1, figsize= (8, 6))

ax[0].plot(data, 'k^', markerfacecolor='w', markersize=12)
ax[0].set_xticks([])
ax[0].set_xlabel('Data index')
ax[0].set_ylabel('Orig. scale')

# then plot the zscores
ax[1].plot(dataMz, 'k^', markerfacecolor='w', markersize=12)
ax[1].plot([0, N], [zscorethresh, zscorethresh], 'r--')
ax[1].set_xlabel('Data index')
ax[1].set_ylabel('Median dev. units (Mz)')
plt.show()


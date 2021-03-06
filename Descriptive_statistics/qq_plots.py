import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

n = 1000
data = np.random.randn(n)
data_log_normal = np.exp(np.random.randn(n)*.8)

# theoretical normal distribution given N
x = np.linspace(-4, 4, 10001)
theonorm = stats.norm.pdf(x)
theonorm = theonorm/max(theonorm)

yy, xx = np.histogram(data, 40)
yy = yy/max(yy)
xx = (xx[:-1]+xx[1:])/2

# plt.plot(xx, yy, label='Empirical')
# plt.plot(x, theonorm, label='Theoretical')
# plt.legend()
# plt.show()

zSortData = np.sort(stats.zscore(data))
sortNormal = stats.norm.ppf(np.linspace(0, 1, n))

# # QQ plot is theory vs reality
# plt.plot(sortNormal, zSortData, 'o')
#
#
# plt.xlabel('Theoretical normal')
# plt.ylabel('Observed data')
# plt.title('QQ plot')
# plt.axis('square')
# plt.show()

## Python solution

x = stats.probplot(data,plot=plt)
plt.show()

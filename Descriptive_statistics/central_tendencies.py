import matplotlib.pyplot as plt
import numpy as np

# the distributions
N = 10001   # number of data points
bins = 30  # number of histogram bins

d1 = np.random.randn(N) - 1
d2 = 3*np.random.randn(N)
d3 = np.random.randn(N) + 1

# need their histograms
y1, x1 = np.histogram(d1, bins)
x1 = (x1[1:]+x1[:-1])/2

y2, x2 = np.histogram(d2, bins)
x2 = (x2[1:]+x2[:-1])/2

y3, x3 = np.histogram(d3, bins)
x3 = (x3[1:]+x3[:-1])/2

# plot them
plt.plot(x1, y1, 'b')
plt.plot(x2, y2, 'r')
plt.plot(x3, y3, 'k')


plt.xlabel('Data values')
plt.ylabel('Data counts')

# compute the means
mean_d1 = sum(d1) / len(d1)
mean_d2 = np.mean(d2)
mean_d3 = np.mean(d3)

# plot them
plt.plot(x1, y1, 'b', x2, y2, 'r', x3, y3, 'k')
plt.plot([mean_d1, mean_d1], [0, max(y1)], 'b--')
plt.plot([mean_d2, mean_d2], [0, max(y2)], 'r--')
plt.plot([mean_d3, mean_d3], [0, max(y3)], 'k--')

plt.xlabel('Data values')
plt.ylabel('Data counts')
plt.show()

# new dataset of distribution combinations
d4 = np.hstack((np.random.randn(N)-2, np.random.randn(N)+2))
# and its histogram
[y4, x4] = np.histogram(d4, bins)
x4 = (x4[:-1]+x4[1:])/2

# and its mean
mean_d4 = np.mean(d4)


plt.plot(x4, y4, 'b')
plt.plot([mean_d4, mean_d4], [0, max(y4)], 'b--')

plt.xlabel('Data values')
plt.ylabel('Data counts')
plt.show()

# create a log-normal distribution
shift = 0
stretch = .7
n = 2000
bins = 50

# generate data
data = stretch*np.random.randn(n) + shift
data = np.exp(data)
# and its histogram
y, x = np.histogram(data, bins)
x = (x[:-1]+x[1:])/2

# compute mean and median
data_mean = np.mean(data)
data_median = np.median(data)


# plot data
fig, ax = plt.subplots(2, 1, figsize=(4, 6))
ax[0].plot(data, '.', color=[.5, .5, .5], label='Data')
ax[0].plot([1, n], [data_mean, data_mean], 'r--', label='Mean')
ax[0].plot([1, n], [data_median, data_median], 'b--', label='Median')
ax[0].legend()

ax[1].plot(x, y)
ax[1].plot([data_mean, data_mean], [0, max(y)], 'r--')
ax[1].plot([data_median, data_median], [0, max(y)], 'b--')
ax[1].set_title('Log-normal data histogram')
plt.show()



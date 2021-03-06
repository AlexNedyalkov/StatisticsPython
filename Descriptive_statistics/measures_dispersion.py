import matplotlib.pyplot as plt
import numpy as np

N = 10001
bins = 30

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


# # plot them
# plt.plot(x1, y1, 'b')
# plt.plot(x2, y2, 'r')
# plt.plot(x3, y3, 'k')
#
# plt.xlabel('Data values')
# plt.ylabel('Data counts')
# plt.show()


mean_val = 10.2
std_val = 7.5
num_samp = 123

# this
np.random.normal(mean_val, std_val, num_samp)

# is equivalent to
np.random.randn(num_samp)*std_val + mean_val

# compute the means
mean_d1 = sum(d1) / len(d1)
mean_d2 = np.mean(d2)
mean_d3 = np.mean(d3)

# initialize
stds = np.zeros(3)

# compute standard deviations
stds[0] = np.std(d1, ddof=1)
stds[1] = np.std(d2, ddof=1)
stds[2] = np.std(d3, ddof=1)


# same plot as earlier
plt.plot(x1, y1, 'b', x2, y2, 'r', x3, y3, 'k')
plt.plot([mean_d1, mean_d1], [0, max(y1)], 'b--', [mean_d2, mean_d2], [0, max(y2)], 'r--',
         [mean_d3, mean_d3], [0, max(y3)], 'k--')

# now add stds
plt.plot([mean_d1-stds[0], mean_d1+stds[0]], [.4*max(y1), .4*max(y1)], 'b', linewidth=10)
plt.plot([mean_d2-stds[1], mean_d2+stds[1]], [.5*max(y2), .5*max(y2)], 'r', linewidth=10)
plt.plot([mean_d3-stds[2], mean_d3+stds[2]], [.6*max(y3), .6*max(y3)], 'k', linewidth=10)

plt.xlabel('Data values')
plt.ylabel('Data counts')
plt.show()


# illustrate the difference between the different measures of dispersion
variances = np.arange(1, 11)
N = 300

var_measures = np.zeros((4, len(variances)))

for i in range(len(variances)):
    # create data and mean-center
    data = np.random.randn(N) * variances[i]
    data_cent = data - np.mean(data)

    # variance
    var_measures[0, i] = sum(data_cent ** 2) / (N - 1)

    # "biased" variance
    var_measures[1, i] = sum(data_cent ** 2) / N

    # standard deviation
    var_measures[2, i] = np.sqrt(sum(data_cent ** 2) / (N - 1))

    # MAD (mean absolute difference)
    varmeasures[3, i] = sum(abs(data_cent)) / (N - 1)

# show them!
plt.plot(variances, var_measures.T)
plt.legend(('Var', 'biased var', 'Std', 'MAD'))
plt.show()


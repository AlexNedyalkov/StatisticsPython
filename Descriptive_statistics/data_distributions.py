import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

N = 1001

x = np.linspace(-4, 4, N)
gausdist = stats.norm.pdf(x)

plt.plot(x, gausdist)
plt.title('Analytic Gaussian (normal) distribution')
plt.show()

print(sum(gausdist*(-x[0] + x[1])))

# increase the std
stretch_distribution = 1
# shift the mean
shift_distribution = 5
n = 1000

# Normally-distributed random numbers
data = stretch_distribution*np.random.randn(n) + shift_distribution

# plot data
plt.hist(data, 25)
plt.title('Empirical normal distribution')
plt.show()

# Uniformly-distributed numbers
data = stretch_distribution*np.random.rand(n) + shift_distribution-stretch_distribution/2

# plot data
fig,ax = plt.subplots(2, 1, figsize=(5, 6))

ax[0].plot(data, '.', markersize=1)
ax[0].set_title('Uniform data values')

ax[1].hist(data, 25)
ax[1].set_title('Uniform data histogram')

plt.show()

# log-normal distribution

N = 1001
x = np.linspace(0, 10, N)
lognormdist = stats.lognorm.pdf(x, 1)

plt.plot(x, lognormdist)
plt.title('Analytic log-normal distribution')
plt.show()

# empirical log-normal distribution


stretch_distribution = .5
n = 2000
# generate data
data = stretch_distribution*np.random.randn(n) + shift_distribution
data = np.exp(data)

# plot data
fig, ax = plt.subplots(2, 1, figsize=(4, 6))
ax[0].plot(data, '.')
ax[0].set_title('Log-normal data values')

ax[1].hist(data, 25)
ax[1].set_title('Log-normal data histogram')
plt.show()


# binomial

# a binomial distribution is the probability of K heads in N coin tosses,
# given a probability of p heads (e.g., .5 is a fair coin).

# number on coin tosses
n = 10
# probability of heads
p = .9
x = range(n+2)
bindist = stats.binom.pmf(x, n, p)

plt.bar(x, bindist)
plt.title(f'Binomial distribution (n={n}, p={p})')
plt.show()


#t

x = np.linspace(-4, 4, 1001)
df = 200
t = stats.t.pdf(x, df)

plt.plot(x,t)
plt.xlabel('t-value')
plt.ylabel('P(t | H$_0$)')
plt.title(f't({df}) distribution')
plt.show()



# parameters
num_df = 5   # numerator degrees of freedom
den_df = 100 # denominator df

# values to evaluate
x = np.linspace(0, 10, 10001)

# the distribution
fdist = stats.f.pdf(x, num_df, den_df)

plt.plot(x,fdist)
plt.title(f'F({num_df},{den_df}) distribution')
plt.xlabel('F value')
plt.show()

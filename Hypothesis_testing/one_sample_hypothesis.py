import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

N = 20  # sample size
population_mean = 0.5
data = np.random.randn(N) + population_mean

H0val = 0

# compute the t-value
t_num = np.mean(data) - H0val
t_den = np.std(data, ddof=1) / np.sqrt(N)
t_value = t_num / t_den

df = N-1
p_value = (1-stats.t.cdf(abs(t_value), df)) * 2

x = np.linspace(-4, 4, 1001)
t_distribution = stats.t.pdf(x, df) * np.mean(np.diff(x))

plt.plot(x, t_distribution, linewidth=2)
plt.plot([t_value, t_value], [0,max(t_distribution)], 'r--')
plt.legend(('H_0 distribution', 'Observed t-value'))
plt.xlabel('t-value')
plt.ylabel('pdf(t)')
plt.title('t(%g) = %g, p=%g'%(df, t_value, p_value))
plt.show()


t, p = stats.ttest_1samp(data,H0val)
print(t, p)

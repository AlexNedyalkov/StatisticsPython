import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

n = 1000
data = np.random.randn(n)**2

iqrange2 = stats.iqr(data)

print(iqrange2)

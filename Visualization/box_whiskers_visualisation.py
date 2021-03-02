import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

m = 30
n = 6

data = np.zeros((m, n))

for i in range(n):
     data[:, i] = 30*np.random.randn(m) * (2*i/(n-1)-1)**2 + (i+1)**2

plt.boxplot(data)
plt.show()

sns.boxplot(data=data, orient='v')
plt.show()



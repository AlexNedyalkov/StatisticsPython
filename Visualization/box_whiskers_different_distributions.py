import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

N = 100000
data_normal_distribution = np.random.randn(N)
data_uniform_distribution = np.random.rand(N)

fig, ax = plt.subplots(1, 2, figsize=(8, 8))
ax[0].set_title('Normal Distribution')
ax[1].set_title('Uniform Distribution')
# ax[0].hist(data_normal_distribution)
# ax[1].hist(data_uniform_distribution)
# plt.show()

ax[0].boxplot(data_normal_distribution)
ax[1].boxplot(data_uniform_distribution)
plt.show()

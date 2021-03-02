import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# data are groups (rows) X property (columns)
m = [[2, 5, 4, 3], [1, 1, 8, 6]]

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8,8))

# conceptualizing the data as <row> groups of <columns>
ax[0, 0].imshow(m)

# using pandas dataframe
df = pd.DataFrame(m, columns=['prop 0', 'prop 1', 'prop 2', 'prop 3'])
df.plot(ax=ax[1, 0], kind='bar')
ax[1, 0].set_title('Grouping by rows')

# now other orientation (property X group)
ax[0, 1].imshow(np.array(m).T)
df.T.plot(ax=ax[1, 1], kind='bar')
ax[1, 1].set_title('Grouping by columns')
plt.show()


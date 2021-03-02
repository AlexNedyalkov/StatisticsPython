import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# create data for the plot
nbins = 5
totalN = 100

rawdata = np.ceil(np.logspace(np.log10(1/2), np.log10(nbins-.01), totalN))


# prepare data for pie chart
uniquenums = np.unique(rawdata)
data4pie = np.zeros(len(uniquenums))

for i in range(len(uniquenums)):
    data4pie[i] = sum(rawdata == uniquenums[i])

plt.pie(data4pie, labels=100*data4pie/sum(data4pie))
plt.show()
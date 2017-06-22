import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

# Set up JB's preferred style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

def ecdf(data):
    """
    Compute the empirical cumulative distribution function, or ECDF
    for given data.
    """

    # Compute x by sorting the array data.
    x = np.sort(data)

    # Compute y. 1/n ... 1
    y = np.arange(1, len(data)+1)/len(data)

    return x, y

# Load in data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# compute x and y for plotting
high_x, high_y = ecdf(xa_high)
low_x, low_y = ecdf(xa_low)

# Setup the plot Area
fig, ax = plt.subplots(1,1)
_ = ax.set_xlabel('cross-sectional area (µm$^2$)')
_ = ax.set_ylabel('ECDF')

_ = ax.plot(high_x, high_y, marker='.', linestyle='none')
_ = ax.plot(low_x, low_y, marker='*', linestyle='none')
plt.show()

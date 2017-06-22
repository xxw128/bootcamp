import numpy as np
import bootcamp_utils
import scipy.stats
import matplotlib.pyplot as plt

import seaborn as sns

# Set up JB's preferred style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

# Load data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# compute x and y for plotting
high_x, high_y = bootcamp_utils.ecdf(xa_high)
low_x, low_y = bootcamp_utils.ecdf(xa_low)

# Make smooth x-values
x = np.linspace(1600, 2500, 400)

# Compute theoretical Normal distribution
cdf_low = scipy.stats.norm.cdf(x, loc=np.mean(xa_low), scale=np.std(xa_low))
cdf_high = scipy.stats.norm.cdf(x, loc=np.mean(xa_high), scale=np.std(xa_high))

# Setup the plot Area
fig, ax = plt.subplots(1,1)
_ = ax.set_xlabel('cross-sectional area (µm$^2$)')
_ = ax.set_ylabel('ECDF')

#plot theoretical curves
_ = ax.plot(x,cdf_low, color='grey')
_ = ax.plot(x,cdf_high, color = 'grey')

#plot ECDFs
_ = ax.plot(high_x, high_y, marker='.', linestyle='none', label='high_food')
_ = ax.plot(low_x, low_y, marker='.', linestyle='none', label='low_food')

# Make the legend
ax.legend(loc='lower right')

plt.show()

"""
Useful codes for data processing.
From Bootcamp 2017. Instructor Dr. Justin Bois.
Author: Xia
Contents:
    -function- ecdf(data) : Computes the empirical cumulative distribution
    - - ...
"""

import numpy as np

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

def ecdf_plot(data, value, hue=None, formal=False, buff=0.1, min_x=None, max_x=None, 
              ax=None):
    """
    Generate `x` and `y` values for plotting an ECDF.

    Parameters
    ----------
    data : Pandas DataFrame
        Tidy DataFrame with data sets to be plotted.
    value : column name of DataFrame
        Name of column that contains data to make ECDF with.
    hue : column name of DataFrame
        Name of column that identifies labels of data. A seperate
        ECDF is plotted for each unique entry.
    formal : bool, default False
        If True, generate `x` and `y` values for formal ECDF.
        Otherwise, generate `x` and `y` values for "dot" style ECDF.
    buff : float, default 0.1
        How long the tails at y = 0 and y = 1 should extend as a
        fraction of the total range of the data. Ignored if
        `formal` is False.
    min_x : float, default None
        Minimum value of `x` to include on plot. Overrides `buff`.
        Ignored if `formal` is False.
    max_x : float, default None
        Maximum value of `x` to include on plot. Overrides `buff`.
        Ignored if `formal` is False.
    ax : matplotlib Axes
        Axes object to draw the plot onto, otherwise makes a new
        figure/axes.

    Returns
    -------
    output : matplotlib Axes
        Axes object containg ECDFs.
    """

    # Set up axes
    if ax is None:
        fig, ax = plt.subplots(1, 1)
        ax.set_xlabel(str(value))
        ax.set_ylabel('ECDF')

    if hue is None:
        x, y = ecdf(data[value], formal=formal, buff=buff, min_x=min_x, max_x=max_x)

        # Make plots
        if formal:
            _ = ax.plot(x, y)
        else:
            _ = ax.plot(x, y, marker='.', linestyle='none')
    else:
        gb = data.groupby(hue)
        ecdfs = gb[value].apply(ecdf, formal=formal, buff=buff, min_x=min_x, max_x=max_x)

        # Make plots
        if formal:
            for i, xy in ecdfs.iteritems():
                _ = ax.plot(*xy)
        else:
            for i, xy in ecdfs.iteritems():
                _ = ax.plot(*xy, marker='.', linestyle='none')

        # Add legend
        ax.legend(ecdfs.index, loc=0)

    return ax


def bs_replicate(data, func=np.mean):
    """Compute a bootstrap replicate for data, doing the 'func' function."""
    bs_sample = np.random.choice(data, replace=True, size=len(data))
    return func(bs_sample)

def draw_bs_reps(data, func=np.mean, size=10000):
    """Draw bootstrap replicates from 1d data."""
    return np.array([bs_replicate(data, func=func) for _ in range(size)])

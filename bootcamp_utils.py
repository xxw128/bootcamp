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

def bs_replicate(data, func=np.mean):
    """Compute a bootstrap replicate for data, doing the 'func' function."""
    bs_sample = np.random.choice(data, replace=True, size=len(data))
    return func(bs_sample)

def draw_bs_reps(data, func=np.mean, size=10000):
    """Draw bootstrap replicates from 1d data."""
    return np.array([bs_replicate(data, func=func) for _ in range(size)])

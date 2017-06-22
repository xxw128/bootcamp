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

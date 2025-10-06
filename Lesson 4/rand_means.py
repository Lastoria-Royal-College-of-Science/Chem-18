import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def gen_rand_means(n=10):
    """
    Generate an array of random means calculated over multiple iterations.

    This function computes the means of randomly generated integers within a
    range [0, 101) for a specified number of samples `n`. The process is
    repeated 10,000 times, and the resulting means are stored in an array,
    which is returned as the output.

    :param n: Number of random integers to generate for each iteration
               (default is 10).
    :type n: int
    :return: An array of calculated means from 10,000 iterations.
    :rtype: numpy.ndarray
    """
    rm_array = np.array([])
    for _ in range(10000):
        rand_vars = np.random.randint(0,101,n)
        rm_array = np.append(rm_array, np.mean(rand_vars))
    return rm_array

def rand_means_stats(rm_array):
    return np.mean(rm_array), np.std(rm_array)
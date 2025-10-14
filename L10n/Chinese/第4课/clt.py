"""
**You should learn Lesson 1.5 and preferably 3.5 before check this script!**

Provides interactive statistical visualizations using uniform random variables
and associated normal distributions.

This module allows users to generate a histogram comparing uniform random
variables and their associated normal distributions, along with an interactive
widget for parameter adjustment. The visualization includes multiple subplots
and is designed for dynamic interaction.
"""


from ipywidgets import interact
import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt


def make_plot(n: int = 1):
    """
    Generates and displays plots comparing the histogram of uniform random variables
    and their corresponding normal distribution across multiple subplots. The number
    of random variables can be adjusted using the parameter.

    :param n: The number of columns in the uniform random matrix. This determines
        the number of random variables whose means will be calculated and plotted.
    :type n: int
    :return: None
    """
    rm_array = np.random.rand(1000000, n).mean(axis=1)

    mean, std = rm_array.mean(), rm_array.std()
    x_min, x_max = mean - 5*std, mean + 5*std
    norm_x = np.linspace(x_min, x_max, 1000)

    plt.figure(figsize=(10, 6))

    plt.subplot(2,2,(1,2))
    plt.hist(rm_array, bins='auto', range=(x_min, x_max), density=True, histtype='stepfilled', label='Random Variables')
    plt.plot(norm_x, norm.pdf(norm_x, loc=mean, scale=std), label='Normal Distribution')
    plt.xlim(x_min, x_max)
    plt.legend()
    plt.title('Uniform Distribution and Its Associated Normal Distribution')

    plt.subplot(2,2,3)
    plt.hist(rm_array, bins='auto', range=(x_min, x_max), density=True, histtype='stepfilled', label='Random Variables')
    plt.plot(norm_x, norm.pdf(norm_x, loc=mean, scale=std), label='Normal Distribution')
    plt.xlim(x_min-4*std, x_max-4*std)
    plt.ylim(0, 0.002)
    plt.legend()

    plt.subplot(2,2,4)
    plt.hist(rm_array, bins='auto', range=(x_min, x_max), density=True, histtype='stepfilled', label='Random Variables')
    plt.plot(norm_x, norm.pdf(norm_x, loc=mean, scale=std), label='Normal Distribution')
    plt.xlim(x_min+4*std, x_max+4*std)
    plt.ylim(0, 0.002)
    plt.legend()

    plt.tight_layout()
    plt.show()


def show_plot():
    """
    Displays an interactive plot control widget.

    This function uses the `interact` method to create an interactive widget for
    adjusting parameters of the `make_plot` function. The widget allows users to
    adjust the number parameter (`n`) within a specified range. The range and step
    size for the parameter are provided explicitly, enabling dynamic interaction
    with the plot.

    :return: The interactive widget instance created by `interact`. It enables
        users to manipulate the given parameter for real-time updates to the plot.
    """
    return interact(make_plot, n=(1, 30, 1))

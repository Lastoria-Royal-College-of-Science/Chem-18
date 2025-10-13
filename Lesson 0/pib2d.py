"""
Computational visualization and simulation of the 2D quantum Particle in a Box (PIB) wavefunction.

This module provides functions to compute and visualize the 2D PIB wavefunction, including its
time and quantum number dependency. The visualization is performed using 3D plotting and
interactive widgets to allow dynamic parameter adjustments.
"""

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact


L = 1
A = 2/L


def pib_2d(t: float = 0, nx: int = 1, ny: int = 1):
    """
    Calculates the 2D Particle in a Box (PIB) wavefunction based on quantum numbers,
    spatial coordinates, and time evolution.

    The function computes the spatial grid and evaluates the PIB wavefunction for the given
    energy levels in the x and y direction (denoted by quantum numbers) and time parameter `t`.
    The wavefunction considers both spatial and temporal variations.

    :param t: Time parameter influencing the temporal evolution of the wavefunction
              in a cosine function.
    :type t: float
    :param nx: Quantum number associated with the wavefunction's x-direction,
               determines the number of spatial variations along x.
    :type nx: int
    :param ny: Quantum number associated with the wavefunction's y-direction,
               determines the number of spatial variations along y.
    :type ny: int
    :return: A tuple containing:
             - X: 2D array for x-coordinates across spatial grid.
             - Y: 2D array for y-coordinates across spatial grid.
             - Z: Evaluated wavefunction at each point in the X, Y spatial grid.
    :rtype: tuple
    """
    x = np.linspace(0, L, 100)
    y = np.linspace(0, L, 100)
    X, Y = np.meshgrid(x, y)
    return X, Y, A * np.sin(nx*np.pi*X/L) * np.sin(ny*np.pi*Y/L) * np.cos(t)


def make_plot(t: float = 0, nx: int = 1, ny: int = 1):
    """
    Generates a 3D plot visualization for a given set of parameters.

    The function creates a 3D surface plot based on the provided time
    `t`, and integers `nx`, `ny`. The plot has predefined visual limits
    and uses a surface generated from a helper function `pib_2d`. A
    color map is applied for better visualization.

    :param t: The time parameter, which influences the plot generation.
    :type t: float
    :param nx: The x-axis resolution or index for the plot.
    :type nx: int
    :param ny: The y-axis resolution or index for the plot.
    :type ny: int
    :return: None. Displays the generated 3D plot.
    """
    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_zlim(-A, A)
    ax.plot_surface(*pib_2d(t, nx, ny), cmap='viridis')
    plt.show()


def show_plot():
    """
    Generates and displays an interactive plot.

    This function uses the `interact` tool to create an interactive widget. It allows
    the user to control and alter parameters `t`, `nx`, and `ny` within specified ranges,
    dynamically updating the plot based on these values.

    :return: Returns an interactive widget for creating and manipulating the plot.
    :rtype: Any
    """
    return interact(make_plot, t=(0, 2*np.pi, np.pi/6), nx=(1, 5, 1), ny=(1, 5, 1))

# TODO: needs to animate

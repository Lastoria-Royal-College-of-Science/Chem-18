import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact


L = 2

x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x,y)


def pib_2d(x, y, nx: int = 1, ny: int = 1, t = 0):
    return (2/L) * np.sin(nx*np.pi*X/L) * np.sin(ny*np.pi*Y/L) * np.cos(t)


def make_plot(nx=1, ny=1, t: float=0):
    Z = pib_2d(x, y, nx, ny, t)
    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    plt.show()


def show_plot():
    return interact(make_plot, nx=(1, 10, 1), ny=(1, 10, 1), t=(0, 2*np.pi, ))

# needs to animate


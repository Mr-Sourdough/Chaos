import matplotlib.pyplot as plt
import numpy as np
from plotting_3d import exact_lin_soln, lorenz_eq

"""
- Not appropriate for varying h yet
- Only gives plot, not suitable for creating tables
"""


def method_error(brsigma, tmax, h, x_0, method):
    # initialise time
    t = 0

    # create plot arrays
    error = np.empty(0)
    ts = np.empty(0)

    xs, ys, zs = lorenz_eq(brsigma, tmax, h, x_0, method, linearise=True)
    exact_xs, exact_ys, exact_zs = exact_lin_soln(brsigma, tmax, h, x_0)
    for i in range(len(exact_xs)):
        method_vec = np.array([xs[i], ys[i], zs[i]])
        exact_vec = np.array([exact_xs[i], exact_ys[i], exact_zs[i]])
        error = np.append(error, np.linalg.norm(method_vec - exact_vec))
        ts = np.append(ts, t)
        t += h

    # create plot
    fig = plt.figure("Error analysis")
    plt.xlabel('time')
    plt.ylabel('distance from exact solution')
    plt.semilogy(ts, error)
    return fig

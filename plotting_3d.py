import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import exp


def draw_axes(title=None):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_title(title)
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')
    return ax


def lorenz_eq(brsigma, tmax, h, x_0, method, ax=None, linearise=False, coord=True):
    """
    Plots the solution of the Lorenz system
    - brsigma is a tuple with the parameters b, r and sigma
    - tmax is the time to which the routine is run; needs to be float
    - h is the step size;
      if adaptive step size implemented, then initial step size
    - x_0 is the initial condition at t = 0 as numpy array
    - method is the timestepping routine to be used to integrate;
      still need to adapt for Richardson extrapolation
    - ax is the set of 3d axes drawn with draw_axes()
    - linearise parameter set to True evaluates for the linearised system
    - coord parameter causes the f-n to return the plot arrays;
      set coord to False to generate plot.
    """
    x = x_0
    # initialise xs, ys and zs
    xs = np.array(x_0[0])
    ys = np.array(x_0[1])
    zs = np.array(x_0[2])

    # initialiase time t
    t = 0
    # times, hs = [], []

    # creates the plot arrays
    while t <= tmax:
        # times.append(t)
        # hs.append(h)
        x = method(x, h, brsigma, linearise)
        xs = np.append(xs, x[0])
        ys = np.append(ys, x[1])
        zs = np.append(zs, x[2])
        # here put function for generating h
        # h = ts.step_size(x, h, brsigma, method, 4, 10**-4)
        t += h
    if coord is True:
        return xs, ys, zs
    else:
        # create 3d plot
        ax.scatter(x_0[0], x_0[1], x_0[2], marker='.')
        ax.text(x_0[0], x_0[1], x_0[2],
                "{}".format(tuple(x_0)))
        ax.plot(xs, ys, zs, lw=0.75)
        # print(times, hs, len(times), sep='\n')
        return ax


def exact_lin_soln(brsigma, tmax, h, x_0, ax=None, coord=True):
    """
    Plots the linearised solution around the origin.
    - brsigma is a tuple with the parameters b, r and sigma
    - tmax is the time to which the routine is run;
      best not to take tmax > 1.0; needs to be float
    - h is the step size
    - x_0 is the initial condition at t = 0 as numpy array
    - ax is the set of 3d axes drawn with draw_axes()
    - coord parameter causes the f-n to return the plot arrays;
      set coord to False to generate plot.
    """
    # Jacobian matrix calculated at origin
    Jacobian_origin = np.array([[-brsigma[2], brsigma[2], 0],
                                [brsigma[1], -1, 0],
                                [0, 0, -brsigma[0]]])

    # Eigenvalues and eigenvectors & calc constant vector
    val, vec = np.linalg.eig(Jacobian_origin)
    C = np.linalg.solve(vec, x_0)

    # Initialise plot lists
    xs = np.array([x_0[0]])
    ys = np.array([x_0[1]])
    zs = np.array([x_0[2]])

    for t in np.arange(0+h, tmax+h, h):
        x = x_0 * 0
        for i in range(3):
            x = np.add(x, C[i] * vec[:, i] * exp(val[i]*t))
        xs = np.append(xs, x[0])
        ys = np.append(ys, x[1])
        zs = np.append(zs, x[2])

    if coord is True:
        return xs, ys, zs
    else:
        # creates 3d plot
        ax.scatter(x_0[0], x_0[1], x_0[2], marker='x')
        ax.text(x_0[0], x_0[1], x_0[2],
                "{}".format(tuple(x_0)))
        ax.plot(xs, ys, zs, lw=2.0)
        return ax

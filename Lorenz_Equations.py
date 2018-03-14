import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import timestepping as tstep

'''
brsigma is a tuple with the parameters b, r, and sigma in the Lorenz Equations
initial time t is set to zero and runs to tmax (needs to be a float)
h is the step size (if adaptive step size implemented, then initial step size)
x_0 is the initial condition in the form np.array([x, y, z])
with x, y and z being the coordinates
linearise parameter set to True evaluates for the linearised system
'''

fig = plt.figure("Lorenz System")
ax = Axes3D(fig)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


def lorenz_eq(brsigma, tmax, h, x_0, method, linearise=False, coord=True):
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
        ax.set_title("Lorenz System")
        ax.scatter(x_0[0], x_0[1], x_0[2])
        ax.text(x_0[0], x_0[1], x_0[2],
                "({}, {}, {})".format(x_0[0], x_0[1], x_0[2]))
        ax.plot(xs, ys, zs)
        # print(times, hs, len(times), sep='\n')
        return fig


lorenz_eq((1, 4, 1), 1.0, 0.01, np.array([1, -1, 2]),
          tstep.step_rk2, coord=False)
plt.show()

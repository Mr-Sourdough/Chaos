import numpy as np
import matplotlib.pyplot as pt
import timestepping as ts
from mpl_toolkits.mplot3d import Axes3D

'''
For this function, b, r, and sigma are the parameters in the Lorenz Equations
initial time t is set to zero and runs to tmax
with nsteps being the number of steps taken between t and tmax
points is a list of tuples, where the first argument of the tuple
is the position at the initial time in the form np.array([x, y, z])
with x, y and z being the coordinates
and the second being the colour of the line drawn from that point.
If
'''

def lorenz_eq(b, r, sigma, t=0, tmax, nsteps, points, save=False):
    # create 3d figure to plot on
    fig = pt.figure()
    ax = fig.gca(projection='3d')

    # calculate the time step
    dt = tmax / nsteps

    # first loop goes over each point
    for x, c in points:
        # initialise xs, ys and zs arrays
        xs = np.array(x[0])
        ys = np.array(x[1])
        zs = np.array(x[2])

        n = 0  # number of timesteps taken; initialise to 0

        # creates the plot arrays
        for steps in range(nsteps):
            x = ts.step_rk2(x, dt, b, r, sigma)
            t += dt
            n += 1
            xs = np.append(xs, x[0])
            ys = np.append(ys, x[1])
            zs = np.append(zs, x[2])

            ax.plot(xs, ys, zs, c, lw=0.1)  # plot the arrays...
        ax.scatter(x[0], x[1], x[2])  # and initial points

    if save == True:
        pt.savefig()  # save plot to file...
    else:
        pt.show()  # or show the final image

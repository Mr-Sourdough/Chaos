import matplotlib.pyplot as plt
import numpy as np
import timestepping as ts

x0 = np.array([10**-6, 10**-6, 10**-6])

# This version of the lorenz_eq function generates the points
# to measure the distance from x0


def lorenz_points(b, r, sigma, tmax, nsteps, x0, x, t=0, save=False):
    # calculate the time step
    dt = tmax / nsteps

    # creates the plot arrays
    dist = np.empty()
    for steps in range(nsteps):
        x = ts.step_rk2(x, dt, b, r, sigma)
        np.append(dist, np.linalg.norm(x - x0))
    # generate a time values array to plot dist against
    ts = np.array([(t + n * dt) for n in range(1, nsteps + 1)])
    plt.plot(ts, dist)

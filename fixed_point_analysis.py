import matplotlib.pyplot as plt
import numpy as np
import timestepping as tstep
from Lorenz_Equations import lorenz_eq

x0 = np.array([10**-6, 10**-6, 10**-6])

# This version of the lorenz_eq function generates the points
# to measure the distance from x0
# x is a single point as np.array


def lorenz_points(b, r, sigma, tmax, nsteps, x):  # put dt size instead of nsteps
    # calculate the time step
    dt = tmax / nsteps

    # creates the plot arrays
    dist = np.empty(nsteps)
    for steps in range(nsteps):
        x = tstep.step_rk2(x, dt, b, r, sigma)
        np.append(dist, np.linalg.norm(x - x0))  # put x0 into the function you moron

    # generate a time values array to plot dist against
    ts = np.linspace(0, tmax, nsteps)

    plt.figure()
    plt.plot(ts, dist)
    plt.show()
    return None


lorenz_eq(8 / 3, 28, 10, 5.0, 500, [x0], save=True)
lorenz_points(8 / 3, 28, 10, 5.0, 500, x0)

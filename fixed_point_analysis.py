import matplotlib.pyplot as plt
import numpy as np
import timestepping as tstep
from Lorenz_Equations import lorenz_eq

x_0 = np.array([10**-7, 10**-7, 10**-7])

'''
This version of the lorenz_eq function generates the points
to measure the distance from x0
x is a single point as np.array
'''


def lorenz_points(brsigma, tmax, nsteps, x):
    dt = tmax / nsteps  # calculate the time step
    x0 = x  # save initial point

    # creates the plot arrays
    dist = np.empty(0)
    for steps in range(nsteps):
        dist = np.append(dist, np.linalg.norm(x - x0))
        x = tstep.step_rk2(x, dt, brsigma)

    # generate a time values array to plot dist against
    ts = np.linspace(0, tmax, nsteps)

    plt.figure()
    plt.plot(ts, dist)
    plt.show()
    return None


sigma = 10
m = 20.0
n = int(m * 100)
brsigma = (8/3, 28, sigma)

lorenz_eq(brsigma, m, n, [x_0])
lorenz_points(brsigma, m, n, x_0)

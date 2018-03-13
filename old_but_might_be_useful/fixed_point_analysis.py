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


def lorenz_points(brsigma, tmax, h, x):
    x0 = x  # save initial point
    t = 0  # initialise time

    # create plot arrays
    dist = np.empty(0)
    ts = np.empty(0)

    while t <= tmax:
        dist = np.append(dist, np.linalg.norm(x - x0))
        x = tstep.step_rk2(x, h, brsigma)
        ts = np.append(ts, t)
        # here put function for generating h
        t += h

    fig = plt.figure()
    plt.title('$x_0$ = {}'.format(x_0))
    plt.xlabel('time')
    plt.ylabel('distance from $x_0$')
    plt.plot(ts, dist)
    return fig


sigma = 24
m = 10.0
h = 0.02
brsigma = (8/3, 28, sigma)

lorenz_eq(brsigma, m, h, x_0)
plt.show()
# lorenz_points(brsigma, m, n, x_0)

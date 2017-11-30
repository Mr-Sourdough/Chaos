import matplotlib.pyplot as plt
import numpy as np

x0 = np.array([10**-6, 10**-6, 10**-6])

# This version of the lorenz_eq function generates the points
# to measure the distance from x0
def lorenz_points(b, r, sigma, tmax, nsteps, x, t=0, save=False):

    # calculate the time step
    dt = tmax / nsteps

    # creates the plot arrays
    for steps in range(nsteps):
        x = ts.step_rk2(x, dt, b, r, sigma)
        '''
        add list to append the points to to be able to measure their distance
        use np.linalg.norm(x - x0) to measure distance of x from x0
        '''

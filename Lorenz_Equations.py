# time steps the Lorenz equations
import numpy as np
import matplotlib.pyplot as pt
import timestepping as ts

# parameters
b = 8/3
r = 28
sigma = 10

# time−stepping parameters
tmax = 1  # run to this time
nsteps = 100  # number of time steps
dt = tmax/nsteps  # calculate the time step

# initial conditions
t = 0
x = np.array([1, -1, 20])

n = 0  # number of timesteps taken; initialise to 0
while n < nsteps:
    x = ts.step_rk2(x, dt, b, r, sigma)
    t += dt
    n += 1
    # plot the three variables (red, blue, green dots):
    pt.plot(t, x[0], 'r.')
    pt.plot(t, x[1], 'b.')
    pt.plot(t, x[2], 'g.')

print(t, x[0], x[1], x[2])  # print the final time and coordinates
pt.savefig('test.pdf')  # save the plot to a file

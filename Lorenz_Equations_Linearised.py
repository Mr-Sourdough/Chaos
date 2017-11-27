# time steps the Lorenz equations
import numpy as np
import matplotlib.pyplot as pt
import timestepping_linearised as ts
from mpl_toolkits.mplot3d import Axes3D

# parameters
b = 8 / 3
r = 28
sigma = 10

# time-stepping parameters
tmax = 50  # run to this time
nsteps = 7500  # number of time steps
dt = tmax / nsteps  # calculate the time step

# initial conditions
t = 0
x = np.array([1, -1, 2])

# initialise x, y and z arrays
xs = np.array(x[0])
ys = np.array(x[1])
zs = np.array(x[2])

n = 0  # number of timesteps taken; initialise to 0
for steps in range(nsteps):
    x = ts.step_rk2(x, dt, b, r, sigma)
    t += dt
    n += 1
    xs = np.append(xs, x[0])
    ys = np.append(ys, x[1])
    zs = np.append(zs, x[2])

# plot the three variables in 3D
fig = pt.figure()
ax = fig.gca(projection='3d')
ax.set_xlim(-20, 20)
ax.set_ylim(-40, 40)
ax.plot(xs, ys, zs, lw=0.5)

# show the final image
pt.show()

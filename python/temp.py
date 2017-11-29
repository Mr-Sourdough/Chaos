# -*- coding: utf-8 -*-


# timesteps the Lorenz equations
import numpy as np, matplotlib.pyplot as pt, timestepping as ts
from mpl_toolkits.mplot3d import Axes3D
fig = pt.figure()
ax = fig.add_subplot(111, projection='3d')
# parameters
b =8/3
r =28
sigma =10
# time stepping parameters
tmax=1 # run to this time
nsteps =100 # number of timesteps
dt = tmax/nsteps # calculate the timestep
# initial conditions
t=0
x=np.array([1,-1,1.05])
n=0 # number of time steps taken ; initialise to 0
while n < 100:
  x=ts.step_rk2(x,dt,b,r,sigma)
  t=t+dt
  n=(n+1)
# plot the three variables (red,blue,green dots):
pt.plot(t,x[0],'r. ')
pt.plot(t,x[1],'b. ')
pt.plot(t,x[2],'g. ')
print (t, x[0],x[1],x[2]) # print the final time and coordinates
pt.savefig('test.pdf') # save the plot to a file

x= x[0]
y= x[1]
z= x[2]

ax.plot(x,y,z)
pt.show()

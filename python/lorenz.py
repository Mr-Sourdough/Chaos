# -*- coding: utf-8 -*-


# timesteps the Lorenz equations
import numpy as np, matplotlib.pyplot as pt, timestepping as ts
 

# parameters
b =8/3
r =28
sigma =10
# time stepping parameters
tmax =1 # run to this time
nsteps =250 # number of timesteps
dt=tmax/nsteps # calculate the timestep

# initial conditions
t =0
x =np.array([1,-1,20])

n =0 # number of time steps taken ; initialise to 0
while n < nsteps:
  x =ts.step_rk2(x,dt,b,r,sigma)
  t =t+dt
  n =n+1
  # plot the three variables (red,blue,green dots):
  pt.plot(t, x[0], 'r.', label='x0')
  pt.plot(t, x[1], 'b.', label='x1')
  pt.plot(t, x[2], 'g.', label='x2')

print (t)
print (x[0])
print (x[1])
print (x[2])

 # print the final time and coordinates
pt.savefig('test3.pdf') # save the plot to a file

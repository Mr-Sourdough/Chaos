# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:40:45 2017

@author: user
"""

import numpy as np, matplotlib.pyplot as pt, timestepping as ts
from mpl_toolkits.mplot3d import Axes3D



# parameters
b =8/3
r =28
sigma =10
# time stepping parameters
tmax =3 # run to this time
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
  #  pt.plot(t, x[0], 'r.', label='x0')
  #  pt.plot(t, x[1], 'b.', label='x1')
  #  pt.plot(t, x[2], 'g.', label='x2')
  # fig = pt.figure()
  #  ax = fig.gca(projection='3d')
  a=np.array([x[0],x[1],x[2]]) 
  j=[a[0]]
  k=[a[1]]
  l=[a[2]]
  print(j,k,l)
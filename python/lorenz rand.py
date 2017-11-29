# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:50:32 2017

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:51:42 2017

@author: user
"""
import matplotlib.pyplot as pt
from scipy import integrate
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


pt.rcParams.update({'font.size': 8})


# starting point
x_0 = [50, 100, 100]
x_1 = [60, 20, 30]
x_2 = [0,1,1]

def lorenz(vec, t0, s=10, b=8/3, r=28):
    (x,y,z)=vec
    return [s*(y-x), x*(r-z)-y, x*y-b*z]

ti=0
tf=20
nsteps=10000
t = np.linspace(ti, tf, nsteps)


xt_0 = integrate.odeint(lorenz, x_0, t)
xt_1 = integrate.odeint(lorenz, x_1, t)
xt_2 = integrate.odeint(lorenz, x_2, t)

j_0=[row[0] for row in xt_0]
k_0=[row[1] for row in xt_0]
l_0=[row[2] for row in xt_0]

j_1=[row[0] for row in xt_1]
k_1=[row[1] for row in xt_1]
l_1=[row[2] for row in xt_1]

j_2=[row[0] for row in xt_2]
k_2=[row[1] for row in xt_2]
l_2=[row[2] for row in xt_2]

fig = pt.figure()
ax = fig.gca(projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


ax.plot(j_0,k_0,l_0, 'g', linewidth=0.2, label=x_0)
ax.plot(j_1,k_1,l_1, 'r', linewidth=0.2, label=x_1)
ax.plot(j_2,k_2,l_2, 'b', linewidth=0.2, label=x_2)
hg
ax.legend()
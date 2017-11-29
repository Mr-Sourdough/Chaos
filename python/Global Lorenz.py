# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:46:10 2017
@author: user
"""
import matplotlib.pyplot as pt
from scipy import integrate
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

pt.rcParams.update({'font.size': 8})

a=0.7

def lorenz(vec, t0, s=10, b=8/3, r=a):
    (x,y,z)=vec
    return [s*(y-x), x*(r-z)-y, x*y-b*z]

# starting point
x_0 = [1,0,0]
x_1 = [0,-1,a-1]

ti=0
tf=1
nsteps=10
t = np.linspace(ti, tf, nsteps)

xt_0 = integrate.odeint(lorenz, x_0, t)
xt_1 = integrate.odeint(lorenz, x_1, t)

j_0=[row[0] for row in xt_0]
k_0=[row[1] for row in xt_0]
l_0=[row[2] for row in xt_0]

j_1=[row[0] for row in xt_1]
k_1=[row[1] for row in xt_1]
l_1=[row[2] for row in xt_1]

fig = pt.figure()
ax = fig.gca(projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.plot(j_0,k_0,l_0, 'g', linewidth=0.4, label=x_0)
ax.plot(j_1,k_1,l_1, 'r', linewidth=0.4, label=x_1)
ax.plot([1,0],[0,-1], [0,a-1], 'bx', markersize=5)
ax.legend()

#ax.view_init(0,-25)

#pt.savefig('100.png', dpi=250)
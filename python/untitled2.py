#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:01:09 2017

@author: Phin
"""

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
fig = pt.figure()
ax = fig.gca(projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

a=100

def lorenz(vec, t0, s=10, b=8/3, r=a):
    (x,y,z)=vec
    return [s*(y-x), x*(r-z)-y, x*y-b*z]
# starting point
x_0 = [1,0,0]
x_1 = [0,-1,a-1]

each = [(x_0, 'g'), (x_1, 'r')]

ti=0
tf=1000
nsteps=50000
t = np.linspace(ti, tf, nsteps)

for i, c in each:
    xt_i = integrate.odeint(lorenz, i, t)
    
    j_i=[row[0] for row in xt_i]
    k_i=[row[1] for row in xt_i]
    l_i=[row[2] for row in xt_i]
    
    ax.plot(j_i, k_i, l_i, c, linewidth=0.2, label=i)
    ax.plot([1,0],[0,-1], [0,a-1], 'bx', markersize=5)
    ax.legend()

#ax.view_init(0,-25)

#pt.savefig('100.png', dpi=250)

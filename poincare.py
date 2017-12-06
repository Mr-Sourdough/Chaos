#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:01:09 2017

@author: Phin
"""
import matplotlib.pyplot as pt
from scipy import integrate
import numpy as np

pt.rcParams.update({'font.size': 8})

a=28

q=a-1

def lorenz(vec, t0, s=10, b=8/3, r=a):
    (x,y,z)=vec
    return [s*(y-x), x*(r-z)-y, x*y-b*z]
# starting point
x_0 = [1,-1,20]

ti=0
tf=50
nsteps=5000
t = np.linspace(ti, tf, nsteps)

xt = integrate.odeint(lorenz, x_0, t)

j=[row[0] for row in xt]
k=[row[1] for row in xt]
l=[row[2] for row in xt]

for i in range(nsteps-1):
    if l[i] < q < l[i+1] or l[i] > q > l[i+1]:
        continue
    else:
        j[i], k[i] = 'a', 'a'
if not 26.8 < l[-1] < 27.2:
    j[-1], k[-1] = 'a', 'a'
        

# print(j, '\n', k)

i = 0
while 'a' in j:
    if j[i] == 'a':
        del j[i]
        del k[i]
        del l[i]
    else:
        i += 1 
'''for i in range(1, len(j)):
    print(j[i], k[i], l[i])'''

pt.plot(j, k, l, 'r+', markersize = 5)
#pt.plot(t, j, 'g.')

#pt.plot([1],[0], 'bx', markersize=5)

#ax.view_init(0,-25)

#pt.savefig('100.png', dpi=250)


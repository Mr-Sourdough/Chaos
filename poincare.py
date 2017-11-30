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

def lorenz(vec, t0, s=10, b=8/3, r=a):
    (x,y,z)=vec
    return [s*(y-x), x*(r-z)-y, x*y-b*z]
# starting point
x_0 = [1,0,0]

ti=0
tf=1000
nsteps=50000
t = np.linspace(ti, tf, nsteps)


xt = integrate.odeint(lorenz, x_0, t)

#j=np.array(row[0] for row in xt)
#k=np.array(row[1] for row in xt)
#l=np.array(row[2] for row in xt)

j=[row[0] for row in xt]
k=[row[1] for row in xt]
l=[row[2] for row in xt]

l=27

graph = np.array([j,k])
#psec=np.array([(j,k) '''for (j,k) in graph if l==27'''])

pt.plot(graph)

pt.plot([1],[0], 'bx', markersize=5)
pt.legend()

#ax.view_init(0,-25)

#pt.savefig('100.png', dpi=250)


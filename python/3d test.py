# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:08:36 2017

@author: user
"""
import numpy as np, matplotlib.pyplot as pt, timestepping as ts
from mpl_toolkits.mplot3d import Axes3D

pt.plot([1,2,3], [1,2,3], 'go-', label='line 1')
pt.plot([1,2,3], [1,4,9], 'rs--',  label='line 2')

pt.legend()
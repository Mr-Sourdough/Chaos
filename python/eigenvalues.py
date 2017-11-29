#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:50:47 2017

@author: Phin
"""

import numpy as np
import math
import matplotlib.pyplot as pt
# set standard parameters
b =8/3
sigma =10
r=1.1
# make a 3x3 matrix
a=np.array([[-sigma, sigma, 0],
            [1, -1, math.sqrt(b*(r-1))],
            [math.sqrt(b*(r-1)), math.sqrt(b*(r-1)), -b]])
print (a)
# calculate eigenvalues and eigenvectors
evals,evecs=np.linalg.eig(a)
print(evals)
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 22:25:43 2017

@author: user
"""

import numpy as np
import matplotlib.pyplot as pt

xi = -10
xend = 40
nsteps = 200
step = (xend-xi)/nsteps


x=np.arange(xi, xend, step)

y1 = x+(3/8)+((6*x+8)/(11-3*x))
y2 = -(5/8)-x 
y3 = [0.6875]*nsteps
#print(y3)
pt.plot (x, y1, 'g-', linewidth =0.5, label='$p_1p_2$>$p_0$')
pt.plot (x, y2, 'b-', linewidth =0.5, label='$p_1$>0')
pt.plot (x, y3, 'r-', linewidth =0.5, label='$p_0$>0')
pt.plot (10,28, 'x', c='purple', ms=5, label ='(10,28)')
pt.rcParams.update({'font.size': 10})
pt.xlabel('s')
pt.ylabel('r')
pt.xlim(xi, xend)
pt.ylim(-10, 40)
pt.title('Minimum value of r as a function of s necessary for stable fixed point')
pt.legend(fontsize=6)
pt.show()

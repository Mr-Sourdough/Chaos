# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 14:14:11 2017

@author: user
"""
import matplotlib.pyplot as plt
fig=plt.figure()
plt.axis([0,1000,0,1])

i=0
x=list()
y=list()

while i <1000:
    temp_y=np.random.random()
    x.append(i)
    y.append(temp_y)
    plt.scatter(i,temp_y)
    i+=1
    plt.show()
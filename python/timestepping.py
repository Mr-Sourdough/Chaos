# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:36:24 2017

@author: user
"""
def step_rk2 (x,dt,b,r,sigma):
# advances the input array x (at time t)
# to the returned value x_out (at time t+dt)
    dxdt1 =calc_dxdt(x,b,r,sigma)
    xtemp1 =x+0.5*dt*dxdt1
    dxdt2 =calc_dxdt(xtemp1,b,r,sigma)
    x_out =x+dt*dxdt2
    return x_out

def calc_dxdt(x,b,r,sigma):
# calculates the vector dx/dt for the Lorenz equations
  dxdt=0*x
  dxdt[0]=sigma*(x[1]-x[0])
  dxdt[1]=r*x[0]-x[1]-x[0]*x[2]
  dxdt[2]=x[0]*x[1]-b*x[2]
  
  return dxdt
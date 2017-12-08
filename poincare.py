import matplotlib.pyplot as pt
from scipy import integrate
import numpy as np

pt.rcParams.update({'font.size': 8})

a=5

z_val=a-1

def lorenz(vec, t0, s=10, b=8/3, r=a):
    (x,y,z)=vec
    return [s*(y-x), x*(r-z)-y, x*y-b*z]

x_0 = [0,-1,a-1]

ti=0
tf=40
    
nsteps=25000

t = np.linspace(ti, tf, nsteps)
xt = integrate.odeint(lorenz, x_0, t)

j=[row[0] for row in xt]
k=[row[1] for row in xt]
l=[row[2] for row in xt]

for i in range(nsteps-1):
    if l[i] < z_val < l[i+1] or l[i] > z_val > l[i+1]:
        continue
    else:
        j[i], k[i] = 'a', 'a'
if not z_val*0.99 < l[-1] < z_val*1.01:
    j[-1], k[-1] = 'a', 'a'

i = 0
while 'a' in j:
    if j[i] == 'a':
        del j[i]
        del k[i]
        del l[i]
    else:
        i += 1 

pt.ylabel('y')
pt.xlabel('x')
pt.title('nsteps=25000,        r=''{}'.format(a))
pt.plot(j, k, 'r+', markersize = 3)
pt.savefig('r=''{}'.format(a), format = 'jpg', dpi=250)


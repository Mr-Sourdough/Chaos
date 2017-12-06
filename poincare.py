import matplotlib.pyplot as pt
from scipy import integrate
import numpy as np

pt.rcParams.update({'font.size': 8})

a=28

z_val=a-1

def lorenz(vec, t0, s=10, b=8/3, r=a):
    (x,y,z)=vec
    return [s*(y-x), x*(r-z)-y, x*y-b*z]

x_0 = [1,-1,20]

ti=0
tf=100
    
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
if not z_val*0.95 < l[-1] < z_val*1.05:
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
pt.title('r=''{}'.format(nsteps))
pt.plot(j, k, 'b+', markersize = 4)
pt.savefig('{}'.format(nsteps), format = 'jpg', dpi=250)


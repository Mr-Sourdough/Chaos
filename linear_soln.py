import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import exp
from Lorenz_Equations import lorenz_eq

"""
Calibrated to have identical number of points to measure real error
(when h is constant).

"""

brsigma = (1, 4, 1)
x_0 = np.array([1, -1, 2])
h = 0.01

# Jacobian matrix calculated at origin
Jacobian_origin = np.array([[-brsigma[2], brsigma[2], 0],
                            [brsigma[1], -1, 0],
                            [0, 0, -brsigma[0]]])

# Eigenvalues and eigenvectors of the metrix
val, vec = np.linalg.eig(Jacobian_origin)

# Initialise plot lists
xs = np.array([x_0[0]])
ys = np.array([x_0[1]])
zs = np.array([x_0[2]])

# Calculate constant vector for initial condition x_0
C = np.linalg.solve(vec, x_0)

for t in np.arange(0+h, 1.0, h):
    x = x_0 * 0
    for i in range(3):
        x = np.add(x, C[i] * vec[:, i] * exp(val[i]*t))
    xs = np.append(xs, x[0])
    ys = np.append(ys, x[1])
    zs = np.append(zs, x[2])

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x_0[0], x_0[1], x_0[2])
ax.plot(xs, ys, zs)
lorenz_eq(brsigma, 1.0, h, [x_0], linearise=True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import exp

"""
-Need to cater for non-constant h
"""

fig = plt.figure("Exact Solution of Linear Approximation")
ax = Axes3D(fig)
ax.set_title("Exact Solution of Linear Approximation")
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')


def exact_lin_soln(brsigma, tmax, h, x_0, coord=True):
    # Jacobian matrix calculated at origin
    Jacobian_origin = np.array([[-brsigma[2], brsigma[2], 0],
                                [brsigma[1], -1, 0],
                                [0, 0, -brsigma[0]]])

    # Eigenvalues and eigenvectors & calc constant vector
    val, vec = np.linalg.eig(Jacobian_origin)
    C = np.linalg.solve(vec, x_0)

    # Initialise plot lists
    xs = np.array([x_0[0]])
    ys = np.array([x_0[1]])
    zs = np.array([x_0[2]])

    for t in np.arange(0+h, tmax+h, h):
        x = x_0 * 0
        for i in range(3):
            x = np.add(x, C[i] * vec[:, i] * exp(val[i]*t))
        xs = np.append(xs, x[0])
        ys = np.append(ys, x[1])
        zs = np.append(zs, x[2])

    if coord is True:
        return xs, ys, zs
    else:
        # creates 3d plot
        ax.scatter(x_0[0], x_0[1], x_0[2])
        ax.text(x_0[0], x_0[1], x_0[2],
                "({}, {}, {})".format(x_0[0], x_0[1], x_0[2]), )
        ax.plot(xs, ys, zs, lw=1.0)
        return fig


# val = [-1, 1]
#
# for i in val:
#     for j in val:
#         for k in val:
#             exact_lin_soln((2, 7, 1), 1.0, 0.01, np.array([i, j, k]), coord=False)
ax.scatter(0, 0, 0)
ax.text(0, 0, 0, "(0, 0, 0)")
plt.show()

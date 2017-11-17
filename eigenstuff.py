import numpy as np

# set standard parameters
b = 8 / 3
sigma = 10
r = 1.1

# make a 3x3 matrix
a = np.array([[-sigma, sigma, 0], [r, -1, 0], [0, 0, -b]])
print(a)

# calculate eigenvalues and eigenvectors
evals, evecs = np.linalg.eig(a)
print(evals)

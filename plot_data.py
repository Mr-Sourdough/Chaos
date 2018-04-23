from plotting_3d import lorenz_eq
import numpy as np
from timestepping import RE_rk4
import pickle

xs, ys, zs = lorenz_eq((8/3, 28, 10), 10.0, 0.01, np.array([1, 0, 0]), RE_rk4)

with open("plot_data.pickle", 'bw') as data:
    pickle.dump((list(xs), list(ys), list(zs)), file=data)

with open("plot_data.pickle", 'br') as data:
    coords = pickle.load(data)

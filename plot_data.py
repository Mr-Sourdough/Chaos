from plotting_3d import lorenz_eq
import numpy as np
from timestepping import RE_rk4
import pickle

xs, ys, zs = lorenz_eq((1, 20, 10), 30.0, 0.01, np.array([-1, 1, 1]), RE_rk4)

with open("plot_data.pickle", 'bw') as data:
    pickle.dump((list(xs), list(ys), list(zs)), file=data)

with open("plot_data.pickle", 'br') as data:
    coords = pickle.load(data)

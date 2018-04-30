from timestepping import step_rk2, step_rk4, step_rk64, step_rk65, RE_rk2, RE_rk4
from error_analysis import method_error_at_tmax
from matplotlib import pyplot as plt
import numpy as np

# initialise function parameters
methods = [step_rk2, step_rk4, step_rk64, step_rk65, RE_rk2, RE_rk4]
brsigma = (1, 4, 1)
x_0 = np.array([-1, 1, 1])

# initialise plot and plot lists
fig = plt.figure()
Error = []
step_sizes = [0.001 * 2**i for i in range(5)]

for method in methods:
    for h in step_sizes:
        h_err = method_error_at_tmax(brsigma, 1.0, h, x_0, method)
        Error.append(h_err)
    plt.loglog(step_sizes, Error, label="{}".format(method.__name__))
    Error = []  # clear the Error list

plt.legend()
plt.xlabel("$log(h)$")
plt.ylabel("$log(error)$")
plt.show()

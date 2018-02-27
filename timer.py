# Timing function to measure speed of code.
from time import time  # use timeit module instead
import timestepping as tstep

def timer(function, *args, **kwargs):
    t_1 = time()
    function(*args, **kwargs)
    t_2 = time()
    return t_2 - t_1

print(timer(tstep.step_rk2, lambda y: y, 1.0, 1, 8))

# Timing function to measure speed of code.
from time import time  # use timeit module instead
from euler import euler

def timer(function, *args, **kwargs):
    t_1 = time()
    function(*args, **kwargs)
    t_2 = time()
    return t_2 - t_1

print(timer(euler, lambda y: y, 1.0, 1, 8))

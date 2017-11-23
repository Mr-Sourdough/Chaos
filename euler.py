# Standard Euler method
def euler(f, y_prev, interval, n):
    h = interval / n  # define step size
    for step in range(n):
        y_next = y_prev + h * f(y_prev)
        y_prev = y_next  # reassign previous estimation of y with next
    print(y_next)
    return None

# this function assumes that initial condition (IC) is y(0) = y_prev
euler(lambda y: y, 1.0, 1, 8)

def modEuler(f, y_prev, interval, n):
    h = interval / n  # define step size
    for step in range(n):
        k_1 = h * f(y_prev)
        k_2 = h * f(y_prev + k_1)
        y_next = y_prev + 0.5 * (k_1 + k_2)
        y_prev = y_next  # reassign previous estimation of y with next
    print(y_next)
    return None

modEuler(lambda y: y, 1.0, 1, 8)

# The functions assume that initial condition (IC) is y(0) = y_prev


# Standard Euler method
def euler(f, y_prev, interval, n):
    h = interval / n  # define step size
    for step in range(n):
        y_next = y_prev + h * f(y_prev)
        y_prev = y_next  # reassign previous estimation of y with next
    print(y_next)
    return None


# Modified Euler method
def modEuler(f, y_prev, interval, n):
    h = interval / n  # define step size
    for step in range(n):
        k_1 = h * f(y_prev)
        k_2 = h * f(y_prev + k_1)
        y_next = y_prev + 0.5 * (k_1 + k_2)
        y_prev = y_next  # reassign previous estimation of y with next
    print(y_next)
    return None


# 4th order Runge-Kutta mathod
def rk4(f, y_prev, interval, n):
    h = interval / n  # define step size
    for step in range(n):
        k_1 = h * f(y_prev)
        k_2 = h * f(y_prev + 0.5 * k_1)
        k_3 = h * f(y_prev + 0.5 * k_2)
        k_4 = h * f(y_prev + k_3)
        y_next = y_prev + (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
        y_prev = y_next  # reassign previous estimation of y with next
    print(y_next)
    return None


euler(lambda y: y, 1.0, 1, 20)
modEuler(lambda y: y, 1.0, 1, 20)
rk4(lambda y: y, 1.0, 1, 20)

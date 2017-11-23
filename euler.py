# Standard Euler method
def euler(f, y_prev, h, n):
    for step in range(n):
        y_next = y_prev + h * f(y_prev)
        y_prev = y_next
    print(y_next)
    return None

# define the function f(y) as lambda y
f = lambda y: 5*y - 3

euler(f, 1.0, 0.25, 4)

# what are the initial conditions for this kind of equation?

# Standard Euler method
def euler(f, y_prev, h, n):
    for step in range(1, n + 1):
        y_next = y_prev + f(y_prev)
        y_prev = y_next
    print(y_next)


# need to look into defining f(y) for the euler() function

euler(f, 1, 0.25, 4)

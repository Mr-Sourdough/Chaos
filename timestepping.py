"""timestepping module"""

def calc_dxdt(x, b, r, sigma):
    # calculates the vector dx / dt for the Lorenz equations
    dxdt = 0 * x
    dxdt[0] = sigma * (x[1] - x[0])
    dxdt[1] = r * x[0] - x[1] - x[0] * x[2]
    dxdt[2] = x[0] * x[1] - b * x[2]
    return dxdt

def calc_dxdt_lin(x, b, r, sigma):
    # calculates the vector dx / dt for the linearized Lorenz equations
    dxdt = 0 * x
    dxdt[0] = sigma * (x[1] - x[0])
    dxdt[1] = r * x[0] - x[1]
    dxdt[2] = -b * x[2]
    return dxdt


def step_rk2(x, dt, b, r, sigma):
    # Runge-Kutta second order method
    k_1 = dt * calc_dxdt(x, b, r, sigma)
    k_2 = dt * calc_dxdt(x + 0.5 * k_1, b, r, sigma)
    x_out = x + k_2
    return x_out

def step_rk2_RE(x, dt, b, r, sigma):
    # Runge-Kutta two step method with Richardson Extrapolation
    k_1 = dt * calc_dxdt(x, b, r, sigma)
    k_2 = dt * calc_dxdt(x + 0.5 * k_1, b, r, sigma)
    x_large_step = x + k_2
    k_1 = 0.5 * dt * calc_dxdt(x, b, r, sigma)
    k_2 = 0.5 * dt * calc_dxdt(x + 0.5 * k_1, b, r, sigma)
    x_intermediate_step = x + k_2
    k_1 = 0.5 * dt * calc_dxdt(x_intermediate_step, b, r, sigma)
    k_2 = 0.5 * dt * calc_dxdt(x_intermediate_step + 0.5 * k_1, b, r, sigma)
    x_two_small_steps = x_intermediate_step + k_2
    # Richardson Extrapolation
    x_out = x_large_step + (x_large_step - x_two_small_steps)/3
    return x_out


def step_rk4(x, dt, b, r, sigma):
    # Runge-Kutta fourth order method
    k_1 = dt * calc_dxdt(x, b, r, sigma)
    k_2 = dt * calc_dxdt(x + 0.5 * k_1, b, r, sigma)
    k_3 = dt * calc_dxdt(x + 0.5 * k_2, b, r, sigma)
    k_4 = dt * calc_dxdt(x + k_3, b, r, sigma)
    x_out = x + (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
    return x_out

def step_rk4_RE(x, dt, b, r, sigma):
    # Runge Kutta four step method with Richardson Extrapolation
    k_1 = dt * calc_dxdt(x, b, r, sigma)
    k_2 = dt * calc_dxdt(x + 0.5 * k_1, b, r, sigma)
    k_3 = dt * calc_dxdt(x + 0.5 * k_2, b, r, sigma)
    k_4 = dt * calc_dxdt(x + k_3, b, r, sigma)
    x_large_step = x + (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
    k_1 = 0.5 * dt * calc_dxdt(x, b, r, sigma)
    k_2 = 0.5 * dt * calc_dxdt(x + 0.5 * k_1, b, r, sigma)
    k_3 = 0.5 * dt * calc_dxdt(x + 0.5 * k_2, b, r, sigma)
    k_4 = 0.5 * dt * calc_dxdt(x + k_3, b, r, sigma)
    x_intermediate_step = x + (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
    k_1 = 0.5 * dt * calc_dxdt(x_intermediate_step, b, r, sigma)
    k_2 = 0.5 * dt * calc_dxdt(x_intermediate_step + 0.5 * k_1, b, r, sigma)
    k_3 = 0.5 * dt * calc_dxdt(x_intermediate_step + 0.5 * k_2, b, r, sigma)
    k_4 = 0.5 * dt * calc_dxdt(x_intermediate_step + k_3, b, r, sigma)
    x_two_small_steps = x_intermediate_step + (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
    # Richardson Extrapolation
    x_out = x_large_step + (x_large_step - x_two_small_steps)/3
    return x_out

"""timestepping module"""
"""brsigma is a tuple containing
the b, r and sigma paramateres for the system"""


def calc_dxdt(x, brsigma, linearise=False):
    # Calculates the vector dx / dt for the Lorenz equations
    if linearise is False:
        dxdt = 0 * x
        dxdt[0] = brsigma[2] * (x[1] - x[0])
        dxdt[1] = brsigma[1] * x[0] - x[1] - x[0] * x[2]
        dxdt[2] = x[0] * x[1] - brsigma[0] * x[2]
    elif linearise is True:
        # linearised system
        dxdt = 0 * x
        dxdt[0] = brsigma[2] * (x[1] - x[0])
        dxdt[1] = brsigma[1] * x[0] - x[1]
        dxdt[2] = - brsigma[0] * x[2]
    return dxdt


def step_rk2(x, h, brsigma, linearise=False):
    # Runge-Kutta second order method
    k_1 = h * calc_dxdt(x, brsigma, linearise)
    k_2 = h * calc_dxdt(x + 0.5 * k_1, brsigma, linearise)
    x_out = x + k_2
    return x_out


def step_rk2_RE(x, h, brsigma, linearise=False):
    # Runge-Kutta two step method with Richardson Extrapolation
    k_1 = h * calc_dxdt(x, brsigma, linearise)
    k_2 = h * calc_dxdt(x + 0.5 * k_1, brsigma, linearise)
    x_large_step = x + k_2
    k_1 = 0.5 * h * calc_dxdt(x, brsigma, linearise)
    k_2 = 0.5 * h * calc_dxdt(x + 0.5 * k_1, brsigma, linearise)
    x_middle_step = x + k_2
    k_1 = 0.5 * h * calc_dxdt(x_middle_step, brsigma, linearise)
    k_2 = 0.5 * h * calc_dxdt(x_middle_step + k_1 / 2, brsigma, linearise)
    x_two_small_steps = x_middle_step + k_2
    # Richardson Extrapolation
    x_out = x_large_step + (x_large_step - x_two_small_steps)/3
    return x_out


def step_rk4(x, h, brsigma, linearise=False):
    # Runge-Kutta fourth order method
    k_1 = h * calc_dxdt(x, brsigma, linearise)
    k_2 = h * calc_dxdt(x + 0.5 * k_1, brsigma, linearise)
    k_3 = h * calc_dxdt(x + 0.5 * k_2, brsigma, linearise)
    k_4 = h * calc_dxdt(x + k_3, brsigma, linearise)
    x_out = x + (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
    return x_out


def step_rk4_RE(x, h, brsigma, linearise=False):
    # Runge Kutta four step method with Richardson Extrapolation
    k_1 = h * calc_dxdt(x, brsigma, linearise)
    k_2 = h * calc_dxdt(x + 0.5 * k_1, brsigma, linearise)
    k_3 = h * calc_dxdt(x + 0.5 * k_2, brsigma, linearise)
    k_4 = h * calc_dxdt(x + k_3, brsigma, linearise)
    x_large_step = x + (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
    k_1 = 0.5 * h * calc_dxdt(x, brsigma, linearise)
    k_2 = 0.5 * h * calc_dxdt(x + 0.5 * k_1, brsigma, linearise)
    k_3 = 0.5 * h * calc_dxdt(x + 0.5 * k_2, brsigma, linearise)
    k_4 = 0.5 * h * calc_dxdt(x + k_3, brsigma, linearise)
    x_middle_step = x + (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
    k_1 = 0.5 * h * calc_dxdt(x_middle_step, brsigma, linearise)
    k_2 = 0.5 * h * calc_dxdt(x_middle_step + k_1 / 2, brsigma, linearise)
    k_3 = 0.5 * h * calc_dxdt(x_middle_step + k_2 / 2, brsigma, linearise)
    k_4 = 0.5 * h * calc_dxdt(x_middle_step + k_3, brsigma, linearise)
    x_two_small_steps = x_middle_step + (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
    # Richardson Extrapolation
    x_out = x_large_step + (x_large_step - x_two_small_steps)/3
    return x_out


def step_midpoint(x, h, brsigma, linearise=False):
    k = x + 0.5 * h * calc_dxdt(x, brsigma, linearise)
    x_out = x + h * calc_dxdt(k, brsigma, linearise)
    return x_out


def Rich_Extrap(x, h, brsigma, method, linearise=False):
    x_1 = method(x, h, brsigma, linearise)
    x_temp = method(x, h/2, brsigma, linearise)
    x_2 = method(x_temp, h/2, brsigma, linearise)
    x_out = x_1 + (x_1 - x_2)/3
    return x_out

# def step_size(h, method, tol):
#     # Takes initial step size h and using local extrapolation extimates h_new
#     # Only to be used with NON-Extrapolated methods
#     y_1 = method(x, h, brsigma)
#     return h_new

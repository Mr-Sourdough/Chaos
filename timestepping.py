import numpy as np

"""
brsigma is a tuple containing the paramateres b, r and sigma
"""


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
    x_out = x + 0.5*(k_1 + k_2)
    return x_out


def step_rk4(x, h, brsigma, linearise=False):
    # Runge-Kutta fourth order method
    k_1 = h * calc_dxdt(x, brsigma, linearise)
    k_2 = h * calc_dxdt(x + 0.5 * k_1, brsigma, linearise)
    k_3 = h * calc_dxdt(x + 0.5 * k_2, brsigma, linearise)
    k_4 = h * calc_dxdt(x + k_3, brsigma, linearise)
    x_out = x + (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
    return x_out

def step_rk64(x, h, brsigma, linearise=False):
    # Runge-Kutta fourth order, six step method
    k_1 = h * calc_dxdt(x, brsigma, linearise)
    k_2 = h * calc_dxdt(x + 0.244 * k_1, brsigma, linearise)
    k_3 = h * calc_dxdt(x + 0.172 * k_1 + 11/64 * k_2, brsigma, linearise)
    k_4 = h * calc_dxdt(x + 0.084 * k_2 + 0.5 * k_3, brsigma, linearise)
    k_5 = h * calc_dxdt(x - 0.004 * k_1 - 15/64 * k_2 + 0.418 * k_3 + 9/16 * k_4, brsigma, linearise)
    k_6 = h * calc_dxdt(x + 0.568 * k_2 + 6/7 * k_3 - 1.11 * k_4 + 0.685 * k_5, brsigma, linearise)
    x_out = x + (0.066 * k_1 + 0.335 * k_2 + 0.06 * k_3 + 0.105 * k_4 + 32/90 * k_5 + 7/90 * k_6)
    return x_out


def step_rk65(x, h, brsigma, linearise=False):
    # Runge-Kutta fifth order, six step method
    k_1 = h * calc_dxdt(x, brsigma, linearise)
    k_2 = h * calc_dxdt(x + 2/5 * k_1, brsigma, linearise)
    k_3 = h * calc_dxdt(x + 11/64 * (k_1 + k_2), brsigma, linearise)
    k_4 = h * calc_dxdt(x + 0.5 * k_3, brsigma, linearise)
    k_5 = h * calc_dxdt(x + (3 * k_1 - 15 * k_2 + 24 * k_3 + 36 * k_4) / 64, brsigma, linearise)
    k_6 = h * calc_dxdt(x + (5 * k_2 + 6 * k_3 - 12 * k_4 + 8 * k_5) / 7, brsigma, linearise)
    x_out = x + (7 * k_1 + 32 * k_3 + 12 * k_4 + 32 * k_5 + 7 * k_6) / 90
    return x_out


def RE_rk2(x, h, brsigma, linearise=False):
    # Calculate large step x_large_h, then for two small steps and extrapolate
    x_large_h = step_rk2(x, h, brsigma, linearise)
    x_temp = step_rk2(x, h/2, brsigma, linearise)
    x_small_h = step_rk2(x_temp, h/2, brsigma, linearise)
    x_out = x_small_h + (x_small_h - x_large_h)/3
    return x_out


def RE_rk4(x, h, brsigma, linearise=False):
    # Calculate large step x_large_h, then for two small steps and extrapolate
    x_large_h = step_rk4(x, h, brsigma, linearise)
    x_temp = step_rk4(x, h/2, brsigma, linearise)
    x_small_h = step_rk4(x_temp, h/2, brsigma, linearise)
    x_out = x_small_h + (x_small_h - x_large_h)/15
    return x_out


def step_size(x, h, brsigma, method, tol, linearise=False):
    # Takes initial step size h and using local extrapolation estimates h_new
    # Only to be used with NON-Extrapolated methods
    method_name = method.__name__
    order = int(method_name[-1])
    x_large_h = method(x, 2*h, brsigma, linearise)
    x_temp = method(x, h, brsigma, linearise)
    x_small_h = method(x_temp, h, brsigma, linearise)
    error = np.linalg.norm(x_small_h - x_large_h)/(2 ** order - 1)
    theta = 0.9 * (tol * h / error)**(1/order)
    h_new = theta * h
    return h_new

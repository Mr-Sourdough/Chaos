"""timestepping module"""
import numpy as np

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


def step_rk4(x, h, brsigma, linearise=False):
    # Runge-Kutta fourth order method
    k_1 = h * calc_dxdt(x, brsigma, linearise)
    k_2 = h * calc_dxdt(x + 0.5 * k_1, brsigma, linearise)
    k_3 = h * calc_dxdt(x + 0.5 * k_2, brsigma, linearise)
    k_4 = h * calc_dxdt(x + k_3, brsigma, linearise)
    x_out = x + (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
    return x_out


def Rich_Extrap(x, h, brsigma, method, linearise=False):
    # Calculate large step x_large_h, then for two small steps and extrapolate
    x_large_h = method(x, h, brsigma, linearise)
    x_temp = method(x, h/2, brsigma, linearise)
    x_small_h = method(x_temp, h/2, brsigma, linearise)
    x_out = x_large_h + (x_large_h - x_small_h)/3
    return x_out


# def step_size(x, h, brsigma, method, tol, linearise):
#     # Takes initial step size h and using local extrapolation estimates h_new
#     # Only to be used with NON-Extrapolated methods
#     x_large_h = method(x, h, brsigma, linearise)
#     x_temp = method(x, h/2, brsigma, linearise)
#     x_small_h = method(x_temp, h/2, brsigma, linearise)
#     norm = np.linalg.norm(x_small_h - x_large_h)
#     return h_new

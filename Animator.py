from plotting_3d import draw_axes, lorenz_eq
from timestepping import RE_rk4
from matplotlib import animation

ax = draw_axes()
brsigma = (8/3, 28, 10)

line, = lorenz_eq(brsigma, 10.0, 0.01, RE_rk4, ax)

FinalPlot = draw_axes(title="Lorenz System")


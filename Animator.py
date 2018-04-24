"""
Warning!
Imagemagick needs to be installed on the machine
for this file to execute properly
"""

from plotting_3d import draw_axes, lorenz_eq
from timestepping import RE_rk4
from matplotlib import animation
from matplotlib import pyplot as plt
import pickle
plt.rcParams['animation.convert_path'] = 'C:/Program Files/ImageMagick-7.0.7-Q16/magick.exe'

with open("plot_data.pickle", 'br') as data:
    coords = pickle.load(data)

xs, ys, zs = coords
ax, final_plot = draw_axes(title="Lorenz System")
ax.set_xlim(left=-20, right=15)
ax.set_ylim(bottom=-30, top=30)
ax.set_zlim(bottom=0, top=40)
line, = ax.plot([], [], [])

def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

def animate(i):
    # two time steps per frame
    i *= 4
    # for each i get the values of the integration
    x = xs[:i]
    y = ys[:i]
    z = zs[:i]
    # plot the values as the line
    line.set_data(x, y)
    line.set_3d_properties(z)
    final_plot.canvas.draw()
    return line,

anim = animation.FuncAnimation(final_plot, animate, init_func=init,
                                frames=750, interval=20, blit=True)

gif_writer = animation.ImageMagickFileWriter()
anim.save('lorenz_animation.gif', writer=gif_writer)

# plt.show()

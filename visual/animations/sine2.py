import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

def animate(frame):
    ax.cla()
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    x = np.arange(0, (2*np.pi), 0.05)
    y = np.sin(x + frame/50)
    ax.plot(x, y, "gx")

def run():
    vari = animation.FuncAnimation(fig, animate, frames = 720, interval = 10)
    plt.show()

run()
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

#fig can be anything, can be bob for example

def animate(frame):
    ax.cla()
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 15)
    ax.plot(frame, 5, "bo")

def run():
    x = animation.FuncAnimation(fig, animate, frames = 12, interval = 100, repeat = False)
    plt.show()

run()
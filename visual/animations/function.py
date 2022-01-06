import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

def animate(frame):
  print(f"Frame number {frame}")

def run():
  x = animation.FuncAnimation(fig, animate, interval = 100, frames = 55)
  plt.show()
run()
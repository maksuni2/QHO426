import matplotlib.pyplot as plt

def display_line(x, y):
  plt.plot(x, y)
  plt.show()

def run_task1():
  print("Running...")
  x_values = [1, 2, 3, 4, 5]
  y_values = [1, 4, 9, 16, 25]
  display_line(x_values, y_values)

run_task1()
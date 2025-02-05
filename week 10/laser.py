from tech import Tech

class Laser(Tech):

  MAX_RANGE = 100

  def __init__(self):
    super().__init__()

  def __repr__(self):
    return "laser()"

  def activate():
    print("Laser has been activated.")

  def deactivate():
    print("Laser has been deactivated.")

  def fire(range_distance):
    if (range_distance > Laser.MAX_RANGE):
      print(f"Fired maximum range of {Laser.MAX_RANGE}")
    else:
      print(f"Fired a distance of {range_distance}")


if __name__ == "__main__":
  laser = Laser()
  print(repr(laser))
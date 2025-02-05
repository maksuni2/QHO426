from inhabitant import Inhabitant

class Alien(Inhabitant):

  def __init__(self):
    self.technology = []

  def __str__(self):
    return f"Alien has: {self.technology}."

  def __repr__(self):
    return f"alien(technology={self.technology})"

  def pickup(self, tech):
    self.technology.append(tech)

  def drop(self, tech):
    self.technology.remove(tech)


if __name__ == "__main__":
  alien = Alien()
  print(repr(alien))
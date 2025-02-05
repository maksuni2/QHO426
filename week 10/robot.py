from inhabitant import Inhabitant


class Robot(Inhabitant):
    # class attribute
    laws = "Protect, Obey and Survive"

    # A static method
    @staticmethod
    def the_laws():
        print(Robot.laws)

    # An initialiser (special instance method)
    def __init__(self, name="Robot", age=0):
        super().__init__(name, age)

    def __repr__(self):
        return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'

    def display(self):
        print(f"I am {self.name}")


if (__name__ == "__main__"):
    robot = Robot()
    Robot.the_laws()
    print(repr(robot))
    robot.move(10)
    print(repr(robot))
    robot.eat(5)
    print(repr(robot))
    robot.eat(20)
    print(repr(robot))
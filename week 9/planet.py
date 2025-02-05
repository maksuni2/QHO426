class Planet:
    def __init__(self, name):
        self.name = name
        self.inhabitants = {
            'humans': [],
            'robots': []
        }

    def __repr__(self):
        return f"Planet(name={self.name}, humans={len(self.inhabitants['humans'])}, robots={len(self.inhabitants['robots'])})"

    def __str__(self):
        return f"This planet has {len(self.inhabitants['humans'])} humans and {len(self.inhabitants['robots'])} robots."

    def add_human(self, human):
        self.inhabitants['humans'].append(human)

    def add_robot(self, robot):
        self.inhabitants['robots'].append(robot)
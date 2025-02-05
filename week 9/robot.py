class Robot:
    def __init__(self, model):
        self.model = model

    def __repr__(self):
        return f"Robot({self.model})"
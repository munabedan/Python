# Create a class
class Point:

    # Initialise a class

    def __init__(self, x, y):
        self.move(x, y)

    # Move to new coordinates

    def move(self, x, y):
        self.x = x
        self.y = y

    # reset coordinates to 0,0

    def reset(self):
        self.move(0, 0)

import math


class Point:
    """Represents a point in 2D space.
    """
    
    def __init__(self, x=0, y=0):
        """Initialise the position of a new point, the coordinates can be specified if notn it defaults to 0,0.

        Args:
            x (int, optional): This is the x coordinate of your point. Defaults to 0.
            y (int, optional): This is the y coordinate of your point. Defaults to 0.
        """

        self.move(x, y)
        

    def move(self, x, y):
        """_summary_

        Args:
            x (int): This is the x coordinate of your point.
            y (int): This is the y coordinate of your point.
        """
        self.x = y
        self.y = y

    def reset(self):
        """This method will reset the coodinates to 0,0.
        """
        self.move(0, 0)
        

    def calculate_distance(self, other_point):
        """Calculates the Pythagorean Distance between this point and the other_point.

        Args:
            other_point (Point): This is the Point object of your other coordinates.

        Returns:
            float: Pythagorean Distance between this point and the other_point.
        """

        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)


p1 = Point(6,6)
p2 = Point(2,2)

print(p1.calculate_distance(p2))

import math


class Point:
    'Represents a point in two-dimensional geometric coordinates'

    def __init__(self, x=0, y=0):
        '''Initialise the position of a new point. 
        The x and y coordinates can be specified. 
        If they are not , the point defaults to origin.
        '''
        self.move(x, y)

    def move(self, x, y):
        'Move the point to a new location in 2D space.'
        self.x = y
        self.y = y

    def reset(self):
        'Reset the point back to the geometric origin: 0,0'
        self.move(0, 0)

    def calculate_distance(self, other_point):
        '''Calulate the distance from this point to a second point passed as a parameter.
            This function uses the pythagorean Theorem to calculate the distance between two points. The distance is returned as a float.
        '''

        return math.sqrt(
            (self.x - other_point)**2 +
            (self.y - other_point)**2
        )

p = Point()
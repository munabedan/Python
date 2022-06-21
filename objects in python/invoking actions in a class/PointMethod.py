# Define a class named Point
class Point:

    # The class has a method reset
    def reset(self):
        p.x = 0
        p.y = 0


# Instantiate a point p
p = Point()

# call the method reset in object p
p.reset()

# Print the attributes of both objects
print("p = ", p.x, p.y)

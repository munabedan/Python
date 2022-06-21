# create class point

class Point:

    # initalize the class with default 0,0 coordinates

    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
        pass
    
# instantiate the object

p = Point()
print(p.x,p.y)




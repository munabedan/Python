
from cmath import sqrt
import math

"Define a class named Point"
class Point:

    "The class has no methods or attributes"
    pass



"Define a distance calculaor class"
class DistanceCalculator:

    "define a calculate method"
    def calculate (self, p1,p2):

        "use formula to calulate the distance"
        d= (p2.x-p1.x)^2 + (p2.y-p1.y)^2
        distance=sqrt(d)
        print(distance)
        
"Instantiate two objects of class Point"
p1 = Point()
p2 = Point()


"Assign x and y attributes to both objects"
p1.x = 5 
p1.y = 0

p2.x = 3
p2.y = 4

"Instantiate a distance calculator object"
calculator =  DistanceCalculator()


"call the method calculate to calculate the distance"
calculator.calculate(p1,p2)

"""
Write a class Point that models a 2 dimensional point (x,y). The UML diagram is
as follows:

The Point class has 2 instance variables, x and y.
It has a constructor that initializes 2 instance variables with the value of x and
y, with default values (0,0).

It has the following methods:
 Getter and setter properties for x and y .
 A move(dx, dy) method that moves to (x+dx, y+dy).
 A distanceTo(aPoint) method that returns the distance to another point
(x1, y1). The distance is calculated by this formula:
distance = ((x − x1)^2+ (y − y1)^2)^0.5
 A quadrant() method that returns the quadrant of the point as follows:
For any point along x or y axis, return 0.
 A __str__() method that returns the string value in this format: (x, y)

Test the Point class, with the following:
i. Create a point object p1, at (5, 1)
ii. Print the coordinates of p1
iii. Move p1 by delta (5, -5)
iv. Create another point p2 at (10 , -10)
v. Print the distance between p1 and p2
vi. Print the quadrants for p1 and p2
"""

class Point:
    def __init__(self, x: float = None, y: float = None):
        self.__x = 0 if x is None else x
        self.__y = 0 if y is None else y

    def getX(self) -> float:
        return self.__x
    
    def getY(self) -> float:
        return self.__y
    
    def x(self, x: float):
        self.__x = x
    
    def y(self, y: float):
        self.__y = y

    def move(self, dx: float, dy: float):
        self.__x += dx
        self.__y += dy

    def distanceTo(self, p: object) -> float:
        distance = ((self.getX() - p.getX())**2 + (self.getY() - p.getY())**2)**0.5
        return distance
    
    def quadrant(self):
        x = self.getX()
        y = self.getY()
        if (x == 0 and y == 0):
            return 0
        if (x > 0 and y > 0):
            return 1
        if (x < 0 and y > 0):
            return 2
        if (x < 0 and y < 0):
            return 3
        if (x > 0 and y < 0):
            return 4
        
def main():
    p0 = Point()
    print('p0: ({0},{1})'.format(p0.getX(), p0.getY()))
    p1 = Point(5, 1)
    print('p1: ({0},{1})'.format(p1.getX(), p1.getY()))
    p1.move(5, -5)
    p2 = Point(10, -10)
    print('p1: ({0},{1})'.format(p1.getX(), p1.getY()))
    print('p2: ({0},{1})'.format(p2.getX(), p2.getY()))
    print('Distance between p1 and p2: {0}'.format(p1.distanceTo(p2)))
    print('p1 is in quadrant {0}'.format(p1.quadrant()))
    print('p2 is in quadrant {0}'.format(p2.quadrant()))

main()
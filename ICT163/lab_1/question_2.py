"""
Write a class that models a Rectangle. The class diagram is given as follows:

A Rectangle class has 2 instance variables – length (float) and width (float).

It has a constructor that initializes the length and width. It also has get/set
methods for the length and width.

It has the following methods:
 getArea() that returns the area of the rectangle
 getPerimeter() that returns the perimeter of the rectangle
 increaseSize(deltaLength, deltaWidth) that increases the length and
width of the rectangle by deltaLength and deltaWidth respectively.
 isBigger(rect) that has another rectangle as parameter. The method
returns True if the current area is bigger than the area of the rectangle
rect and False otherwise.
 __str__() method that returns a string representation of a Rectangle
object, including its area and perimeter as in:
Length: 2.0 Width: 5.0 Area: 10.0 Perimeter: 14.0

Test out the Rectangle class with the following statements:
i. Create a Rectangle object r1 with any dimension.
ii. Print the details of r1.
iii. Increase the size of the rectangle by 10 units on both sides.
iv. Print the details of r1 again.
v. Create another rectangle r2 with any dimension.
vi. Print the area and perimeter using the getArea() and getPerimeter() methods.
vii. Compare r1 with r2 using the isBigger() method. Display the outcome.
"""

class Rectangle:
    def __init__(self, length: float, width: float):
        self.__length = length
        self.__width = width

    def getLength(self) -> float:
        return self.__length
    
    def length(self, newLength: float):
        self.__length = newLength

    def getWidth(self) -> float:
        return self.__width
    
    def width(self, newWidth: float):
        self.__width = newWidth
    
    def getArea(self) -> float:
        area = self.__length * self.__width
        return area

    def getPerimeter(self) -> float:
        perimeter = 2 * (self.__width + self.__length)
        return perimeter
    
    def increaseSize(self, deltaLength: float, deltaWidth: float):
        self.__width += deltaWidth
        self.__length += deltaLength
    
    def isBigger(self, rect: object):
        if type(rect) == Rectangle:
            return self.getArea() > rect.getArea()
        return 'Invalid argument passed'
    
    def __str__(self) -> str:
        length = 'Length: {0:<6.2f}'.format(self.getLength())
        width = 'Width: {0:<6.2f}'.format(self.getWidth())
        area = 'Area: {0:<6.2f}'.format(self.getArea())
        perimeter = 'Perimeter: {0:<6.2f}'.format(self.getPerimeter())
        return '{0} {1} {2} {3}'.format(length, width, area, perimeter)

def main():
    r1 = Rectangle(10, 5)
    print('r1 (before increasing its size): ', r1)
    r1.increaseSize(10, 10)
    print('r1 (after increasing its size): ', r1)
    r2 = Rectangle(25, 30)
    print('Area of r2: {0:.<6.2f}'.format(r2.getArea()))
    print('Perimeter of r2: {0:.<6.2f}'.format(r2.getPerimeter()))
    r1ComparedToR2 = 'same as' if r1.getArea()== r2.getArea() else 'bigger than' if r1.isBigger(r2) else 'smaller than'
    print('r1 is {0} r2'.format(r1ComparedToR2))

main()
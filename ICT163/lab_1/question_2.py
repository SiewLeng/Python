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
        else:
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
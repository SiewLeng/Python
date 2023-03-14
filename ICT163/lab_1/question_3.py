class Point:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

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
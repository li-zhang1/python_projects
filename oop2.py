"""
This program is to implement a plan with the Cartesian coordinate system
"""
import math
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot( abs(x - self.__x), abs(y - self.__y))

    def distance_from_point(self, point):
        return math.hypot(abs(point.getx() - self.__x),abs(point.gety() - self.__y))


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))

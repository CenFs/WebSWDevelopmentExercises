# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 22:22:06 2017

@author: Jingyi
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_from(self, Point):
        x1 = self.x
        x2 = Point.x
        y1 = self.y
        y2 = Point.y
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    
class Circle:
    def __init__(self, center, radius):
        self.center = Point(center.x, center.y)
        self.radius = radius
    def is_inside(self, Point):
        x1 = self.center.x
        x2 = Point.x
        y1 = self.center.y
        y2 = Point.y
        d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        r = self.radius
        if d >= r:
            return False
        else:
            return True


"""
p1 = Point(0,0)
p2 = Point(2,4)
p1.distance_from(p2)
circle = Circle(p2,4)
circle.is_inside(p1)
circle.is_inside(Point(2,2))
"""